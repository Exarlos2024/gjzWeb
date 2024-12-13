<template>
  <div class="contact-node">
    <div class="contact-info">
      <h3>{{ contact.name }} ({{ contact.position }})</h3>
      <p>办公室: {{ contact.office }}</p>
      <p>电话: {{ contact.office_phone }}</p>
      <p>手机: {{ contact.handphone }}</p>
    </div>
    <div v-if="contact.children && contact.children.length" class="children">
      <div class="children-container">
        <ContactNode
          v-for="child in contact.children"
          :key="child.id"
          :contact="child"
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
  }
})
</script>

<style scoped>
.contact-node {
  margin: 10px 0;
}

.contact-info {
  text-align: left;
  padding-left: 20px;
}

.contact-info h3 {
  margin: 0;
  font-size: 1.5rem;
  color: #333;
}

.contact-info p {
  margin: 0.2rem 0;
  color: #666;
}

.children-container {
  padding-left: 60px;
}
</style>