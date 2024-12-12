<template>
  <DefaultLayout>
    <div class="excel-duplicate-page">
      <div class="page-header">
        <h1>Excel 查重工具</h1>
        <p class="description">上传 Excel 文件，快速查找重复数据</p>
      </div>

      <div class="main-content">
        <!-- 文件上传区域 -->
        <div class="upload-section">
          <div class="upload-box" @click="triggerFileInput" @drop.prevent="handleDrop" @dragover.prevent>
            <div class="upload-icon">
              <div class="i-heroicons-cloud-arrow-up-20-solid text-3xl" />
            </div>
            <p>点击或拖拽文件到此处上传</p>
            <p class="file-hint">支持 .xlsx, .xls 格式</p>
            <input
              type="file"
              ref="fileInput"
              class="hidden"
              accept=".xlsx,.xls"
              @change="handleFileChange"
            />
          </div>
        </div>

        <!-- 设置区域 -->
        <div class="settings-section">
          <h2>查重设置</h2>
          <div class="settings-grid">
            <div class="setting-item">
              <label>查重列</label>
              <select v-model="selectedColumns" multiple>
                <option v-for="col in columns" :key="col" :value="col">
                  {{ col }}
                </option>
              </select>
            </div>
            <div class="setting-item">
              <label>查重方式</label>
              <select v-model="duplicateType">
                <option value="exact">完全匹配</option>
                <option value="partial">部分匹配</option>
              </select>
            </div>
          </div>
          <UButton
            class="start-button"
            :disabled="!hasFile"
            @click="startCheck"
          >
            开始查重
          </UButton>
        </div>

        <!-- 结果展示区域 -->
        <div v-if="showResults" class="results-section">
          <h2>查重结果</h2>
          <div class="results-table">
            <!-- 这里放结果表格 -->
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref } from 'vue'
import DefaultLayout from "~/components/layout/DefaultLayout.vue"

// 状态变量
const fileInput = ref(null)
const hasFile = ref(false)
const columns = ref([])
const selectedColumns = ref([])
const duplicateType = ref('exact')
const showResults = ref(false)

// 触发文件选择
const triggerFileInput = () => {
  fileInput.value.click()
}

// 处理文件选择
const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    hasFile.value = true
    // TODO: 处理文件上传
  }
}

// 处理文件拖放
const handleDrop = (event) => {
  const file = event.dataTransfer.files[0]
  if (file && (file.name.endsWith('.xlsx') || file.name.endsWith('.xls'))) {
    hasFile.value = true
    // TODO: 处理文件上传
  }
}

// 开始查重
const startCheck = async () => {
  try {
    // TODO: 实现查重逻辑
    showResults.value = true
  } catch (error) {
    console.error('查重出错:', error)
  }
}
</script>

<style scoped>
.excel-duplicate-page {
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
  font-size: 2.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.description {
  color: #666;
  font-size: 1.1rem;
}

.main-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.upload-section {
  margin-bottom: 2rem;
}

.upload-box {
  border: 2px dashed #ddd;
  border-radius: 8px;
  padding: 3rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-box:hover {
  border-color: #4CAF50;
  background-color: rgba(76, 175, 80, 0.05);
}

.upload-icon {
  font-size: 3rem;
  color: #4CAF50;
  margin-bottom: 1rem;
}

.file-hint {
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.settings-section {
  background-color: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.setting-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.setting-item label {
  font-weight: 500;
  color: #2c3e50;
}

.setting-item select {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
}

.start-button {
  width: 100%;
  margin-top: 1.5rem;
  padding: 0.75rem !important;
  background-color: #4CAF50 !important;
  color: white !important;
  font-weight: 500 !important;
  transition: all 0.3s ease !important;
}

.start-button:hover {
  background-color: #45a049 !important;
  transform: translateY(-1px);
}

.start-button:disabled {
  background-color: #cccccc !important;
  cursor: not-allowed;
}

.results-section {
  margin-top: 2rem;
  padding: 2rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.hidden {
  display: none;
}

@media (max-width: 768px) {
  .excel-duplicate-page {
    padding: 1rem;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .settings-grid {
    grid-template-columns: 1fr;
  }
}
</style> 