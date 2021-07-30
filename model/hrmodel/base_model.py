import joblib
import os
import pandas as pd

clf = joblib.load(os.path.dirname(__file__)+'/clf.model')


def get_turnover_score(dataframe):
    drop_columns = ['EmployeeCount', 'EmployeeNumber', 'JobLevel', 'Over18',
                    'StandardHours', 'TotalWorkingYears', 'Attrition']
    columns = list(dataframe.columns)
    for x in drop_columns:
        columns.remove(x)
    dataframe["TurnoverScore"] = clf.predict_proba(dataframe[columns])[:,1]

    return dataframe


def hr_predict(request):
    df = pd.DataFrame([request])
    ID = int(df["EmployeeNumber"][0])
    df.drop(columns=['EmployeeNumber'], inplace=True)
    prediction = clf.predict_proba(df)
    output = {'ID': ID, 'turnover_score': list(prediction[:,1])[0]}
    return output
