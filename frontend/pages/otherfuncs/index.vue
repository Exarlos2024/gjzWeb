<template>
  <DefaultLayout>
    <div class="word-tools-page">
      <div class="page-header">
        <h1>常用工具</h1>
        <p class="description">提供其他工具</p>
      </div>

      <div class="tools-grid">
        <nuxt-link to="/otherfuncs/links" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-link text-3xl" />
          </div>
          <h3>常用链接</h3>
          <p>访问常用的外部链接</p>
        </nuxt-link>

        <nuxt-link to="/otherfuncs/addressbook" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-book-open text-3xl" />
          </div>
          <h3>通讯录</h3>
          <p>查看和管理联系人信息</p>
        </nuxt-link>

        <nuxt-link to="/otherfuncs/about" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-information-circle text-3xl" />
          </div>
          <h3>关于我们</h3>
          <p>了解我们的背景和使命</p>
        </nuxt-link>

        <nuxt-link to="/otherfuncs/contact" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-phone text-3xl" />
          </div>
          <h3>联系我们</h3>
          <p>获取我们的联系信息</p>
        </nuxt-link>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import DefaultLayout from "~/components/layout/DefaultLayout.vue"
</script>

<style scoped>
.word-tools-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
  background: linear-gradient(135deg, #e0f7fa, #80deea);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.page-header {
  text-align: center;
  margin-bottom: 3rem;
}

.page-header h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.page-header .description {
  color: #666;
  font-size: 1.1rem;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

.tool-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  border: 1px solid #eee;
}

.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #2196F3;
}

.tool-icon {
  font-size: 2rem;
  color: #2196F3; /* Word工具使用蓝色主题 */
  margin-bottom: 1rem;
}

h3 {
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-size: 1.25rem;
}

p {
  color: #666;
  text-align: center;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .word-tools-page {
    padding: 1rem;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .tools-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style> 