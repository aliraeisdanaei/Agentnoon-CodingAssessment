class Employee {
    constructor(employee_id, manager = null) {
        this.employee_id = employee_id
        this.manager = manager // Another Employee object or null
        this.subordinates = [] // Array of Employee objects
    }

    addSubordinate(sub) {
        this.subordinates.push(sub)
        sub.manager = this
    }
}

function buildEmployeeTree(tree, manager = null) {
    const result = []

    // Ensure there's only one root employee (the CEO)
    const employeeIds = Object.keys(tree)
    if (employeeIds.length !== 1) {
        throw new Error('There must be exactly one root employee (CEO) in the tree.')
    }

    // Loop over the single root employee
    const rootEmployeeId = employeeIds[0]
    const subs = tree[rootEmployeeId]

    // Create the CEO Employee
    const employee = new Employee(rootEmployeeId, manager)

    // Build subordinates for the CEO
    for (const sub of subs) {
        const subEmployees = buildEmployeeTree(sub, employee)
        employee.subordinates.push(...subEmployees)
    }

    result.push(employee)

    return result
}


export { Employee, buildEmployeeTree }