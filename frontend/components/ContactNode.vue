<template>
    <div class="contact-node" :style="{ paddingLeft: `${indent}px` }">
      <div class="contact-info">
        <span class="contact-name">{{ contact.name }} ({{ contact.position }})</span>
        <span class="contact-details">科室: {{ contact.department }}</span>
        <span class="contact-details">级别: {{ contact.level }}</span>
        <span class="contact-details">办公室: {{ contact.office }}</span>
        <span class="contact-details">手机: {{ contact.mobile_phone }}</span>
        <span class="contact-details">办公电话: {{ contact.office_phone }}</span>
        <span v-if="contact.level !== '局长' && contact.level !== '科员'" class="contact-details">领导: {{ contact.leader }}</span>
      </div>
      <div v-if="contact.children && contact.children.length" class="children">
        <div class="children-container">
          <ContactNode
            v-for="child in contact.children"
            :key="child.id"
            :contact="child"
            :indent="indent + 20"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  const props = defineProps({
    contact: {
      type: Object,
      required: true
    },
    indent: {
      type: Number,
      default: 0
    }
  })
  </script>
  
  <style scoped>
  .contact-node {
    margin: 10px 0;
    padding: 15px;
    background-color: #ffffff; /* 背景颜色 */
    border-radius: 8px; /* 圆角 */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* 阴影效果 */
    transition: box-shadow 0.3s; /* 添加过渡效果 */
  }
  
  .contact-node:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* 悬停时的阴影效果 */
  }
  
  .contact-info {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
  }
  
  .contact-name {
    font-weight: bold;
    margin-right: 10px;
    color: #333; /* 名字颜色 */
    font-size: 1.1rem; /* 字体大小 */
  }
  
  .contact-details {
    margin-right: 15px;
    color: #666; /* 细节颜色 */
    font-size: 0.9rem; /* 字体大小 */
  }
  
  .children {
    margin-top: 10px; /* 子节点的顶部间距 */
  }
  
  .children-container {
    margin-left: 20px; /* 子节点的左侧间距 */
  }
  </style>