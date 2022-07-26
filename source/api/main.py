# from typing import Union
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import pandas as pd
import joblib
import os
import wandb
#import tensorflow
import sys
#classes que criamos no pipeline
from source.api.pipeline import FeatureSelector, CategoricalTransformer, NumericalTransformer

# global variables
#todas as classes que criamos são modulos
setattr(sys.modules["__main__"], "FeatureSelector", FeatureSelector)
setattr(sys.modules["__main__"], "CategoricalTransformer", CategoricalTransformer)
setattr(sys.modules["__main__"], "NumericalTransformer", NumericalTransformer)

# name of the model artifact wandb
#lembrar de fazer login no terminal
artifact_model_name = "alcirjr/projeto_2_AM/model_export:latest"

# initiate the wandb project
run = wandb.init(project="projeto_2_AM",job_type="api")

# create the api
app = FastAPI()

# declare request example data using pydantic
# a person in our dataset has the following attributes aa
class Person(BaseModel):
    customerID: str
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection:str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

    #adaptando o template do fastapi para nosso problema
    class Config:
        schema_extra = {
            "example": {
                "customerID" : '0000-AAAAA',
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
                "MonthlyCharges" : 29.30,
                "TotalCharges" : 29.30
            }
        }

# give a greeting using GET
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><span style="font-size:28px"><strong>Hello World</strong></span></p>"""\
    """<p><span style="font-size:20px">In this project, we will apply the skills """\
        """acquired in the Deploying a Scalable ML Pipeline in Production course to develop """\
        """a classification model on publicly available"""\
        """<a href="https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction"> Kaggle </a>.</span></p>"""

# run the model inference and use a Person data structure via POST to the API.
@app.post("/predict")
async def get_inference(person: Person):

    # Download inference artifact
    model_export_path = run.use_artifact(artifact_model_name).file()
    pipe = joblib.load(model_export_path)

    # Create a dataframe from the input feature
    # note that we could use pd.DataFrame.from_dict
    # but due be only one instance, it would be necessary to
    # pass the Index.
    df = pd.DataFrame([person.dict()])

    # Predict test data
    predict = pipe.predict(df)

    return "No Churn" if predict[0] <= 0.5 else "Churn"
