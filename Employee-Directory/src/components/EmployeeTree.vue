<script setup>
// import { ref } from 'vue'
import EmployeeCard from './EmployeeCard.vue'
// import { useEmployeeStore } from '@/stores/employeeStore'
// const employeeStore = useEmployeeStore()

const props = defineProps({
  employeeShown: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="space-y-6">

    <div class="w-full flex items-center justify-center">
        <EmployeeCard :key="employeeShown.employee_id"
        :employeeShown="employeeShown" :parent-in-tree="employeeShown"></EmployeeCard>
    </div> 

    <div v-if="employeeShown.subordinates && employeeShown.subordinates.length" 
    class="flex flex-wrap gap-2 p-2 items-center justify-center">
      <div v-for="sub in employeeShown.subordinates" 
           :key="sub.employee_id"
           class="w-full sm:w-1/2 lg:w-1/5 xl:w-1/6">
        <!-- Ensure the EmployeeCard has a max-width and proper padding -->
        <div class="w-full p-2">
          <EmployeeCard :employeeShown="sub" :parent-in-tree="employeeShown"></EmployeeCard>
        </div>
      </div>
    </div>
  </div>
</template>
