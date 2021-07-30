def test_obtener_registros(client):
    url = '/employees/predictions'
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
    res = client.post(url, json=example)
    assert res.status_code == 201
    assert res.json["turnover_score"] == 0
