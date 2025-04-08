
import { Employee, buildEmployeeTree } from '@/models/Employee.js'

// Function to fetch employee data by employee_id
export async function fetchEmployeeData(employeeId) {
    try {
        const response = await fetch(`http://localhost:5000/employee/${employeeId}`)

        if (!response.ok) {
            throw new Error(`Failed to fetch employee data. Status: ${response.status}`)
        }

        return await response.json()
    } catch (error) {
        console.error('Error fetching employee data:', error)
        throw error
    }
}

// You can add more API-related functions here if needed, for example:
export async function fetchEmployeeTree() {
    try {
        const response = await fetch('http://localhost:5000/employee_tree')

        if (!response.ok) {
            throw new Error(`Failed to fetch employee tree. Status: ${response.status}`)
        }

        return await response.json()
    } catch (error) {
        console.error('Error fetching employee tree:', error)
        throw error
    }
}
