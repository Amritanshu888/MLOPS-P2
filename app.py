## To trigger training_pipeline in pipeline folder
## This app.py should be our frontend
## Here i will be using FastAPI.  ---> Since FstAPI is going to be used we will need another library called as Uvicorn.

import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
## The above is the basic setup so that we can access it in the browser(to ensure that we can access it in the browser).

from fastapi.templating import Jinja2Templates ## This is responsible in picking up all the HTML files which are present inside this particular templates folder.
templates = Jinja2Templates(directory="./templates")

## Creating our Home Page in FastAPI
@app.get("/",tags=["authentication"]) ## This is the get request, tags will be authentication
async def index():
    return RedirectResponse(url="/docs") ## Then we used async def index : this will redirect to "/docs"
## This is the hardcoded thing that basically happens in FastAPI and through this u will be able to see probably every API's that
## are available in that FastAPI(generic API).

@app.get("/train") ## Whenever we have this URL "/train" it is basically going to train my entire training pipeline --> we need to probably initiate the training pipeline
async def train_route():
    try:
        ## Here i need to initiate my training pipeline
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline() ## Once we do this then the entire thing will start running
        return Response("Training is successfull")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
@app.post("/predict")
## So this function will be responsible in probably doing our prediction whenever i upload any new file(test.csv is a entire file in valid_data folder)
async def predict_route(request:Request,file:UploadFile=File(...)): ## With this UploadFile u can upload any type of file that u really want.
    try:
        df = pd.read_csv(file.file)
        #print(df)
        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor,model=final_model)
        print(df.iloc[0])
        y_pred = network_model.predict(df)  ## The same predict function which we have made in NetworkModel class (in this predict function firstly ur preprocessor will transform the new data and then it will go and predict and give u the final output)
        print(y_pred)
        df['predicted_column'] = y_pred ## Creating a new column
        print(df['predicted_column'])  ## Then printing the new column
        #df['predicted_column'].replace(-1,0)
        #return df.to_json()
        ## Then create another folder prediction_output (to store the predictions there)
        df.to_csv("prediction_output/output.csv") ## Passing the path where we want it to be saved --> u can save it anywhere like MongoDb(after converting to json) or S3 bucket.
        table_html = df.to_html(classes='table table-striped')
        #print(table_html)
        return templates.TemplateResponse("table.html", {"request":request, "table":table_html})
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)

    
## Giving the entry point to run this
if __name__ == "__main__":
    app_run(app,host="localhost",port=8000)    
    
## To run ETL pipeline from scratch : Run the push_data.py file ---> To get the recent fresh data.
# Run this file: python app.py --> in terminal  
# Inorder to run this we can use the uvicorn command : uvicorn app:app --reload
# Here the second app mentioned is the app name i.e. app and then --reload -> so that i don't have to refresh and reload each and every time.
# After u run this : It will open the URL ---> initially it will show nothing
# in front of url u have to give : /docs  --> u will get ur swagger ui and w.r.t this u will be able to see that i m able to get 1.Index Authentication 2.Next one is specifically w.r.t the train_route
## train_route one will be under default --> click on Try it out there u have to enter /train and then click execute --> then entire training will start again.
## In DagsHub MLflow ---> u will see two experiments each time u will run the training_pipeline the reason for this is that : one is for the training_data and one is for the testing_data.
## We can also go and compare experiments directly from the remote repository in DagsHub.
## Comparison button will be there when u open the experiments and there u will have : ur experiments select any two experiments and then comparison button will be enabled, click on compare and then u will be able to see the comaparison.

## Next u will do batch-prediction pipeline ---> See how we can do it from the frontend.
## Right now in swagger ui i just have two : "/ index" and "/train"  ---> one more will come i.e. "/batch_prediction".
## All these ("/","/train") are API's , u can execute them from the swagger ui.
## After creating "/batch-prediction" or can say "/predict" run the app again as said above(uvicorn app:app --reload) , ur /predict(predict_route api will be there) -> click try it out --> it will ask to choose the file --> choose test.csv and then click on execute.

## In app.py i should be able to read the entire templates folder so for that in FastAPI we use something called as jinja2 template.
