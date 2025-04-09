<template>
  <div>
    <h1 v-if="employeeShown?.name">Employee Tree for {{ employeeShown.name }}</h1>
    <h1 v-else>Employee Tree</h1>

    <!-- Error Message -->
    <div v-if="error" class="error">
      <p>⚠️ Failed to load employee tree:</p>
      <pre>{{ error }}</pre>
    </div>

    <!-- Employee Tree -->
    <!-- <div v-else-if="root_employees && root_employees.length > 0"> -->
    <div v-else-if="employeeShown">
      <!-- {{employee_shown.employee_id }} -->
      <!-- <EmployeeCard :employee_id="employee_shown.employee_id"></EmployeeCard> -->
       <EmployeeTree :employeeShown="employeeShown" 
        @updateEmployeeTree="handleUpdateEmployee" 
       ></EmployeeTree>
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
// import EmployeeCard from './components/EmployeeCard.vue'
import EmployeeTree from './components/EmployeeTree.vue'
import { fetchEmployeeTree } from './services/employeeService' 
import { buildEmployeeTree } from './models/Employee'

// Variables to store employee data and errors
const root_employees = ref([])
const error = ref(null)
const loading = ref(true) 

let employeeShown = ref(null)

// Fetch employee tree on component mount
onMounted(async () => {
  try {
    loading.value = true
    const json = await fetchEmployeeTree() 
    root_employees.value = buildEmployeeTree(json)
    employeeShown.value = root_employees.value[0]
    console.log("Found the ceo: ", employeeShown.value)
  } catch (err) {
    console.log(err)
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    loading.value = false
  }
})

const handleUpdateEmployee = (updatedEmployee) => {
  console.log('Finally changing the employee at the app level', updatedEmployee)
  employeeShown.value = { ...updatedEmployee }
}

</script>

<style scoped>
</style>
