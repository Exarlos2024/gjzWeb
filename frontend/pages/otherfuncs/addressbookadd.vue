<template>
  <DefaultLayout>
    <div class="add-contact-container">
      <h1>添加通讯录条目</h1>
      <form @submit.prevent="addContact">
        <div class="form-group">
          <label for="name">姓名:</label>
          <input type="text" v-model="name" required />
        </div>
        <div class="form-group">
          <label for="position">职位:</label>
          <input type="text" v-model="position" required />
        </div>
        <div class="form-group">
          <label for="office">办公室:</label>
          <input type="text" v-model="office" required />
        </div>
        <div class="form-group">
          <label for="office_phone">办公电话:</label>
          <input type="text" v-model="office_phone" required />
        </div>
        <div class="form-group">
          <label for="handphone">手机:</label>
          <input type="text" v-model="handphone" required />
        </div>
        <div class="form-group">
          <label>级别:</label>
          <div class="radio-group">
            <label>
              <input type="radio" value="1" v-model="level" required />
              局长
            </label>
            <label>
              <input type="radio" value="2" v-model="level" required />
              副局长
            </label>
            <label>
              <input type="radio" value="3" v-model="level" required />
              科长
            </label>
            <label>
              <input type="radio" value="4" v-model="level" required />
              科员
            </label>
          </div>
        </div>
        <button type="submit" class="submit-button">提交</button>
      </form>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import DefaultLayout from "~/components/layout/DefaultLayout.vue"; // 引入 DefaultLayout
import Contact from '~/utils/Contact.js'; // 引入 Contact 类

const name = ref('')
const position = ref('')
const office = ref('')
const office_phone = ref('')
const handphone = ref('')
const level = ref('') // 级别字段，保存为数字
const router = useRouter()

const addContact = async () => {
  const contact = new Contact(name.value, position.value, office.value, office_phone.value, handphone.value, level.value);

  const response = await fetch('/api/contacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(contact.toJSON()) // 使用 toJSON 方法
  })

  if (response.ok) {
    router.push('/otherfuncs') // 添加成功后重定向到通讯录页面
  } else {
    alert('添加失败，请重试')
  }
}
</script>

<style scoped>
.add-contact-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input[type="text"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.radio-group {
  display: flex; /* 使用 flexbox */
  justify-content: space-around; /* 在主轴上均匀分布 */
  margin-top: 0.5rem; /* 添加顶部间距 */
}

.radio-group label {
  margin: 0 10px; /* 添加左右间距 */
}

.submit-button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.3s;
}

.submit-button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}
</style>
