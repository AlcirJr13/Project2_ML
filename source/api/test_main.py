"""
Creator: Ivanovitch Silva
Date: 18 April 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with no churn
def test_get_inference_no_churn():

    person = {
        "customerID" : '0000-AAAAAA',
        "gender"  : 'Female',
        "SeniorCitizen" :  0,
        "Partner" : 'Yes',
        "Dependents" : 'No',
        "tenure" : 1,
        "PhoneService" :  'No',
        "MultipleLines" : 'No phone service',
        "InternetService" : 'DSL',
        "OnlineSecurity" : 'No',
        "OnlineBackup" : 'Yes',
        "DeviceProtection" : 'No',
        "TechSupport" : 'No',
        "StreamingTV" : 'No',
        "StreamingMovies" : 'No',
        "Contract" : 'Month-to-month',
        "PaperlessBilling" : 'Yes',
        "PaymentMethod" :  'Electronic check',
        "MonthlyCharges" : 29.85,
        "TotalCharges" : 29.85
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "No Churn"

# a unit test that tests the status code and response 
# for an instance with churn
def test_get_inference_churn():

    person = {
        "customerID" : '0000-AAAAAA',
        "gender"  : 'Male',
        "SeniorCitizen" :  1,
        "Partner" : 'No',
        "Dependents" : 'No',
        "tenure" : 1,
        "PhoneService" :  'No',
        "MultipleLines" : 'No phone service',
        "InternetService" : 'DSL',
        "OnlineSecurity" : 'No',
        "OnlineBackup" : 'No',
        "DeviceProtection" : 'Yes',
        "TechSupport" : 'No',
        "StreamingTV" : 'No',
        "StreamingMovies" : 'Yes',
        "Contract" : 'Month-to-month',
        "PaperlessBilling" : 'No',
        "PaymentMethod" :  'Mailed check',
        "MonthlyCharges" : 20.15,
        "TotalCharges" : 20.15
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "Churn"