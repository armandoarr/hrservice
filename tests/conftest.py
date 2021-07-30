import pytest
import sys

sys.path.append("..")


@pytest.fixture(scope="session")
def app():
    from model.api import app as flask_app
    yield flask_app


@pytest.fixture
def client(app, monkeypatch):
    from model import api
    flask_app = api.app
    app_client = flask_app.test_client()
    example = {'Age': 37,
               'BusinessTravel': 'Travel_Frequently',
               'DailyRate': 18,
               'Department': 'Research & Development',
               'DistanceFromHome': 20,
               'Education': 4,
               'EducationField': 'Life Sciences',
               'EmployeeNumber': 23333,
               'EnvironmentSatisfaction': 10,
               'Gender': 'Female',
               'HourlyRate': 54,
               'JobInvolvement': 3,
               'JobRole': 'Research Scientist',
               'JobSatisfaction': 1,
               'MaritalStatus': 'Married',
               'MonthlyIncome': 4567,
               'MonthlyRate': 23456,
               'NumCompaniesWorked': 2,
               'OverTime': 'Yes',
               'PercentSalaryHike': 20,
               'PerformanceRating': 4,
               'RelationshipSatisfaction': 3,
               'StockOptionLevel': 1,
               'TrainingTimesLastYear': 3,
               'WorkLifeBalance': 2,
               'YearsAtCompany': 15,
               'YearsInCurrentRole': 3,
               'YearsSinceLastPromotion': 2,
               'YearsWithCurrManager': 2}
    req = app_client.post("/employees/predictions", json=example)
    assert req.status_code == 201
    assert req.json["turnover_score"] in [0, 1]
    return app_client
