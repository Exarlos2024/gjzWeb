<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 12:20:35
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-08 12:03:31
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <section class="hero-section">

    <HeroBackground />
    <div class="hero-container">
      <h1 class="hero-title">
        大连市甘井子区卫生健康局<br>
        数据中心
      </h1>
      <p class="hero-description">
        Think different
      </p>
      
      <!-- 引入 CTA 按钮组件 -->
      <HeroCTA />
      <!-- 添加轮播图组件 -->
      <HeroCarousel />
    </div>
  </section>
</template>

<script setup>
import HeroBackground from '~/components/HeroBackground.vue'
import HeroCTA from '~/components/HeroCTA.vue'
import HeroCarousel from '~/components/HeroCarousel.vue'
</script>

<style scoped>
.hero-section {
  position: relative;
  padding: 80px 16px;
  min-height: calc(100vh - 64px);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}

/* 内容样式 */
.hero-container {
  position: relative;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
  z-index: 1;
}

.hero-title {
  font-size: 72px;
  line-height: 1.1;
  font-weight: 600;
  letter-spacing: -0.025em;
  color: #ffffff;
  margin-bottom: 24px;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  background: linear-gradient(120deg, #fff, #88ccff);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: titleGlow 3s ease-in-out infinite;
}

.hero-description {
  font-size: 24px;
  line-height: 1.5;
  color: #7d8590;
  margin-bottom: 32px;
  max-width: 680px;
  margin-left: auto;
  margin-right: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hero-title {
    font-size: 48px;
  }

  .hero-description {
    font-size: 20px;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 32px;
  }

  .hero-description {
    font-size: 18px;
  }
}
</style> 