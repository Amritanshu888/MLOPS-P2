import os
import sys
import json

from dotenv import load_dotenv ## So that i can call all the enviroment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi  ## This certifi is a python package that provides a set of root certificates , commonly used by python libraries that needs to probably make a secure HTTP connection.
ca=certifi.where() ## Right now we are trying to make a HTTP connection to my MongoDB database. This is also used to make ensure that they trust only these certificates verified by the trusted certified authorities.

## Whenever we try to communicate with MongoDB and certifi library has been imported then it knows that it is a valid request being made.
## certifi.where() ---> this line retrieves the path to the bundle of ca certificates provided by certifi and stores it in a variable ca.
## ca ---> Certificate Authority(Trusted certificate authorities usually done for SSL , TSL connections to verify that server u are connecting to has a trusted certificate)

import pandas as pd
import numpy as np
import pymongo
## We also need to implement logging and exception
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

## This will be our ETL pipeline
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    ## Read the data and convert to json format
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            ## Here the data automatically has an index we need to drop that index as we are loading inside our MongoDB database so no need of the index.
            data.reset_index(drop=True,inplace=True)
            # Then we will convert to records
            records = list(json.loads(data.T.to_json()).values()) ## .values() --> It will look like arrays of json , T -> Transpose
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        ## Above word for : What happens if the file path is not found

    def insert_data_mongodb(self,records,database,collection):
        ## collection in mongodb is just like tables
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL) ## Library for python to connect with MongoDb 
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
## Starting Our Execution of the ETL Pipeline
if __name__ == '__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "SHUBHAMAI"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)

            