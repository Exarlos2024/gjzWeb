<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 14:30:06
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 13:29:48
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <DefaultLayout>
    <div class="login-page">
      <div class="form-container">
        <h2 class="form-title">登录</h2>
        <form @submit.prevent="handleSubmit">
          <div class="form-group">
            <label for="email">邮箱</label>
            <input type="email" id="email" v-model="form.email" required />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" id="password" v-model="form.password" required />
          </div>
          <button type="submit" class="submit-button">登录</button>
          <div class="form-footer">
            <NuxtLink to="/reg" class="register-link">
              还没有账号？点击注册
            </NuxtLink>
          </div>
        </form>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'
import DefaultLayout from '~/components/layout/DefaultLayout.vue'

const form = ref({
  email: '',
  password: ''
})

const handleSubmit = () => {
  console.log('提交的表单数据:', form.value)
}
</script>

<style scoped>
.login-page {
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

.register-link {
  color: #1a73e8;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.register-link:hover {
  color: #174ea6;
  text-decoration: underline;
}
</style> 