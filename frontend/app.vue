<template>
  <div id="app">
    <header class="site-header">
      <h1>教學範例計帳網頁 </h1>
      <h2>podName: {{ config.public.POD_NAME }}</h2>
      <h2>POD_NAMESPACE: {{ config.public.POD_NAMESPACE }}</h2>
      <h2>NodeName: {{ config.public.NODE_NAME }}</h2>
      <h2>NodeIP: {{ config.public.NODE_IP }}</h2>
    </header>

    <!-- Nuxt3 會根據路由載入各個頁面 -->
    <NuxtPage />

    <footer class="site-footer">
      <p>&copy; 2025 GDG on Campus NCU</p>
    </footer>
  </div>
</template>

<script setup>
// 這裡可以加入全域性的邏輯或引入共用組件
const config = useRuntimeConfig()
</script>

<style scoped>
/* 全域樣式，可根據需求調整 */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.site-header,
.site-footer {
  background-color: #f4f4f4;
  padding: 1rem;
  text-align: center;
}

.site-header {
  border-bottom: 1px solid #ddd;
}

.site-footer {
  border-top: 1px solid #ddd;
  margin-top: auto;
}
</style>
