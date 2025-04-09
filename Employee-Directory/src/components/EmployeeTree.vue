<script setup>
import { defineEmits } from 'vue'
import EmployeeCard from './EmployeeCard.vue'

const props = defineProps({
  employeeShown: {
    type: Object,
    required: true
  }
})

const emitTree = defineEmits(['updateEmployeeTree'])
const handleUpdateEmployeeTree = (updatedEmployee) => {
  emitTree('updateEmployeeTree', updatedEmployee)
}
</script>

<template>
  <div class="space-y-6">

    <div class="w-full flex items-center justify-center">
        <EmployeeCard :employeeShown="props.employeeShown" :parent-in-tree="props.employeeShown"
            @updateEmployeeCard="handleUpdateEmployeeTree"
        ></EmployeeCard>
    </div> 

    <div v-if="props.employeeShown.subordinates && props.employeeShown.subordinates.length" 
    class="flex flex-wrap gap-2 p-2 items-center justify-center">
      <div v-for="sub in props.employeeShown.subordinates" 
           :key="sub.employee_id"
           class="w-full sm:w-1/2 lg:w-1/5 xl:w-1/6">
        <!-- Ensure the EmployeeCard has a max-width and proper padding -->
        <div class="w-full p-2">
          <EmployeeCard :employeeShown="sub" :parent-in-tree="props.employeeShown"
            @updateEmployeeCard="handleUpdateEmployeeTree"
          ></EmployeeCard>
        </div>
      </div>
    </div>
  </div>
</template>
