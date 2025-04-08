<template>
  <div v-if="employee" class="bg-slate-200 p-2 rounded-lg shadow-lg border-2 border-gray-300 max-w-xs sm:max-w-md md:max-w-lg mx-auto">
    <div class="flex justify-center mb-4">
      <img :src="employee.photo" alt="Employee Photo" class="w-20 h-20 rounded-full border-4 border-primary object-cover">
    </div>

    <h2 class="text-2xl font-semibold text-center mb-2 text-gray-800">{{ employee.name }}</h2>
    <p class="text-center text-sm text-gray-500">
      {{ employee.job_title }}
      </br>
      {{ employee.email }}
      </br>
      {{employee.employee_id }}
    </p>

    <p class="text-center text-sm text-gray-500">
      <div v-if="employee.manager_id" class="text-gray-700">
        <strong>Manager:</strong>
        {{ employee.manager_id }}
      </div>
    </p>

    <div class="grid gap-4 mt-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3">

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
import { ref, onMounted} from 'vue'
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
