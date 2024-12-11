<template>
  <DefaultLayout>
    <div class="links-container">
      <h1 class="page-title">常用链接</h1>
      
      <div class="categories">
        <div v-for="category in usefulLinks" :key="category.category" class="category">
          <h2 class="category-title">{{ category.category }}</h2>
          <div class="links-grid">
            <UCard
              v-for="link in category.links"
              :key="link.title"
              class="link-card"
            >
              <div class="link-content">
                <UIcon :name="link.icon" class="link-icon"/>
                <div class="link-info">
                  <h3 class="link-title">
                    <a :href="link.url" target="_blank" rel="noopener noreferrer">
                      {{ link.title }}
                    </a>
                  </h3>
                  <p class="link-description">{{ link.description }}</p>
                </div>
              </div>
            </UCard>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { usefulLinks } from '~/constants/links';
import DefaultLayout from '~/components/layout/DefaultLayout.vue';
</script>

<style scoped>
.links-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.page-title {
  font-size: 2rem;
  color: #24292f;
  margin-bottom: 2rem;
  text-align: center;
}

.category {
  margin-bottom: 3rem;
}

.category-title {
  font-size: 1.5rem;
  color: #24292f;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #e1e4e8;
}

.links-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.link-card {
  transition: transform 0.2s, box-shadow 0.2s;
}

.link-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.link-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.link-icon {
  font-size: 2rem;
  color: #0969da;
}

.link-info {
  flex: 1;
}

.link-title {
  margin: 0;
  font-size: 1.1rem;
}

.link-title a {
  color: #0969da;
  text-decoration: none;
}

.link-title a:hover {
  text-decoration: underline;
}

.link-description {
  margin: 0.5rem 0 0;
  color: #57606a;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .links-grid {
    grid-template-columns: 1fr;
  }
}
</style> 

 