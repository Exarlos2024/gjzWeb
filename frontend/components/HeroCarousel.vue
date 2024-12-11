<template>
  <div class="carousel-outer">
    <button class="nav-button prev" @click.stop="prevSlide">‹</button>
    <div class="carousel-container">
      <div class="carousel-wrapper" :style="{ transform: `translateX(-${currentTranslate}px)` }">
        <NuxtLink 
          v-for="(slide, index) in slides" 
          :key="index" 
          :to="slide.action"
          class="carousel-slide-link"
        >
          <div class="carousel-slide" :class="{ active: currentIndex === index }">
            <div class="slide-image-container">
              <img :src="slide.image" :alt="slide.title" class="slide-image">
              <div class="slide-content-overlay">
                <div class="button-group">
                  <button class="slide-button">{{ slide.buttonText }}</button>
                  <button class="learn-more">了解详情</button>
                </div>
                <div class="slide-content">
                  <h2 class="slide-title">{{ slide.title }}</h2>
                  <p class="slide-description">{{ slide.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
    <button class="nav-button next" @click.stop="nextSlide">›</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const slides = [
  {
    title: "Excel工具",
    description: "关于Excel的工具",
    buttonText: "了解更多",
    action: "/services",
    image: "/images/Excel.png"
  },
  {
    title: "Word公文工具",
    description: "提供方便的Word公文生成",
    buttonText: "立即预约",
    action: "/appointment",
    image: "/images/word.png"
  },
  {
    title: "信息化建设",
    description: "用技术解决问题",
    buttonText: "查看详情",
    action: "/health",
    image: "/images/ppt.png"
  }
]

const currentIndex = ref(0)
const currentTranslate = ref(0)
const slideWidth = ref(0)

const updateSlideWidth = () => {
  const container = document.querySelector('.carousel-container')
  if (container) {
    slideWidth.value = container.offsetWidth * 0.5 // 修改为容器的50%宽度
  }
}

const setSlide = (index) => {
  currentIndex.value = index
  currentTranslate.value = index * slideWidth.value
  updateActiveSlide()
}

const nextSlide = (e) => {
  if (e) e.preventDefault()
  if (currentIndex.value < slides.length - 1) {
    setSlide(currentIndex.value + 1)
  } else {
    setSlide(0)
  }
}

const prevSlide = (e) => {
  if (e) e.preventDefault()
  if (currentIndex.value > 0) {
    setSlide(currentIndex.value - 1)
  } else {
    setSlide(slides.length - 1)
  }
}

// 添加自动轮播
const autoPlayInterval = ref(null)

const startAutoPlay = () => {
  stopAutoPlay()
  autoPlayInterval.value = setInterval(() => {
    nextSlide()
  }, 5000) // 每5秒切换一次
}

const stopAutoPlay = () => {
  if (autoPlayInterval.value) {
    clearInterval(autoPlayInterval.value)
    autoPlayInterval.value = null
  }
}

// 添加鼠标悬停时暂停自动轮播的功能
const pauseAutoPlay = () => {
  stopAutoPlay()
}

const resumeAutoPlay = () => {
  startAutoPlay()
}

// 添加激活状态的处理
const updateActiveSlide = () => {
  const slides = document.querySelectorAll('.carousel-slide')
  slides.forEach((slide, index) => {
    if (index === currentIndex.value) {
      slide.classList.add('active')
    } else {
      slide.classList.remove('active')
    }
  })
}

onMounted(() => {
  updateSlideWidth()
  window.addEventListener('resize', updateSlideWidth)
  startAutoPlay()
  updateActiveSlide()
  
  // 添加鼠标悬停事件监听
  const container = document.querySelector('.carousel-container')
  if (container) {
    container.addEventListener('mouseenter', pauseAutoPlay)
    container.addEventListener('mouseleave', resumeAutoPlay)
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', updateSlideWidth)
  stopAutoPlay()
  
  // 移除鼠标悬停事件监听
  const container = document.querySelector('.carousel-container')
  if (container) {
    container.removeEventListener('mouseenter', pauseAutoPlay)
    container.removeEventListener('mouseleave', resumeAutoPlay)
  }
})
</script>

<style scoped>
.carousel-outer {
  position: relative;
  width: 100%;
  margin: 3rem auto; /* 增加与上方按钮的间距 */
  padding: 0 60px; /* 为导航按钮留出空间 */
  overflow: visible; /* 允许内容溢出以显示其他幻灯片 */
}

.carousel-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  overflow: visible; /* 允许显示相邻幻灯片 */
  background: transparent;
}

.carousel-wrapper {
  display: flex;
  transition: transform 0.5s ease-in-out;
  gap: 20px; /* 幻灯片之间的间距 */
}

.carousel-slide-link {
  text-decoration: none;
  min-width: calc(100% - 200px); /* 主幻灯片宽度，留出两侧空间 */
  cursor: pointer;
  transition: transform 0.3s ease;
}

.carousel-slide-link:hover {
  transform: translateY(-5px); /* 悬停时轻微上浮效果 */
}

.carousel-slide {
  position: relative;
  background: #fff;
  border-radius: 16px;
  overflow: hidden; /* 确保图片不会超出圆角边框 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transform: scale(0.8);
  transition: all 0.5s ease-in-out;
  opacity: 0.5;
  height: 400px; /* 设置卡片固定高度 */
}

.carousel-slide.active {
  transform: scale(1); /* 当前幻灯片正常大小 */
  opacity: 1; /* 当前幻灯片完全不透明 */
}

.nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: white;
  border: none;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  font-size: 24px;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10;
}

.nav-button:hover {
  background: #f8f9fa;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.prev {
  left: 0;
}

.next {
  right: 0;
}

.button-group {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
  margin-bottom: 1rem;
}

.slide-button, .learn-more {
  padding: 0.5rem 1rem;
  border-radius: 50px;
  border: none;
  font-weight: 500;
  font-size: 0.8rem;
  cursor: pointer;
  pointer-events: none; /* 防止按钮点击事件干扰整体链接 */
}

.slide-button {
  background: #1a73e8;
  color: white;
}

.learn-more {
  background: #e8f0fe;
  color: #1a73e8;
}

.slide-image-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slide-content-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.7));
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.slide-content {
  text-align: center;
  padding: 1rem 0;
}

.slide-title {
  color: #ffffff; /* 改为白色以便在深色背景上显示 */
  margin-bottom: 0.5rem;
}

.slide-description {
  color: #ffffff; /* 改为白色以便在深色背景上显示 */
  opacity: 0.9;
}

@media (max-width: 768px) {
  .carousel-outer {
    padding: 0 30px;
  }
  
  .carousel-slide {
    min-width: calc(100% - 100px);
  }
  
  .nav-button {
    width: 30px;
    height: 30px;
    font-size: 20px;
  }
}
</style> 