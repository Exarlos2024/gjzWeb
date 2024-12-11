<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 22:44:50
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-07 23:24:23
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <footer class="site-footer">
    <div class="footer-content">
      <p>版权所有 © 艾克萨罗斯 2024</p>
      <div class="footer-links">
        <a href="https://github.com/" target="_blank">GitHub</a>
        <span class="divider">|</span>
        <a href="/about">关于我们</a>
        <span class="divider">|</span>
        <a href="/contact">联系我们</a>
        <span class="divider">|</span>
        <a href="#" @click.prevent="showQRCode = true" class="wechat-link">
          <i class="fab fa-weixin"></i>
        </a>
      </div>
    </div>

    <div v-if="showQRCode" class="qr-modal" @click="showQRCode = false">
      <div class="qr-content" @click.stop>
        <img src="../../images/wechat.jpg" alt="微信二维码" class="qr-image">
        <button class="close-button" @click="showQRCode = false">&times;</button>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue';

const showQRCode = ref(false);
</script>

<style scoped>
.site-footer {
  background-color: #24292f;
  color: #8b949e;
  text-align: center;
  padding: 2rem 0;
  position: relative;
  z-index: 2;
  margin-top: auto;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

.footer-links {
  margin-top: 0;
  display: flex;
  align-items: center;
}

.footer-links a {
  color: #58a6ff;
  text-decoration: none;
  transition: color 0.3s ease;
  font-size: 0.9rem;
}

.footer-links a:hover {
  color: #79c0ff;
}

.divider {
  color: #8b949e;
  margin: 0 1rem;
}

p {
  margin: 0;
  font-size: 0.9rem;
}

.qr-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.qr-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  position: relative;
  width: 300px;
  margin: auto;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.qr-image {
  width: 100%;
  height: auto;
  display: block;
}

.close-button {
  position: absolute;
  top: -15px;
  right: -15px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: none;
  background: #24292f;
  color: white;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.close-button:hover {
  background: #444;
}
</style> 