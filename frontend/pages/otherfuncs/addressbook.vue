<template>
  <DefaultLayout>
    <div class="contact-list-container">
      <h1>通讯录</h1>
      <div v-if="error" class="error-message">获取联系人数据失败: {{ error.message }}</div>
      <div v-if="!contacts || !contacts.length" class="no-contacts">暂无通讯录条目</div>
      <div v-else>
        <div class="contact-tree">
          <ContactNode v-for="contact in sortedContacts" :key="contact.id" :contact="contact" />
        </div>
      </div>
      <nuxt-link v-if="userPermissions.can_add_contact" to="/otherfuncs/addressbookadd" class="add-button">添加通讯录条目</nuxt-link>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAsyncData } from 'nuxt/app'
import DefaultLayout from "~/components/layout/DefaultLayout.vue"; // 引入 DefaultLayout
import ContactNode from "~/components/ContactNode.vue"; // 引入 ContactNode 组件

const userPermissions = ref({ can_add_contact: false }); // 用户权限

// 获取 Token
const token = localStorage.getItem('token'); // 从 localStorage 获取 Token

// 使用 useAsyncData 获取用户权限
const { data: permissionsData, error: permissionsError } = await useAsyncData('user_permissions', async () => {
  const response = await $fetch('http://localhost:8000/api/user/permissions/', {  // 确保这个 URL 是正确的
    headers: {
      Authorization: `Token ${token}` // 在请求头中添加 Token
    }
  });
  return response; // 返回获取到的用户权限数据
});

// 设置用户权限
if (permissionsData.value) {
  userPermissions.value = permissionsData.value; // 假设返回的数据结构包含权限
}

// 使用 useAsyncData 获取联系人数据
const { data: contacts, error } = await useAsyncData('contacts', async () => {
  const response = await $fetch('http://localhost:8000/api/contacts/', {
    headers: {
      Authorization: `Token ${token}` // 在请求头中添加 Token
    }
  });
  return response; // 返回获取到的数据
});

// 错误处理
if (error.value) {
  console.error("获取联系人数据失败:", error.value);
}

// 级别排序和树形结构构建
const sortedContacts = computed(() => {
  const levelOrder = {
    '局长': 1,
    '副局长': 2,
    '科长': 3,
    '科员': 4
  };

  // 按级别排序
  const sorted = contacts.value.sort((a, b) => levelOrder[a.level] - levelOrder[b.level]);

  // 构建树形结构
  const contactMap = {};
  sorted.forEach(contact => {
    contactMap[contact.id] = { ...contact, children: [] };
  });

  const tree = [];
  sorted.forEach(contact => {
    if (contact.leader) {
      const leaderId = sorted.find(c => c.name === contact.leader)?.id;
      if (leaderId) {
        contactMap[leaderId].children.push(contactMap[contact.id]);
      } else {
        tree.push(contactMap[contact.id]);
      }
    } else {
      tree.push(contactMap[contact.id]);
    }
  });

  return tree;
});
</script>

<style scoped>
.contact-list-container {
  max-width: 1200px; /* 增加最大宽度 */
  margin: 2rem auto;
  padding: 2rem;
  background-color: #f9f9f9; /* 背景颜色 */
  border-radius: 12px; /* 圆角 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.no-contacts {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1rem;
}

.error-message {
  color: red;
  font-size: 1.2rem;
}

.contact-tree {
  text-align: left;
}

.add-button {
  display: inline-block;
  margin-top: 1rem;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s;
}

.add-button:hover {
  background-color: #45a049;
}
</style>