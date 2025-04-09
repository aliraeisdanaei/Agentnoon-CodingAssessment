// stores/employeeStore.js
import { defineStore } from 'pinia'

export const useEmployeeStore = defineStore('employee', {
    state: () => ({
        employeeShown: null, // This will hold the employee data
    }),
    actions: {
        // Action to update the employee data
        setEmployee(employee) {
            this.employeeShown = employee
        },
    },
    getters: {
        // Getter to get employee name
        employeeName(state) {
            return state.employeeShown ? state.employeeShown.name : ''
        },
    },
})
