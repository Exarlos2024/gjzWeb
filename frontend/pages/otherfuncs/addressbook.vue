<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 00:30:48
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 14:38:38
 * @Description: 通讯录页面
-->
<template>
  <DefaultLayout>
    <div class="contact-list-container">
      <h1>通讯录</h1>
      <div v-if="!contacts.length" class="no-contacts">暂无通讯录条目</div>
      <div v-else>
        <div class="contact-tree">
          <ContactNode v-for="contact in contacts" :key="contact.id" :contact="contact" />
        </div>
      </div>
      <nuxt-link v-if="isAdmin" to="/otherfuncs/addressbookadd" class="add-button">添加通讯录条目</nuxt-link>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'
import DefaultLayout from "~/components/layout/DefaultLayout.vue"; // 引入 DefaultLayout
import ContactNode from "~/components/ContactNode.vue"; // 引入自定义联系人节点组件

// 模拟的联系人数据
const contacts = ref([
  {
    id: 1,
    name: "张新龙",
    position: "局长",
    office: "301",
    office_phone: "123456789",
    handphone: "13812345678",
    level: "1",
    children: [
      {
        id: 2,
        name: "分公司1",
        position: "经理",
        office: "302",
        office_phone: "987654321",
        handphone: "13912345678",
        level: "2",
        children: [
          {
            id: 3,
            name: "部门1",
            position: "主管",
            office: "303",
            office_phone: "555555555",
            handphone: "14012345678",
            level: "3",
            children: []
          },
          {
            id: 4,
            name: "部门2",
            position: "主管",
            office: "304",
            office_phone: "444444444",
            handphone: "14112345678",
            level: "3",
            children: []
          }
        ]
      },
      {
        id: 5,
        name: "分公司2",
        position: "经理",
        office: "305",
        office_phone: "666666666",
        handphone: "14212345678",
        level: "2",
        children: [
          {
            id: 6,
            name: "部门3",
            position: "主管",
            office: "306",
            office_phone: "333333333",
            handphone: "14312345678",
            level: "3",
            children: []
          }
        ]
      }
    ]
  }
]);

// 模拟用户角色，实际应用中应从用户认证系统获取
const isAdmin = ref(true); // 将其设置为 true 或 false 以模拟管理员状态
</script>

<style scoped>
.contact-list-container {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #f0f4f8; /* 背景颜色 */
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

.add-button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4CAF50; /* 按钮背景颜色 */
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.3s;
}

.add-button:hover {
  background-color: #45a049; /* 悬停效果 */
  transform: translateY(-2px);
}

/* 树形结构样式 */
.contact-tree {
  text-align: left;
}
</style>
