<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 00:30:48
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 14:38:38
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <nav class="main-nav">
    <div class="nav-content">
      <div class="left-nav">
        <div class="logo-hint">
          主页请点击 <span class="arrow">→</span>
        </div>
        <nuxt-link to="/">
          <img src="/images/logo2.png" alt="Logo" class="logo" />
          <!-- <img src="/images/sibuleisi.jpg" alt="Logo" class="logo" /> -->
        </nuxt-link>
        <UDropdown
          v-for="menu in navMenus"
          :key="menu.label"
          :items="menu.items"
          :popper="{
            placement: 'bottom-start',
            strategy: 'fixed',
          }"
          class="github-dropdown"
        >
          <UButton
            variant="solid"
            class="nav-button"
            :label="menu.label"
            trailing-icon="i-heroicons-chevron-down-20-solid"
          />
        </UDropdown>
        <UButton
          variant="solid"
          class="nav-button"
          label=" 关于"
          @click="$router.push('/about')"
        />
        <UButton
          variant="solid"
          class="nav-button"
          label="常用链接"
          @click="$router.push('/links')"
        />
      </div>
      <div class="right-nav">
        <nuxt-link to="/login" class="sign-in-button">登录</nuxt-link>
        <nuxt-link to="/reg" class="sign-up-button">注册</nuxt-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { navMenus } from "~/constants/navigation";
</script>

<style scoped>
.main-nav {
  width: 100%;
  background-color: #1a1a1a;
  padding: 0.5rem 8rem;
}

.nav-content {
  max-width: 1800px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10rem;
}

.left-nav {
  display: flex;
  align-items: center;
  gap: 3.5rem;
}

.right-nav {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-left: auto;
}

.sign-in-button,
.sign-up-button {
  color: white !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  font-size: 18px !important;
  padding: 5px 12px !important;
  border-radius: 6px !important;
  font-weight: 500 !important;
  background-color: transparent !important;
}

.sign-in-button:hover,
.sign-up-button:hover {
  background-color: rgba(255, 255, 255, 0.1) !important;
}

/* GitHub风格的下拉菜单样式 */
:deep(.github-dropdown) {
  --dropdown-background: #ffffff;
  --dropdown-border: 1px solid #d0d7de;
  --dropdown-shadow: 0 8px 24px rgba(140, 149, 159, 0.2);
}

:deep(.github-dropdown .u-dropdown-item) {
  padding: 8px 16px !important;
  font-size: 14px !important;
  color: #24292f !important;
}

:deep(.github-dropdown .u-dropdown-item:hover) {
  background-color: #f6f8fa !important;
  color: #24292f !important;
}

/* 响应式设计调整 */
@media (max-width: 1400px) {
  .main-nav {
    padding: 0.5rem 6rem;
  }
  
  .nav-content {
    padding: 0 8rem;
  }
}

@media (max-width: 1200px) {
  .main-nav {
    padding: 0.5rem 4rem;
  }
  
  .nav-content {
    padding: 0 6rem;
  }
}

@media (max-width: 768px) {
  .main-nav {
    padding: 0.5rem 2rem;
  }
  
  .nav-content {
    padding: 0 3rem;
  }
  
  .left-nav, .right-nav {
    gap: 2rem;
  }
}

.logo-hint {
  display: flex;
  align-items: center;
  color: #ffffff;
  font-size: 14px;
  margin-right: 8px;
}

.arrow {
  display: inline-block;
  margin-left: 4px;
  font-size: 18px;
  animation: pointRight 1s infinite;
}

@keyframes pointRight {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(4px);
  }
}

.left-nav {
  display: flex;
  align-items: center;
  gap: 8px;
}

@media (max-width: 768px) {
  .logo-hint {
    display: none; /* 在移动端隐藏提示文字 */
  }
}
</style>
