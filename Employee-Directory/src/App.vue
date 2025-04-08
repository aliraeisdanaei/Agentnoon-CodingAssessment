<template>
  <div>
    <h1>Employee Tree</h1>

    <div v-if="error" class="error">
      <p>⚠️ Failed to load employee tree:</p>
      <pre>{{ error }}</pre>
    </div>

    <div v-else-if="root_employees && root_employees.length > 0">
      <!-- <pre>{{ employee_tree }}</pre> -->

      <p>
        This should include the employee id of the ceo
        <!-- {{root_employees}} -->
        {{root_employees[0].employee_id}}
     </p>
    </div>

    <div v-else class="loading-screen">
      <div class="spinner"></div>
      <p>Loading employee tree...</p>
    </div>

    <EmployeeCard></EmployeeCard>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Employee, buildEmployeeTree } from '@/models/Employee.js'
import EmployeeCard from './components/EmployeeCard.vue'

const root_employees = ref([])
const error = ref(null)

async function fetchEmployeeTree() {
  try {
    const res = await fetch('http://localhost:5000/employee_tree')
    const json = await res.json()

    root_employees.value = buildEmployeeTree(json)
    console.log(root_employees.value[0].employee_id)
  } catch (err) {
    console.error(err)
    error.value = err.message || 'Unknown error'
  }
}

onMounted(() => {
  fetchEmployeeTree()
})
</script>

<style scoped>
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

.error {
  color: #b00020;
  background: #ffe6e6;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}
</style>
