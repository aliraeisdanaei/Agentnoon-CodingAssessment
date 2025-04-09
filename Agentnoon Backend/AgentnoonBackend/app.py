from flask import Flask
from flask_cors import CORS

def create_app(employee_directory=None) -> Flask:
    import pandas as pd
    import os

    from .models.employee import Employee
    from .routes.routes import register_routes
    from typing import Dict

    app = Flask(__name__)
    CORS(app)

    def generate_employees_directory() -> Dict[str, Employee]:
        # SHEET_NAME = "Giga Corp (40k) - Sheet1 short.csv"
        SHEET_NAME = "Giga Corp (40k) - Sheet1.csv"
        SHEET_PATH = os.path.join(os.path.dirname(__file__), 'data', 'Giga Corp (40k) - Sheet1 short.csv')
        employee_df = pd.read_csv(SHEET_PATH)

        employee_df.columns = employee_df.columns.str.strip().str.lower().str.replace(' ', '_')
        employee_df['start_date'] = pd.to_datetime(employee_df['start_date'], errors='coerce')
        employee_df['end_date'] = pd.to_datetime(employee_df['end_date'], errors='coerce')
        # employee_df['manager'] = employee_df['manager'].fillna('')
        employee_df = employee_df.map(lambda x: None if pd.isna(x) else x)
        employee_df.rename(columns={'manager': 'manager_id'}, inplace=True)

        employees = {
            row['employee_id']: Employee(**row.to_dict()) 
            for _, row in employee_df.iterrows()}
        
        return employees
    
    if employee_directory is None:
        app.config['employee_directory'] = generate_employees_directory()
    else:
        app.config['employee_directory'] = employee_directory

    Employee.set_employee_tree(app.config.get('employee_directory'))
    app.config['EmployeeClass'] = Employee
    register_routes(app)

    return app
