<template>
  <DefaultLayout>
    <div class="word-tools-page">
      <div class="page-header">
        <h1>Word 公文工具</h1>
        <p class="description">提供多种 Word 公文处理工具</p>
      </div>

      <div class="tools-grid">
        <nuxt-link to="/word/format" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-document-plus text-3xl" />
          </div>
          <h3>公文格式化工具</h3>
          <p>快速规范公文格式</p>
        </nuxt-link>

        <nuxt-link to="/word/open" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-folder-open text-3xl" />
          </div>
          <h3>打开公文</h3>
          <p>查看和编辑公文文件</p>
        </nuxt-link>

        <nuxt-link to="/word/templates" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-document-duplicate text-3xl" />
          </div>
          <h3>公文格式模板下载</h3>
          <p>下载标准公文模板</p>
        </nuxt-link>

        <nuxt-link to="/word/export-pdf" class="tool-card">
          <div class="tool-icon">
            <div class="i-heroicons-arrow-up-tray text-3xl" />
          </div>
          <h3>导出PDF</h3>
          <p>将公文转换为PDF格式</p>
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
  background-color: #fff;
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