<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 14:29:27
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-07 17:10:39
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <nav class="main-nav">
    <div class="nav-content">
      <div class="left-nav">
        <nuxt-link to="/">
          <img src="/images/Exarlos.png" alt="Logo" class="logo" />
        </nuxt-link>
        <nuxt-link to="/" class="nav-link">回到主页</nuxt-link>
        <nuxt-link to="/about" class="nav-link">关于</nuxt-link>
      </div>
      <div class="right-nav">
        <span>还没有账号？</span>
        <nuxt-link to="/reg" class="sign-up-button">注册</nuxt-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
// 这里可以添加任何需要的脚本逻辑
</script>

<style scoped>
.main-nav {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #24292f;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
}

.right-nav {
  display: flex;
  gap: 8px;
  align-items: center;
}

.sign-up-button {
  background-color: #24292f;
  color: white;
  padding: 5px 12px;
  border-radius: 6px;
  font-weight: 500;
  text-decoration: none;
}

.sign-up-button:hover {
  background-color: #3b3f45;
}
</style> 