<template>
  <DefaultLayout>
    <div class="excel-duplicate-page">
      <div class="page-header">
        <h1>Excel 查重工具</h1>
        <p class="description">上传 Excel 文件，快速查找重复数据</p>
      </div>

      <div class="main-content">
        <!-- 步骤 1: 文件上传区域 -->
        <div class="upload-section" v-if="!hasFile">
          <div 
            class="upload-box" 
            @click="triggerFileInput" 
            @drop.prevent="handleDrop" 
            @dragover.prevent
            @dragenter.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            :class="{ 'dragging': isDragging }"
          >
            <div class="upload-icon">
              <div class="i-heroicons-cloud-arrow-up-20-solid text-3xl" />
            </div>
            <p>点击或拖拽 Excel 文件到此处</p>
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

        <!-- 步骤 2&3: 文件信息展示 -->
        <div v-if="hasFile" class="file-info-card">
          <div class="file-info-header">
            <div class="file-name">
              <div class="i-heroicons-document-20-solid" />
              <span>{{ fileInfo.name }}</span>
            </div>
            <UButton
              size="sm"
              class="change-file-btn"
              @click="resetFile"
            >
              更换文件
            </UButton>
          </div>
          <div class="file-stats">
            <div class="stat-item">
              <span class="stat-label">总行数：</span>
              <span class="stat-value">{{ fileInfo.rows }}</span>
            </div>
            <div class="stat-item">
              <span class="stat-label">总列数：</span>
              <span class="stat-value">{{ fileInfo.columns }}</span>
            </div>
          </div>
        </div>

        <!-- 步骤 4&5: 列选择区域 -->
        <div v-if="hasFile" class="columns-section">
          <h3>选择要查重的列</h3>
          <div class="columns-grid">
            <div 
              v-for="col in columns" 
              :key="col"
              class="column-item"
              :class="{ selected: selectedColumns.includes(col) }"
              @click="toggleColumn(col)"
            >
              <div class="checkbox">
                <div v-if="selectedColumns.includes(col)" class="i-heroicons-check-20-solid" />
              </div>
              <span>{{ col }}</span>
            </div>
          </div>

          <!-- 已选择列的展示 -->
          <div v-if="selectedColumns.length" class="selected-columns">
            <h4>已选择：</h4>
            <div class="selected-tags">
              <div v-for="col in selectedColumns" :key="col" class="selected-tag">
                {{ col }}
                <span class="remove-tag" @click.stop="removeColumn(col)">×</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 步骤 6: 开始查重按钮 -->
        <div v-if="hasFile" class="action-section">
          <UButton
            class="check-button"
            :disabled="!canStartCheck"
            :loading="isChecking"
            @click="startCheck"
          >
            {{ isChecking ? '查重中...' : '开始查重' }}
          </UButton>
        </div>

        <!-- 步骤 7&8: 结果展示区域 -->
        <div v-if="showResults" class="results-section">
          <div class="results-card">
            <h3>查重结果</h3>
            <div class="results-stats">
              <div class="stat-box">
                <span class="stat-number">{{ duplicateGroups }}</span>
                <span class="stat-label">重复组数</span>
              </div>
              <div class="stat-box">
                <span class="stat-number">{{ duplicateRows }}</span>
                <span class="stat-label">重复记录数</span>
              </div>
            </div>
            <UButton
              class="download-button"
              :disabled="duplicateRows === 0"
              @click="downloadResults"
            >
              <div class="i-heroicons-arrow-down-tray-20-solid mr-2" />
              下载查重结果
            </UButton>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import DefaultLayout from "~/components/layout/DefaultLayout.vue"

// 状态变量
const fileInput = ref(null)
const hasFile = ref(false)
const isDragging = ref(false)
const isChecking = ref(false)
const columns = ref([])
const selectedColumns = ref([])
const fileInfo = ref(null)
const showResults = ref(false)
const duplicateGroups = ref(0)
const duplicateRows = ref(0)

// 计算属性：是否可以开始查重
const canStartCheck = computed(() => {
  return hasFile.value && selectedColumns.value.length > 0
})

// 触发文件选择
const triggerFileInput = () => {
  fileInput.value.click()
}

// 处理文件选择
const handleFileChange = async (event) => {
  const file = event.target.files[0]
  if (file) {
    try {
      const formData = new FormData()
      formData.append('file', file)
      
      const token = localStorage.getItem('token')
      const response = await fetch('http://localhost:8000/api/excel/analyze/', {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`
        },
        body: formData
      })
      
      const data = await response.json()
      
      fileInfo.value = {
        name: file.name,
        rows: data.rows,
        columns: data.columns,
        fileId: data.fileId
      }
      
      columns.value = data.headers
      hasFile.value = true
      
    } catch (error) {
      console.error('上传文件失败:', error)
      // TODO: 显示错误提示
    }
  }
}

// 处理文件拖放
const handleDrop = async (event) => {
  isDragging.value = false
  const file = event.dataTransfer.files[0]
  if (file && (file.name.endsWith('.xlsx') || file.name.endsWith('.xls'))) {
    const input = fileInput.value
    input.files = event.dataTransfer.files
    handleFileChange({ target: input })
  }
}

// 重置文件
const resetFile = () => {
  hasFile.value = false
  fileInfo.value = null
  columns.value = []
  selectedColumns.value = []
  showResults.value = false
  fileInput.value.value = ''
}

// 切换列选择
const toggleColumn = (col) => {
  const index = selectedColumns.value.indexOf(col)
  if (index === -1) {
    selectedColumns.value.push(col)
  } else {
    selectedColumns.value.splice(index, 1)
  }
}

// 移除已选择的列
const removeColumn = (col) => {
  const index = selectedColumns.value.indexOf(col)
  if (index !== -1) {
    selectedColumns.value.splice(index, 1)
  }
}

// 开始查重
const startCheck = async () => {
  if (!canStartCheck.value) return
  
  isChecking.value = true
  try {
    const token = localStorage.getItem('token') // 获取 Token
    const response = await fetch('http://localhost:8000/api/excel/check-duplicates/', {
      method: 'POST',
      headers: {
        'Authorization': `Token ${token}`, // 添加 Token 到请求头
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fileId: fileInfo.value.fileId,
        columns: selectedColumns.value
      })
    })
    
    const results = await response.json()
    if (!response.ok) {
      throw new Error(results.error || '查重失败')
    }
    duplicateGroups.value = results.groupCount
    duplicateRows.value = results.rowCount
    showResults.value = true
    
  } catch (error) {
    console.error('查重失败:', error)
    // TODO: 显示错误提示
  } finally {
    isChecking.value = false
  }
}

// 下载结果
const downloadResults = async () => {
  try {
    const token = localStorage.getItem('token') // 获取 Token
    window.location.href = `http://localhost:8000/api/excel/download-results?fileId=${fileInfo.value.fileId}` // 添加 Token 到请求 URL
  } catch (error) {
    console.error('下载失败:', error)
  }
}
</script>

<style scoped>
.excel-duplicate-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
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

/* 上传区域样式 */
.upload-box {
  border: 2px dashed #ddd;
  border-radius: 12px;
  padding: 3rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #f8f9fa;
}

.upload-box.dragging {
  border-color: #4CAF50;
  background-color: rgba(76, 175, 80, 0.05);
}

.upload-box:hover {
  border-color: #4CAF50;
  background-color: rgba(76, 175, 80, 0.05);
}

/* 文件信息卡片样式 */
.file-info-card {
  background-color: #fff;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.file-info-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.file-name {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

.file-stats {
  display: flex;
  gap: 2rem;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* 列选择区域样式 */
.columns-section {
  background-color: #fff;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.columns-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.column-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: 8px;
  border: 1px solid #ddd;
  cursor: pointer;
  transition: all 0.2s ease;
}

.column-item:hover {
  border-color: #4CAF50;
  background-color: rgba(76, 175, 80, 0.05);
}

.column-item.selected {
  background-color: #4CAF50;
  color: white;
  border-color: #4CAF50;
}

.checkbox {
  width: 20px;
  height: 20px;
  border: 2px solid currentColor;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 已选择标签样式 */
.selected-columns {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #eee;
}

.selected-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 0.75rem;
}

.selected-tag {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border-radius: 6px;
  font-size: 0.9rem;
}

.remove-tag {
  cursor: pointer;
  font-weight: bold;
  opacity: 0.8;
  transition: opacity 0.2s ease;
}

.remove-tag:hover {
  opacity: 1;
}

/* 操作按钮样式 */
.action-section {
  text-align: center;
  margin: 2rem 0;
}

.check-button {
  padding: 0.75rem 2rem !important;
  font-size: 1.1rem !important;
  background-color: #4CAF50 !important;
  color: white !important;
}

/* 结果展示区域样式 */
.results-card {
  background-color: #fff;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.results-stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin: 2rem 0;
}

.stat-box {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 2.5rem;
  font-weight: 600;
  color: #4CAF50;
  margin-bottom: 0.5rem;
}

.stat-label {
  color: #666;
}

.download-button {
  width: 100%;
  padding: 0.75rem !important;
  background-color: #2196F3 !important;
  color: white !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

@media (max-width: 768px) {
  .excel-duplicate-page {
    padding: 1rem;
  }

  .page-header h1 {
    font-size: 2rem;
  }

  .columns-grid {
    grid-template-columns: 1fr;
  }

  .results-stats {
    flex-direction: column;
    gap: 1.5rem;
  }
}
</style> 