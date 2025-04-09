<template>
  <button 
    class="bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 flex items-center justify-center"
  >
    <slot></slot>
  </button>
</template>

<script setup>
import { defineEmits } from 'vue'

// Emit the update-employee event when the button is clicked
const emit = defineEmits()

const handleClick = () => {
  // Emit the event to the parent
  emit('update-employee', 'new-employee-id') // Example employee id, replace with actual logic if needed
}
</script>

<style scoped>
</style>
