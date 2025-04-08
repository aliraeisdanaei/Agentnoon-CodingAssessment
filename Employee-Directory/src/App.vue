<template>
  <div>
    <h1>Employee Tree</h1>

    <!-- Error Message -->
    <div v-if="error" class="error">
      <p>⚠️ Failed to load employee tree:</p>
      <pre>{{ error }}</pre>
    </div>

    <!-- Employee Tree -->
    <!-- <div v-else-if="root_employees && root_employees.length > 0"> -->
    <div v-else-if="employee_shown">
      {{employee_shown.employee_id }}
      <EmployeeCard :employee_id="employee_shown.employee_id"></EmployeeCard>
    </div>

    <!-- Loading Screen -->
    <div v-else class="loading-screen">
      <div class="spinner"></div>
      <p>Loading employee tree...</p>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EmployeeCard from './components/EmployeeCard.vue'
import { fetchEmployeeTree } from './services/employeeService' 
import { buildEmployeeTree } from './models/Employee'

// Variables to store employee data and errors
const root_employees = ref([])
const error = ref(null)
const loading = ref(true) 

let employee_shown = ref(null)

// Fetch employee tree on component mount
onMounted(async () => {
  try {
    loading.value = true
    const json = await fetchEmployeeTree() 
    root_employees.value = buildEmployeeTree(json)
    employee_shown = root_employees.value[0]
    console.log("Found the ceo: ", employee_shown)
  } catch (err) {
    console.log(err)
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
</style>
