<!--
 * @Author: Exarlos
 * @Date: 2024-12-07 18:19:32
 * @LastEditors: Exarlos
 * @LastEditTime: 2024-12-07 22:45:24
 * @Description: 世界上没有低级的法术,只有低级的法师!
-->
<template>
  <div class="layout-container">
    <TheNavbar />
    <main>
      <slot />
    </main>
    <TheFooter />
  </div>
</template>

<script setup>
import TheNavbar from "./TheNavbar.vue";
import TheFooter from "./TheFooter.vue";
</script>

<style scoped>
.layout-container {
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  /* background: linear-gradient(135deg, #4e54c8, #8f94fb) !important; */
  /* background: linear-gradient(135deg, #e0f7fa, #80deea, #26c6da); */
  background: linear-gradient(135deg, #a1c4fd, #c2e9fb);  
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

main {
  flex: 1;
  position: relative;
  padding: 0;
}

</style>
