from datetime import datetime
from AgentnoonBackend.models.employee import Employee

# Layer 1 (CEO)
employee_1 = Employee(
    employee_id='1',
    name="John Doe",
    job_title="CEO",
    email="johndoe@example.com",
    manager_id="",
    status="Active",
    start_date=datetime(2020, 1, 1),
    department="Executive",
    location="Headquarters",
    salary=250000,
    bonus=20000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

# Layer 2 (Managers)
employee_2 = Employee(
    employee_id='2',
    name="Jane Smith",
    job_title="VP of Engineering",
    email="janesmith@example.com",
    manager_id="1",
    status="Active",
    start_date=datetime(2019, 5, 1),
    department="Engineering",
    location="Remote",
    salary=180000,
    bonus=10000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_3 = Employee(
    employee_id='3',
    name="Mike Johnson",
    job_title="VP of Marketing",
    email="mikejohnson@example.com",
    manager_id="1",
    status="Active",
    start_date=datetime(2020, 3, 1),
    department="Marketing",
    location="Headquarters",
    salary=175000,
    bonus=9000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

# Layer 3 (Subordinates under Employee 2 - Engineering Department)
employee_4 = Employee(
    employee_id='4',
    name="Alice Brown",
    job_title="Engineering Manager",
    email="alicebrown@example.com",
    manager_id="2",
    status="Active",
    start_date=datetime(2018, 7, 1),
    department="Engineering",
    location="Remote",
    salary=120000,
    bonus=7000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_5 = Employee(
    employee_id='5',
    name="David Lee",
    job_title="Engineering Lead",
    email="davidlee@example.com",
    manager_id="4",
    status="Active",
    start_date=datetime(2019, 9, 1),
    department="Engineering",
    location="Remote",
    salary=110000,
    bonus=6000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_6 = Employee(
    employee_id='6',
    name="Eve White",
    job_title="Software Engineer",
    email="evewhite@example.com",
    manager_id="5",
    status="Active",
    start_date=datetime(2021, 5, 1),
    department="Engineering",
    location="Remote",
    salary=95000,
    bonus=5000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_7 = Employee(
    employee_id='7',
    name="Charlie Green",
    job_title="Software Engineer",
    email="charliegreen@example.com",
    manager_id="5",
    status="Active",
    start_date=datetime(2021, 6, 1),
    department="Engineering",
    location="Remote",
    salary=96000,
    bonus=5000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

# Layer 3 (Subordinates under Employee 3 - Marketing Department)
employee_8 = Employee(
    employee_id='8',
    name="Sophia Turner",
    job_title="Marketing Manager",
    email="sophiaturner@example.com",
    manager_id="3",
    status="Active",
    start_date=datetime(2017, 8, 1),
    department="Marketing",
    location="Headquarters",
    salary=115000,
    bonus=8000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_9 = Employee(
    employee_id='9',
    name="Oliver Harris",
    job_title="Marketing Lead",
    email="oliverharris@example.com",
    manager_id="8",
    status="Active",
    start_date=datetime(2020, 11, 1),
    department="Marketing",
    location="Headquarters",
    salary=105000,
    bonus=6500,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_10 = Employee(
    employee_id='10',
    name="Lucas Scott",
    job_title="Marketing Specialist",
    email="lucasscott@example.com",
    manager_id="9",
    status="Active",
    start_date=datetime(2021, 3, 1),
    department="Marketing",
    location="Headquarters",
    salary=85000,
    bonus=4500,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_11 = Employee(
    employee_id='11',
    name="Isla Wilson",
    job_title="Marketing Intern",
    email="islawilson@example.com",
    manager_id="9",
    status="Active",
    start_date=datetime(2022, 1, 1),
    department="Marketing",
    location="Headquarters",
    salary=40000,
    bonus=2000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

employee_12 = Employee(
    employee_id='12',
    name="Amelia King",
    job_title="Marketing Intern",
    email="ameliaking@example.com",
    manager_id="9",
    status="Active",
    start_date=datetime(2022, 2, 1),
    department="Marketing",
    location="Headquarters",
    salary=40000,
    bonus=2000,
    end_date=None,
    photo=None,
    performance=None,
    project=None,
    entity=None,
    recruiting=None,
    skill=None,
    role=None,
    utilization=None,
    source=None,
    level=None
)

Employee.set_ceo(employee_1)
employees = [
    employee_1, employee_2, employee_3, employee_4,
    employee_5, employee_6, employee_7, employee_8,
    employee_9, employee_10, employee_11, employee_12
]

employee_directory = {str(i + 1): employee for i, employee in enumerate(employees)}

# Establishing the tree relationships
employee_1.add_subordinate(employee_2)
employee_1.add_subordinate(employee_3)

employee_2.add_subordinate(employee_4)
employee_3.add_subordinate(employee_8)

employee_4.add_subordinate(employee_5)
employee_8.add_subordinate(employee_9)

employee_5.add_subordinate(employee_6)
employee_5.add_subordinate(employee_7)
employee_9.add_subordinate(employee_10)
employee_9.add_subordinate(employee_11)
employee_9.add_subordinate(employee_12)

employee_4.set_manager(employee_2)
employee_5.set_manager(employee_4)
employee_6.set_manager(employee_5)
employee_7.set_manager(employee_5)
employee_8.set_manager(employee_3)
employee_9.set_manager(employee_8)
employee_10.set_manager(employee_9)
employee_11.set_manager(employee_9)
employee_12.set_manager(employee_9)

"""
The Employee Tree
                          Employee_1                                     
                            │                                            
         Employee_2 ────────┴────────── Employee_3                       
              │                               │                          
                                              │                          
                                              Employee_8                 
         Employee_4                              │                       
              │                                  │                       
              │                               Employee_9                 
          Employee_5                             │                       
              │                          ┌───────┼───┬────────────┐      
              │                          │           │            │      
Employee_6 ───┴─── Employee_7      Employee_10   Employee_11  Employee_12
"""


# set the expected records
employee_12_num_descendants = 0
employee_12_management_cost = 0.0
employee_12_ic_cost = 0.0
employee_12_total_cost = 0.0

employee_11_num_descendants = 0
employee_11_management_cost = 0.0
employee_11_ic_cost = 0.0
employee_11_total_cost = 0.0

employee_10_num_descendants = 0
employee_10_management_cost = 0.0
employee_10_ic_cost = 0.0
employee_10_total_cost = 0.0

employee_9_num_descendants = 3
employee_9_management_cost = 0.0
employee_9_ic_cost = employee_12.salary + employee_11.salary + employee_10.salary
employee_9_total_cost = employee_9_ic_cost

employee_7_num_descendants = 0
employee_7_management_cost = 0.0
employee_7_ic_cost = 0.0
employee_7_total_cost = 0.0

employee_6_num_descendants = 0
employee_6_management_cost = 0.0
employee_6_ic_cost = 0.0
employee_6_total_cost = 0.0

employee_5_num_descendants = 2
employee_5_management_cost = 0.0
employee_5_ic_cost = employee_6.salary + employee_7.salary
employee_5_total_cost = employee_5_ic_cost

employee_8_num_descendants = 4
employee_8_management_cost = employee_9.salary + employee_9_management_cost
employee_8_ic_cost = employee_9_ic_cost
employee_8_total_cost = employee_8_management_cost + employee_8_ic_cost

employee_4_num_descendants = 3
employee_4_management_cost = employee_5.salary + employee_5_management_cost
employee_4_ic_cost = employee_5_ic_cost
employee_4_total_cost = employee_4_management_cost + employee_4_ic_cost

employee_3_num_descendants = 5
employee_3_management_cost = employee_8.salary + employee_8_management_cost
employee_3_ic_cost = employee_8_ic_cost
employee_3_total_cost = employee_3_management_cost + employee_3_ic_cost

employee_2_num_descendants = 4
employee_2_management_cost = employee_4.salary + employee_4_management_cost
employee_2_ic_cost = employee_4_ic_cost
employee_2_total_cost = employee_2_management_cost + employee_2_ic_cost

employee_1_num_descendants = 11
employee_1_management_cost = employee_2.salary + employee_2_management_cost + employee_3.salary + employee_3_management_cost
employee_1_ic_cost = employee_2_ic_cost + employee_3_ic_cost
employee_1_total_cost = employee_1_management_cost + employee_1_ic_cost

employee_expected = {
    employee_12: (employee_12_num_descendants, employee_12_management_cost, employee_12_ic_cost, employee_12_total_cost),
    employee_11: (employee_11_num_descendants, employee_11_management_cost, employee_11_ic_cost, employee_11_total_cost),
    employee_10: (employee_10_num_descendants, employee_10_management_cost, employee_10_ic_cost, employee_10_total_cost),
    employee_9: (employee_9_num_descendants, employee_9_management_cost, employee_9_ic_cost, employee_9_total_cost),
    employee_8: (employee_8_num_descendants, employee_8_management_cost, employee_8_ic_cost, employee_8_total_cost),
    employee_7: (employee_7_num_descendants, employee_7_management_cost, employee_7_ic_cost, employee_7_total_cost),
    employee_6: (employee_6_num_descendants, employee_6_management_cost, employee_6_ic_cost, employee_6_total_cost),
    employee_5: (employee_5_num_descendants, employee_5_management_cost, employee_5_ic_cost, employee_5_total_cost),
    employee_4: (employee_4_num_descendants, employee_4_management_cost, employee_4_ic_cost, employee_4_total_cost),
    employee_3: (employee_3_num_descendants, employee_3_management_cost, employee_3_ic_cost, employee_3_total_cost),
    employee_2: (employee_2_num_descendants, employee_2_management_cost, employee_2_ic_cost, employee_2_total_cost),
    employee_1: (employee_1_num_descendants, employee_1_management_cost, employee_1_ic_cost, employee_1_total_cost)
}