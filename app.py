# -*- coding: utf-8 -*-
"""
Student Performance Prediction System
Updated Backend Code with Landing Page + Clean Routing
"""

import os
import pandas as pd
from flask import Flask, render_template, request
import pickle

# -----------------------------
# Load dataset & model safely
# -----------------------------

try:
    df = pd.read_csv("StudentsPerformance.csv")
except Exception as e:
    print("Error loading dataset:", e)
    df = pd.DataFrame()

try:
    model = pickle.load(open('model.sav', 'rb'))
except Exception as e:
    print("Error loading model:", e)
    model = None


app = Flask(__name__)


# -----------------------------
# ML Feature Processing
# -----------------------------
def features(gender, race, education, lunch, course):
    """Prepare features for model prediction."""

    test_row = [gender, race, education, lunch, course]

    categorical_columns = [
        'gender',
        'race/ethnicity',
        'parental level of education',
        'lunch',
        'test preparation course'
    ]

    df_cat = df[categorical_columns].copy()

    # Append the new input row
    df_cat.loc[len(df_cat)] = test_row

    # One-hot encoding
    df_dummies = pd.get_dummies(df_cat, drop_first=True)

    # Prepare final input values
    input_values = df_dummies.iloc[-1].values

    # Predict using model
    prediction = model.predict([input_values])
    return prediction


# -----------------------------
# Flask Routes
# -----------------------------

# Landing Page
@app.route('/')
def landing():
    return render_template('landing.html')


# Route: Show prediction form
@app.route('/predict')
def predict_page():
    return render_template('predictor_form.html')


# Route: Prediction logic
@app.route('/result', methods=["POST"])
def results():
    gender = request.form['gender']
    race = request.form['race']
    education = request.form['education']
    lunch = request.form['lunch']
    course = request.form['course']

    pred = features(gender, race, education, lunch, course)[0]

    math_score = round(pred[0], 0)
    reading_score = round(pred[1], 0)
    writing_score = round(pred[2], 0)

    return render_template(
        'result_form.html',
        gender=gender,
        race=race,
        education=education,
        lunch=lunch,
        course=course,
        math_score=math_score,
        reading_score=reading_score,
        writing_score=writing_score
    )


# Route: Dataset Visualization (SweetViz)
@app.route('/visualisation', methods=["GET", "POST"])
def visualisation():
    return render_template('Report.html')


# -----------------------------
# Server Configuration
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
