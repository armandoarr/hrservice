from flask import Flask, abort, request, jsonify
from flask_sqlalchemy_session import flask_scoped_session
from psycopg2.extras import (RealDictCursor, RealDictRow)
from .hrmodel.base_model import hr_predict

import psycopg2
import logging
import sys
import os
import pandas as pd

app = Flask(__name__)
params = {
    "host": "localhost",
    "port": 5438,
    "database": "postgres",
    "user": "postgres",
    "password": "p4ssw0rd"
    }


def humanize_score(employee):
    score = employee.get('turnover_score')
    if score >= 0.6:
        turnover_score = 1
    else:
        turnover_score = 0
    employee.update({'turnover_score': turnover_score})
    return employee


def connect(params):
    conn = None
    try:
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex)
        sys.exit(1)
    print("Conexión exitosa")
    return conn


@app.route('/employees/scores/<int:employee_id>', methods=["GET"])
def get_employee_score(employee_id):
    conn = connect(params)
    sql = """SELECT employee_number, turnover_score FROM employee_attrition WHERE employee_number = {};""".format(employee_id)
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        try:
            cursor.execute(sql)
        except (Exception, psycopg2.DatabaseError) as ex:
            print("Hubo un error: %s" % ex)
            cursor.close()
            return abort(500)
        resp = cursor.fetchall()
        cursor.close()
        return jsonify(resp[0]), 200, {"Content-Type": 'application/json'}


@app.route('/employees/predictions', methods=["POST"])
def get_employee_prediction():
    reg = request.json
    try:
        output = hr_predict(reg)
    except Exception as ex:
        print("Se produjo un error: %s" % ex)
    output = humanize_score(output)

    return output, 201, {"Content-Type": 'application/json'}


if __name__ != "__main__":
    app.run(host="0.0.0.0", debug=True)
