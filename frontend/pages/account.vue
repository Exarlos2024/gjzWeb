<template>
  <DefaultLayout>
    <div class="account-page">
      <div class="account-container">
        <h2 class="page-title">我的账户</h2>
        
        <!-- 用户信息部分 -->
        <div class="user-info-section">
          <h3>基本信息</h3>
          <div class="info-grid">
            <div class="info-item">
              <label>用户名</label>
              <div class="value">{{ username }}</div>
            </div>
            <div class="info-item">
              <label>邮箱</label>
              <div class="value">{{ email }}</div>
            </div>
          </div>
        </div>

        <!-- 账户操作部分 -->
        <div class="account-actions">
          <h3>账户操作</h3>
          <div class="action-buttons">
            <UButton
              class="action-button"
              label="修改密码"
              @click="showChangePasswordModal = true"
            />
            <UButton
              class="action-button danger"
              label="注销账户"
              @click="showDeleteAccountModal = true"
            />
          </div>
        </div>

        <!-- 修改密码模态框 -->
        <UModal v-model="showChangePasswordModal">
          <div class="modal-content">
            <h3>修改密码</h3>
            <form @submit.prevent="handleChangePassword">
              <div class="form-group">
                <label>当前密码</label>
                <input
                  type="password"
                  v-model="passwordForm.currentPassword"
                  required
                />
              </div>
              <div class="form-group">
                <label>新密码</label>
                <input
                  type="password"
                  v-model="passwordForm.newPassword"
                  required
                />
              </div>
              <div class="form-group">
                <label>确认新密码</label>
                <input
                  type="password"
                  v-model="passwordForm.confirmPassword"
                  required
                />
              </div>
              <div class="modal-actions">
                <UButton type="submit" label="确认修改" />
                <UButton
                  variant="soft"
                  label="取消"
                  @click="showChangePasswordModal = false"
                />
              </div>
            </form>
          </div>
        </UModal>

        <!-- 注销账户确认模态框 -->
        <UModal v-model="showDeleteAccountModal">
          <div class="modal-content">
            <h3>注销账户</h3>
            <p class="warning-text">
              注意：账户注销后将无法恢复，请确认是否继续？
            </p>
            <div class="modal-actions">
              <UButton
                class="danger"
                label="确认注销"
                @click="handleDeleteAccount"
              />
              <UButton
                variant="soft"
                label="取消"
                @click="showDeleteAccountModal = false"
              />
            </div>
          </div>
        </UModal>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import DefaultLayout from '~/components/layout/DefaultLayout.vue'

const router = useRouter()
const username = ref('')
const email = ref('')
const showChangePasswordModal = ref(false)
const showDeleteAccountModal = ref(false)

const passwordForm = ref({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
})

// 加载用户信息
onMounted(() => {
  const storedUsername = localStorage.getItem('username')
  if (!storedUsername) {
    router.push('/login')
    return
  }
  username.value = storedUsername
  // TODO: 从后端获取更多用户信息
})

// 修改密码
const handleChangePassword = async () => {
  try {
    if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
      alert('新密码两次输入不一致')
      return
    }

    // TODO: 调用后端 API 修改密码
    showChangePasswordModal.value = false
  } catch (error) {
    console.error('Change password error:', error)
  }
}

// 注销账户
const handleDeleteAccount = async () => {
  try {
    // TODO: 调用后端 API 注销账户
    localStorage.clear()
    router.push('/login')
  } catch (error) {
    console.error('Delete account error:', error)
  }
}
</script>

<style scoped>
.account-page {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.account-container {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.page-title {
  font-size: 24px;
  margin-bottom: 2rem;
  color: #333;
}

.user-info-section,
.account-actions {
  margin-bottom: 2rem;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.info-item {
  padding: 1rem;
  background: #f5f5f5;
  border-radius: 8px;
}

.info-item label {
  color: #666;
  font-size: 14px;
}

.info-item .value {
  margin-top: 0.5rem;
  font-size: 16px;
  color: #333;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.action-button.danger {
  background-color: #dc3545 !important;
  color: white !important;
}

.modal-content {
  padding: 1.5rem;
}

.modal-content h3 {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.warning-text {
  color: #dc3545;
  margin-bottom: 1.5rem;
}
</style>
