import pandas as pd
import logging
import sqlalchemy
import os
import re

from model.hrmodel.base_model import get_turnover_score

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = sqlalchemy.create_engine('postgresql://postgres:p4ssw0rd@localhost:5432/postgres')


def split_column_name(column_name):
    split = re.findall('[A-Z][^A-Z]*', column_name)
    return split


def get_model():
    employees = pd.read_csv(os.path.dirname(__file__)+"HR_Employee_Attrition.csv")
    hr_model = get_turnover_score(employees)

    return hr_model


def load_employees(employees):
    new_columns = []
    for x in employees.columns:
        name = split_column_name(x)
        new_name = "_".join(name)
        new_name = new_name.lower().strip()
        new_columns.append(new_name)
    employees.columns = new_columns

    employees.to_sql("employee_attrition",
                     engine,
                     if_exists="append",
                     index=False,
                     dtype={'age': sqlalchemy.types.Integer,
                            'attrition': sqlalchemy.types.String,
                            'business_travel': sqlalchemy.types.String,
                            'daily_rate': sqlalchemy.types.Integer,
                            'department': sqlalchemy.types.String,
                            'distance_from_home': sqlalchemy.types.Integer,
                            'education': sqlalchemy.types.Integer,
                            'education_field': sqlalchemy.types.String,
                            'employee_count': sqlalchemy.types.Integer,
                            'employee_number': sqlalchemy.types.NUMERIC,
                            'environment_satisfaction': sqlalchemy.types.Integer,
                            'gender': sqlalchemy.types.String,
                            'hourly_rate': sqlalchemy.types.Integer,
                            'job_involvement': sqlalchemy.types.Integer,
                            'job_level': sqlalchemy.types.Integer,
                            'job_role': sqlalchemy.types.String,
                            'job_satisfaction': sqlalchemy.types.Integer,
                            'marital_status': sqlalchemy.types.String,
                            'monthly_income': sqlalchemy.types.Float,
                            'monthly_rate': sqlalchemy.types.Float,
                            'num_companies_worked': sqlalchemy.types.Integer,
                            'over18': sqlalchemy.types.String,
                            'over_time': sqlalchemy.types.String,
                            'percent_salary_hike': sqlalchemy.types.Integer,
                            'performance_rating': sqlalchemy.types.Integer,
                            'relationship_satisfaction': sqlalchemy.types.Integer,
                            'standard_hours': sqlalchemy.types.Integer,
                            'stock_option_level': sqlalchemy.types.Integer,
                            'total_working_years': sqlalchemy.types.Integer,
                            'training_times_last_year': sqlalchemy.types.Integer,
                            'work_life_balance': sqlalchemy.types.Integer,
                            'years_at_company':sqlalchemy.types.Integer,
                            'years_in_current_role': sqlalchemy.types.Integer,
                            'years_since_last_promotion': sqlalchemy.types.Integer,
                            'years_with_curr_manager': sqlalchemy.types.Integer,
                            'turnover_score': sqlalchemy.types.Float
                            })


if __name__ == '__main__':
    employees = get_model()
    load_employees(employees)
