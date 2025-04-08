<template>
  <div v-if="employee" class="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-lg">
    <div class="flex justify-center mb-4">
      <img :src="employee.photo" alt="Employee Photo" class="w-32 h-32 rounded-full border-4 border-primary">
    </div>

    <h2 class="text-2xl font-semibold text-center mb-2">{{ employee.name }}</h2>
    <p class="text-center text-sm text-gray-500">{{ employee.job_title }}</p>

    <!-- Double Column Layout -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
      <div class="text-gray-700">
        <strong>Email:</strong>
        <p>{{ employee.email }}</p>
      </div>

      <div class="text-gray-700">
        <strong>Department:</strong>
        <p>{{ employee.department }}</p>
      </div>

      <div class="text-gray-700">
        <strong>Location:</strong>
        <p>{{ employee.location }}</p>
      </div>

      <div class="text-gray-700">
        <strong>Salary:</strong>
        <p>{{ formatCurrency(employee.salary) }}</p>
      </div>

      <div class="text-gray-700">
        <strong>Performance:</strong>
        <p>{{ employee.performance }}</p>
      </div>

      <div class="text-gray-700">
        <strong>Start Date:</strong>
        <p>{{ formatDate(employee.start_date) }}</p>
      </div>

      <div v-if="employee.manager_id" class="text-gray-700">
        <strong>Manager:</strong>
        <p>{{ employee.manager_id }}</p>
      </div>
    </div>

    <div v-if="error" class="mt-6 text-center text-red-500 p-4 bg-red-100 rounded-md">
      <strong>Error: </strong>{{ error }}
    </div>
  </div>

  <!-- Loading State -->
  <div v-else-if="loading" class="text-center">Loading...</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchEmployeeData } from '../services/employeeService' // Import the fetch function

const employee = ref(null)
const error = ref(null)
const loading = ref(true)

const employeeId = 'p_DrnEHzsrxaHOPnwwNDBwy' // Replace with dynamic ID

// Fetch function to get employee data from API
async function getEmployeeData(employeeId) {
  try {
    loading.value = true
    employee.value = await fetchEmployeeData(employeeId) // Use the imported fetch function
  } catch (err) {
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    loading.value = false
  }
}

// Call the API when the component is mounted
onMounted(() => {
  getEmployeeData(employeeId)
})

// Helper function to format salary to currency
function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(amount)
}

// Helper function to format the start date
function formatDate(dateStr) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString(undefined, options)
}
</script>

<style scoped>
/* Custom styles can go here if needed */
</style>
