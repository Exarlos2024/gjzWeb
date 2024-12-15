<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 23:00:00
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-07 23:00:00
 * @Description: 投诉管理系统页面
-->

<template>
    <DefaultLayout>
      <div class="about-container">
        <h1>投诉管理系统</h1>
        <!-- 文件上传区域 -->
        <div class="upload-area" @dragover.prevent @drop.prevent="handleDrop">
          <input type="file" multiple @change="handleFileUpload" accept=".doc,.docx" />
          <p>拖动文件到这里或点击选择文件</p>
        </div>

        <!-- 展示表格数据 -->
        <div v-if="tableData.length">
          <h2>表格数据</h2>
          <div v-for="(data, index) in tableData" :key="index">
            <h3>{{ data.file_name }}</h3>
            <table>
              <tr v-for="(row, rowIndex) in data.table_data" :key="rowIndex">
                <td v-for="(cell, cellIndex) in row" :key="cellIndex">{{ cell }}</td>
              </tr>
            </table>
          </div>
        </div>

        <nuxt-link to="/" class="back-home-button">回到主页</nuxt-link>
      </div>
    </DefaultLayout>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import DefaultLayout from "~/components/layout/DefaultLayout.vue";

  const files = ref([]); // 存储上传的文件
  const tableData = ref([]); // 存储表格数据

  const handleFileUpload = async (event) => {
    const selectedFiles = Array.from(event.target.files);
    files.value.push(...selectedFiles);
    await uploadFiles(selectedFiles);
  };

  const handleDrop = (event) => {
    const droppedFiles = Array.from(event.dataTransfer.files);
    files.value.push(...droppedFiles);
    uploadFiles(droppedFiles);
  };

  const uploadFiles = async (files) => {
    const formData = new FormData();
    files.forEach(file => {
      formData.append('files', file);
    });

    // 获取 Token
    const token = localStorage.getItem('token'); // 假设您将 Token 存储在 localStorage 中

    try {
      const response = await fetch('http://localhost:8000/api/upload/', {
        method: 'POST',
        body: formData,
        headers: {
          'Authorization': `Token ${token}` // 添加身份验证头
        }
      });

      if (response.ok) {
        const data = await response.json();
        console.log('上传成功:', data);
        tableData.value = data.table_data; // 更新表格数据
      } else {
        console.error('上传失败:', response.statusText);
      }
    } catch (error) {
      console.error('上传错误:', error);
    }
  };
  </script>
  
  <style scoped>
  .about-container {
    width: 100%;
    height: 100vh;
    margin: 0;
    padding: 2rem;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  p {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 2rem;
  }
  
  .quote-author {
    display: block;
    text-align: right;
    margin-right: 20px;
  }
  
  .back-home-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #24292f;
    color: white;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.3s, transform 0.3s;
  }
  
  .back-home-button:hover {
    background-color: #3b3f45;
    transform: translateY(-2px);
  }
  
  .upload-area {
    border: 2px dashed #ccc;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    margin: 20px 0;
    cursor: pointer;
  }
  
  .upload-area:hover {
    background-color: #f0f0f0;
  }
  </style>
  