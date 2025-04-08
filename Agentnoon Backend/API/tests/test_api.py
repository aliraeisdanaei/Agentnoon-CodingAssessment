import pytest
from flask.testing import FlaskClient

from AgentnoonBackend.app import create_app

from AgentnoonBackend.tests.employee_directory import *

@pytest.fixture
def app():
    print(employee_directory)
    app = create_app(employee_directory=employee_directory)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_welcome(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Welcome to this wonderful API. PLEASE HIRE ME :)'


def test_get_employee_tree(client: FlaskClient):
    response = client.get('/employee_tree')
    assert response.status_code == 200
    assert Employee.get_bare_tree() == response.json


def test_get_employee(client: FlaskClient):
    for id, emp in employee_directory.items():
        response = client.get(f'/employee/{id}')
        assert response.status_code == 200

        emp_data = emp.get_employee_dict()
        resp_data = response.json

        # the dates are in different formats
        for date_field in ['start_date', 'end_date']:
            if emp_data[date_field] is None:
                assert resp_data[date_field] is None
            else:
                assert emp_data[date_field].strftime("%a, %d %b %Y %H:%M:%S GMT") == resp_data[date_field]
            emp_data.pop(date_field)
            resp_data.pop(date_field)
        assert emp_data == resp_data


def test_get_employee_not_found(client: FlaskClient):
    response = client.get('/employee/999')
    assert response.status_code == 404
    assert response.json == {"error": "Employee not found"}
