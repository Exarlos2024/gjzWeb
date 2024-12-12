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
          @click="$router.push('/otherfuncs/about')"
        />
        <UButton
          variant="solid"
          class="nav-button"
          label="常用链接"
          @click="$router.push('/otherfuncs/links')"
        />
      </div>
      <div class="right-nav">
        <template v-if="isLoggedIn">
          <div class="user-info">
            <nuxt-link to="/user/settings" class="username-link">
              <div class="user-avatar">
                <span class="avatar-text">{{ username.charAt(0).toUpperCase() }}</span>
              </div>
              <span class="username">{{ username }}</span>
            </nuxt-link>
            <UButton
              variant="solid"
              class="logout-button"
              label="退出"
              @click="handleLogout"
            />
          </div>
        </template>
        <template v-else>
          <nuxt-link to="/login" class="sign-in-button">登录</nuxt-link>
          <nuxt-link to="/reg" class="sign-up-button">注册</nuxt-link>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { navMenus } from "~/constants/navigation"

const router = useRouter()
const isLoggedIn = ref(false)
const username = ref('')

// 检查登录状态
const checkLoginStatus = () => {
  const token = localStorage.getItem('token')
  const storedUsername = localStorage.getItem('username')
  
  if (token && storedUsername) {
    isLoggedIn.value = true
    username.value = storedUsername
  } else {
    isLoggedIn.value = false
    username.value = ''
  }
}

// 退出登录
const handleLogout = () => {
  // 清除本地存储的用户信息
  localStorage.removeItem('token')
  localStorage.removeItem('username')
  localStorage.removeItem('user_id')
  
  // 更新状态
  isLoggedIn.value = false
  username.value = ''
  
  // 跳转到登录页
  router.push('/login')
}

// 组件挂载时检查登录状态
onMounted(() => {
  checkLoginStatus()
})
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
  align-items: center;
  gap: 1rem;
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

.username-link {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.username-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.avatar-text {
  text-transform: uppercase;
}

.username {
  color: white;
  font-size: 15px;
  font-weight: 500;
  white-space: nowrap;
}

.logout-button {
  display: inline-flex !important;
  align-items: center !important;
  padding: 6px 16px !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-radius: 6px !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  background-color: rgba(255, 255, 255, 0.1) !important;
  color: white !important;
  transition: all 0.3s ease !important;
  margin-left: 0.5rem !important;
  white-space: nowrap !important;
}

.logout-button:hover {
  background-color: rgba(255, 255, 255, 0.2) !important;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 响应式调整 */
@media (max-width: 768px) {
  .user-info {
    gap: 0.5rem;
  }

  .username-link {
    padding: 0.25rem;
  }

  .user-avatar {
    width: 28px;
    height: 28px;
    font-size: 14px;
  }

  .username {
    font-size: 14px;
  }

  .logout-button {
    padding: 4px 12px !important;
    font-size: 13px !important;
  }
}
</style>
