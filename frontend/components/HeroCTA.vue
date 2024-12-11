<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 12:24:36
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 13:25:37
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <div class="hero-cta">
    <UButton
      size="xl"
      color="white"
      class="start-button"
      label="开始使用"
      @click="startUsing"
    />
    <UButton
      size="xl"
      variant="ghost"
      class="learn-more-button"
      label="了解更多"
      @click="goToTest"
    />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToTest() {
  router.push('/test')
}

function startUsing() {
  // 处理“开始使用”按钮的逻辑
  router.push('/login')
}
</script>

<style scoped>
.hero-cta {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-top: 40px;
}

.start-button {
  background: #fff !important;
  color: #0d1117 !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  padding: 12px 32px !important;
  font-size: 20px !important;
  font-weight: 600 !important;
  transition: all 0.2s !important;
}

.start-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.learn-more-button {
  color: #fff !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  padding: 12px 32px !important;
  font-size: 20px !important;
  font-weight: 600 !important;
  transition: all 0.2s !important;
}

.learn-more-button:hover {
  border-color: #fff !important;
  transform: translateY(-2px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hero-cta {
    flex-direction: column;
    padding: 0 20px;
  }
}
</style> 