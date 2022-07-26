"""
Creator: Ivanovitch Silva
Date: 26 April. 2022
Script that POSTS to the API using the requests
module and returns both the result of
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "customerID" : '0000-AAAAAA',
        "gender"  : 'Male',
        "SeniorCitizen" :  0,
        "Partner" : 'Yes',
        "Dependents" : 'No',
        "tenure" : 10,
        "PhoneService" :  'Yes',
        "MultipleLines" : 'No',
        "InternetService" : 'DSL',
        "OnlineSecurity" : 'No',
        "OnlineBackup" : 'No',
        "DeviceProtection" : 'No',
        "TechSupport" : 'No',
        "StreamingTV" : 'No',
        "StreamingMovies" : 'No',
        "Contract" : 'One year',
        "PaperlessBilling" : 'Yes',
        "PaymentMethod" :  'Mailed check',
        "MonthlyCharges" : 29.85,
        "TotalCharges" : 29.85
    }

#url = "http://127.0.0.1:8000"
#url = "https://teste-am.herokuapp.com"
url = "https://project1-ml-ppgeec1.herokuapp.com"
response = requests.post(f"{url}/predict",
                         json=person)


print(f"Request: {url}/predict")
print(f"Person: \n customerID: {person['customerID']}\n gender: {person['gender']}\n"\
      f" SeniorCitizen: {person['SeniorCitizen']}\n Partner: {person['Partner']}\n"\
      f" Dependents: {person['Dependents']}\n"\
      f" tenure: {person['tenure']}\n"\
      f" PhoneService: {person['PhoneService']}\n"\
      f" MultipleLines: {person['MultipleLines']}\n"\
      f" InternetService: {person['InternetService']}\n"\
      f" OnlineSecurity: {person['OnlineSecurity']}\n"\
      f" OnlineBackup: {person['OnlineBackup']}\n"\
      f" DeviceProtection: {person['DeviceProtection']}\n"\
      f" TechSupport: {person['TechSupport']}\n"\
      f" StreamingTV: {person['StreamingTV']}\n"\
      f" StreamingMovies: {person['StreamingMovies']}\n"\
      f" Contract: {person['Contract']}\n"\
      f" PaperlessBilling: {person['PaperlessBilling']}\n"\
      f" PaymentMethod: {person['PaymentMethod']}\n"\
      f" MonthlyCharges: {person['MonthlyCharges']}\n"\
      f" TotalCharges: {person['TotalCharges']}\n"
     )
#print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")