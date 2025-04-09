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
    <div v-else-if="employeeStore.employeeShown">
      <!-- {{employeeShown.employee_id }} -->
      <!-- <EmployeeCard :employee_id="employeeShown.employee_id"></EmployeeCard> -->
       <EmployeeTree :employeeShown="employeeStore.employeeShown"></EmployeeTree>
       <!-- <EmployeeTree></EmployeeTree> -->
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
import EmployeeTree from './components/EmployeeTree.vue'
import { fetchEmployeeTree } from './services/employeeService' 
import { buildEmployeeTree } from './models/Employee'
import { useEmployeeStore } from './stores/employeeStore'

const error = ref(null)
const loading = ref(true) 



const employeeStore = useEmployeeStore()
const employeeShown = employeeStore.employeeShown

// Fetch employee tree on component mount
onMounted(async () => {
  try {
    loading.value = true
    const json = await fetchEmployeeTree() 
    const root_employees = buildEmployeeTree(json)
    const ceo = root_employees[0]
    employeeStore.setEmployee(ceo)
    console.log("Found the ceo: ", employeeStore.employeeShown)
  } catch (err) {
    console.log(err)
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    console.log("setting loading to false")
    loading.value = false
  }
})
</script>

<style scoped>
</style>
