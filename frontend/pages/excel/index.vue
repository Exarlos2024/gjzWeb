<template>
  <DefaultLayout>
    <div class="excel-tools-page">
      <div class="page-header">
        <h1>Excel 工具集</h1>
        <p class="description">提供多种 Excel 文件处理工具</p>
      </div>

      <div class="tools-grid">
        <nuxt-link to="/excel/duplicate" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-plus text-3xl" />
          </div>
          <h3>Excel查重工具</h3>
          <p>快速查找重复数据</p>
        </nuxt-link>

        <nuxt-link to="/excel/compare" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-folder-open text-3xl" />
          </div>
          <h3>Excel比对工具</h3>
          <p>对比Excel文件差异</p>
        </nuxt-link>

        <!-- 其他工具卡片 -->
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import DefaultLayout from "~/components/layout/DefaultLayout.vue"
</script>

<style scoped>
.excel-tools-page {
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
}

.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.tool-icon {
  font-size: 2rem;
  color: #4CAF50;
  margin-bottom: 1rem;
}

h3 {
  margin-bottom: 0.5rem;
}

p {
  color: #666;
  text-align: center;
}
</style> 