<template>
  <div class="hero-background">
    <div class="star-field">
      <div class="small"></div>
      <div class="medium"></div>
      <div class="large"></div>
    </div>
    <div class="globe-container">
      <div class="globe"></div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  background: linear-gradient(180deg, rgb(13, 17, 54) 0%, rgb(58, 45, 113) 100%);
}

.star-field {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  animation: twinkle 2s infinite;
}

.star-field div {
  position: absolute;
  width: 2px;
  height: 2px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
}

.star-field .small {
  width: 1px;
  height: 1px;
  box-shadow: 
    10vw 10vh #fff,
    20vw 20vh #fff,
    30vw 30vh #fff,
    90vw 90vh #fff;
}

.star-field .medium {
  width: 2px;
  height: 2px;
  box-shadow: 
    15vw 15vh #fff,
    25vw 25vh #fff,
    35vw 35vh #fff,
    85vw 85vh #fff;
}

.star-field .large {
  width: 3px;
  height: 3px;
  box-shadow: 
    5vw 5vh #fff,
    45vw 45vh #fff,
    75vw 75vh #fff,
    95vw 95vh #fff;
}

.globe-container {
  position: absolute;
  width: 1000px;
  height: 1000px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.1;
}

.globe {
  position: absolute;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, 
    rgba(100, 200, 255, 0.1) 0%,
    rgba(100, 200, 255, 0) 70%);
  border-radius: 50%;
  animation: rotate 20s linear infinite;
}

/* 动画关键帧 */
@keyframes twinkle {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 0.4; }
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes titleGlow {
  0%, 100% { filter: brightness(1); }
  50% { filter: brightness(1.2); }
}

</style> 