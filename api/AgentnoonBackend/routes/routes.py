from flask import Flask, current_app, Blueprint, Response, jsonify

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def welcome() -> Response:
    return 'Welcome to this wonderful API. PLEASE HIRE ME :)'


@main_bp.route('/employee_tree', methods=['GET'])
def get_sample() -> Response:
    return jsonify(current_app.config.get('EmployeeClass').ceo.get_bare_tree())


@main_bp.route('/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id: str) -> Response:
    if employee_id not in current_app.config.get('employee_directory'):
        return jsonify({"error": "Employee not found"}), 404
    employee = current_app.config.get('employee_directory')[employee_id]
    return jsonify(employee.get_employee_dict())


def register_routes(app: Flask) -> None:
    app.register_blueprint(main_bp)

