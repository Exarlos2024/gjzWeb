<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 13:29:24
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 13:31:19
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <DefaultLayout>
    <div class="register-page">
      <div class="form-container">
        <h2 class="form-title">注册</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" id="username" v-model="form.username" required />
          </div>
          <div class="form-group">
            <label for="email">邮箱</label>
            <input type="email" id="email" v-model="form.email" required />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" id="password" v-model="form.password" required />
          </div>
          <div class="form-group">
            <label for="organization">组织名称</label>
            <input type="text" id="organization" v-model="form.organization" />
          </div>
          <div class="form-group">
            <label for="telephone">电话号码</label>
            <input type="text" id="telephone" v-model="form.telephone" />
          </div>
          <button type="submit" class="submit-button">注册</button>
          <div class="form-footer">
            <NuxtLink to="/login" class="login-link">
              已有账号？点击登录
            </NuxtLink>
          </div>
        </form>
        <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue' // 从 Vue 中导入 ref，用于创建响应式数据
import { useRouter } from 'vue-router' // 从 vue-router 中导入 useRouter，用于路由导航
import DefaultLayout from '~/components/layout/DefaultLayout.vue' // 导入默认布局组件

// 创建一个响应式对象 form，用于存储表单数据
const form = ref({
  username: '', // 用户名
  email: '', // 邮箱
  password: '', // 密码
  organization: '', // 组织名称
  telephone: '' // 电话号码
})

// 创建一个响应式变量 errorMessage，用于存储错误信息
const errorMessage = ref('')
// 获取路由实例，用于页面导航
const router = useRouter()

// 定义一个异步函数 handleSubmit，用于处理表单提交
const handleSubmit = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // 请求头，指定内容类型为 JSON
      },
      body: JSON.stringify(form.value), // 将表单数据转换为 JSON 字符串并作为请求体发送
    });

    // 检查响应是否成功
    if (response.ok) {
      const data = await response.json(); // 解析响应数据
      console.log('注册成功:', data); // 在控制台输出成功信息
      // 注册成功后，重定向到登录页面
      router.push('/login');
    } else {
      const errorData = await response.json(); // 解析错误响应数据
      console.error('注册失败:', errorData); // 在控制台输出错误信息
      errorMessage.value = '注册失败，请检查输入信息。'; // 更新错误信息
    }
  } catch (error) {
    console.error('请求失败:', error); // 在控制台输出请求失败信息
    errorMessage.value = '网络错误，请稍后重试。'; // 更新错误信息
  }
}
</script>

<style scoped>
.register-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
  bottom: 0;
}

.form-container {
  background: rgba(255, 255, 255, 0.9);
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 100%;
  margin: 20px;
  backdrop-filter: blur(10px);
  position: relative;
  z-index: 1;
}

.form-title {
  margin-bottom: 24px;
  font-size: 28px;
  text-align: center;
  color: #333;
  font-weight: bold;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #555;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

.submit-button {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.submit-button:hover {
  background-color: #5a67d8;
  transform: translateY(-2px);
}

.form-footer {
  margin-top: 20px;
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

.login-link {
  color: #1a73e8;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.login-link:hover {
  color: #174ea6;
  text-decoration: underline;
}
</style> 