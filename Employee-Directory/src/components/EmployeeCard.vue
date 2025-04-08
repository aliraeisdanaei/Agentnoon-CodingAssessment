<template>
  <div v-if="employee" class="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-lg">
    <div class="flex justify-center mb-4">
      <img :src="employee.photo" alt="Employee Photo" class="w-32 h-32 rounded-full border-4 border-primary">
    </div>

    <h2 class="text-2xl font-semibold text-center mb-2">{{ employee.name }}</h2>
    <p class="text-center text-sm text-gray-500">{{ employee.job_title }}</p>

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

  <div v-else class="loading-screen">
    <div class="spinner"></div>
    <p>Loading employee data...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { fetchEmployeeData } from '../services/employeeService' // Adjust this import to match your file structure

// Define the props
const props = defineProps({
  employee_id: {
    type: String,
    required: true,
  },
})

// Reactive data
const employee = ref(null)
const error = ref(null)
const loading = ref(true)

// Fetch employee data based on the employee_id prop
onMounted(async () => {
  try {
    loading.value = true
    console.log('Fetching data for employee ID:', props.employee_id)
    employee.value = await fetchEmployeeData(props.employee_id) // Assuming this function fetches data from your API
    console.log(employee.value)
  } catch (err) {
    error.value = err.message || 'Failed to fetch employee data.'
  } finally {
    loading.value = false
  }
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
</style>
