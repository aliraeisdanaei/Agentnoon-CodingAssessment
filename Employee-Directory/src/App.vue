<template>
  <div>
    <h1>Employee Tree</h1>

    <!-- Error Message -->
    <div v-if="error" class="error">
      <p>⚠️ Failed to load employee tree:</p>
      <pre>{{ error }}</pre>
    </div>

    <!-- Employee Tree -->
    <div v-else-if="root_employees && root_employees.length > 0">
      <p>
        This should include the employee id of the CEO:
        {{ root_employees[0].employee_id }}
      </p>
    </div>

    <!-- Loading Screen -->
    <div v-else class="loading-screen">
      <div class="spinner"></div>
      <p>Loading employee tree...</p>
    </div>

    <!-- Employee Card Component -->
    <EmployeeCard></EmployeeCard>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EmployeeCard from './components/EmployeeCard.vue'
import { fetchEmployeeTree } from './services/employeeService' // Importing the fetch function from the service file
import { buildEmployeeTree } from './models/Employee'

// Variables to store employee data and errors
const root_employees = ref([])
const error = ref(null)
const loading = ref(true) // Add loading state to show while fetching

// Fetch employee tree on component mount
onMounted(async () => {
  try {
    loading.value = true
    const json = await fetchEmployeeTree() 
    root_employees.value = buildEmployeeTree(json)
  } catch (err) {
    console.log(err)
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Loading screen styles */
.loading-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 200px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #42b983;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 0.8s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Error message styles */
.error {
  color: #b00020;
  background: #ffe6e6;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}
</style>
