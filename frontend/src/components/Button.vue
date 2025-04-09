<template>
  <button 
    class="m-5 bg-blue-500 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50 flex items-center justify-center"
    @click="handleClick"
    >
    <slot></slot>
  </button>
</template>

<script setup>
import { useEmployeeStore } from '@/stores/employeeStore'

const props = defineProps({
  updatedEmployee: {
    type: Object,
    required: true,
  },
})

const employeeStore = useEmployeeStore()

const handleClick = () => {
  console.log('Setting the employee shown to', props.updatedEmployee)
  employeeStore.setEmployee(props.updatedEmployee)
}
</script>

<style scoped>
</style>
