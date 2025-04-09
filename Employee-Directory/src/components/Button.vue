<template>
  <button 
    class="bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 flex items-center justify-center"
    @click="handleClick"
    >
    <slot></slot>
  </button>
</template>

<script setup>
import { defineEmits } from 'vue'

const props = defineProps({
  updatedEmployee: {
    type: Object,
    required: true,
  },
})

const emitButton = defineEmits(['updateEmployeeButton'])
const handleClick = () => {
    console.log("Emitting in button", props.updatedEmployee)
    emitButton('updateEmployeeButton', props.updatedEmployee)
}
</script>

<style scoped>
</style>
