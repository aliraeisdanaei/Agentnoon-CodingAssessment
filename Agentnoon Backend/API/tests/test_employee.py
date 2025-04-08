import pytest
from AgentnoonBackend.models.employee import Employee

from AgentnoonBackend.tests.employee_directory import *

def reset_testing_env():
    Employee.set_ceo(employee_1)
    Employee.reset_tree_fields()


def test_employee_initialization():
    assert employee_1.employee_id == '1'
    assert employee_2.manager_id == '1'
    assert employee_4.manager == employee_2


def test_add_subordinate():
    assert employee_1.subordinates == [employee_2, employee_3]
    assert employee_2.subordinates == [employee_4]
    assert employee_4.subordinates == [employee_5]


def test_reset_tree_fields():
    Employee.ceo = None
    assert Employee.ceo is None
    with pytest.raises(Exception):
        Employee.reset_tree_fields()
    
    reset_testing_env()

    q = []
    q.append(employee_1)
    while len(q) != 0:
        emp = q.pop()
        assert emp.management_cost == None
        assert emp.ic_cost == None
        assert emp.total_cost == None
        assert emp.num_descendants == None

        for sub in emp.subordinates:
            q.append(sub)

def test_get_bare_tree():
    Employee.ceo = None
    assert Employee.ceo is None
    with pytest.raises(Exception):
        Employee.reset_tree_fields()
    
    Employee.set_ceo(employee_1)

    bare_tree = {'1': [
        {'2': [
            {'4': [
                {'5': [
                    {'6': []}, {'7': []}
                ]
                }
            ]}
        ]},
        {'3': [
            {'8': [
                {'9': [
                    {'10': []}, {'11': []}, {'12': []}
                ]}
            ]}
        ]}
    ]}

    assert bare_tree == Employee.get_bare_tree()

def test_get_employee_dict():
    employee_1_dict = employee_data = {
        'employee_id': '1',
        'name': "John Doe",
        'job_title': "CEO",
        'email': "johndoe@example.com",
        'manager_id': "",
        'status': "Active",
        'start_date': datetime(2020, 1, 1),
        'department': "Executive",
        'location': "Headquarters",
        'salary': 250000,
        'bonus': 20000,
        'end_date': None,
        'photo': None,
        'performance': None,
        'project': None,
        'entity': None,
        'recruiting': None,
        'skill': None,
        'role': None,
        'utilization': None,
        'source': None,
        'level': None,
        'num_descendants': employee_1_num_descendants,
        'management_cost': employee_1_management_cost,
        'ic_cost': employee_1_ic_cost,
        'total_cost': employee_1_total_cost,
    }
    employee_1.get_recursive_fields()
    assert employee_1_dict == employee_1.get_employee_dict()

    reset_testing_env()


def test_get_recursive_fields():
    num_descendants, management_cost, ic_cost, total_cost = employee_1.get_recursive_fields()
    assert num_descendants + 1 == len(employee_directory) 
    assert ic_cost + management_cost == total_cost
    assert total_cost + employee_1.salary == sum(e.salary for e in employee_directory.values())

    for employee, expected_values in employee_expected.items():
        expected_num_descendants, expected_management_cost, expected_ic_cost, expected_total_cost = expected_values
        assert expected_num_descendants == employee.num_descendants, f'{employee.management_cost}'
        assert expected_management_cost == employee.management_cost
        assert expected_ic_cost == employee.ic_cost
        assert employee.ic_cost + employee.management_cost == employee.total_cost
        assert expected_total_cost == employee.total_cost
    
    Employee.reset_tree_fields()


def test_get_management_cost():
    assert employee_1_management_cost == employee_1.get_management_cost()
    for employee, expected_values in employee_expected.items():
        _, expected_management_cost, _, _ = expected_values
        assert employee.num_descendants is None
        assert expected_management_cost == employee.management_cost
        assert employee.ic_cost is None
        assert employee.total_cost is None
    
    Employee.reset_tree_fields()


def test_get_management_cost_from_middle():
    assert employee_8_management_cost == employee_8.get_management_cost()
    for employee in [employee_8, employee_9, employee_10, employee_11, employee_12]:
        expected_values = employee_expected[employee]
        _, expected_management_cost, _, _ = expected_values
        assert employee.num_descendants is None
        assert expected_management_cost == employee.management_cost
        assert employee.ic_cost is None
        assert employee.total_cost is None
    
    employee_1.reset_tree_fields()


def test_get_ic_cost():
    assert employee_1_ic_cost == employee_1.get_ic_cost()
    for employee, expected_values in employee_expected.items():
        _, _, expected_ic_cost, _ = expected_values
        assert employee.num_descendants is None
        assert employee.management_cost is None
        assert expected_ic_cost == employee.ic_cost
        assert employee.total_cost is None

    employee_1.reset_tree_fields()


def test_get_ic_cost_from_middle():
    assert employee_8_ic_cost == employee_8.get_ic_cost()
    for employee in [employee_8, employee_9, employee_10, employee_11, employee_12]:
        expected_values = employee_expected[employee]
        _, _, expected_ic_cost, _ = expected_values
        assert employee.num_descendants is None
        assert employee.management_cost is None
        assert expected_ic_cost == employee.ic_cost
        assert employee.total_cost is None

    employee_1.reset_tree_fields()


def test_get_num_descendants():
    assert employee_1_num_descendants == employee_1.get_num_descendants()
    for employee, expected_values in employee_expected.items():
        expected_num_descendants, _, _, _ = expected_values
        assert expected_num_descendants == employee.num_descendants
        assert employee.management_cost is None
        assert employee.ic_cost is None
        assert employee.total_cost is None

    employee_1.reset_tree_fields()

def test_get_num_descendants_from_middle():
    assert employee_8_num_descendants == employee_8.get_num_descendants()
    for employee in [employee_8, employee_9, employee_10, employee_11, employee_12]:
        expected_values = employee_expected[employee]
        expected_num_descendants, _, _, _ = expected_values
        assert expected_num_descendants == employee.num_descendants
        assert employee.management_cost is None
        assert employee.ic_cost is None
        assert employee.total_cost is None

    employee_1.reset_tree_fields()


def test_get_total_cost():
    assert employee_1_total_cost == employee_1.get_total_cost()
    for employee, expected_values in employee_expected.items():
        _, expected_management_cost, expected_ic_cost, expected_total_cost = expected_values
        expected_num_descendants, expected_management_cost, expected_ic_cost, expected_total_cost = expected_values
        assert employee.num_descendants is None
        assert expected_management_cost == employee.management_cost
        assert expected_ic_cost == employee.ic_cost
        assert employee.ic_cost + employee.management_cost == employee.total_cost
        assert expected_total_cost == employee.total_cost

    employee_1.reset_tree_fields()

def test_get_total_cost_from_middle():
    assert employee_8_total_cost == employee_8.get_total_cost()
    for employee in [employee_8, employee_9, employee_10, employee_11, employee_12]:
        expected_values = employee_expected[employee]
        _, expected_management_cost, expected_ic_cost, expected_total_cost = expected_values
        expected_num_descendants, expected_management_cost, expected_ic_cost, expected_total_cost = expected_values
        assert employee.num_descendants is None
        assert expected_management_cost == employee.management_cost
        assert expected_ic_cost == employee.ic_cost
        assert employee.ic_cost + employee.management_cost == employee.total_cost
        assert expected_total_cost == employee.total_cost

    employee_1.reset_tree_fields()
