import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ## This will be our log file --> logging at different timestamps

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)    ## Where it should probably create the logs(the path) , a folder named "logs" has been used.
## os.getcwd() ---> to get the current working directory.
os.makedirs(logs_path,exist_ok=True) ## If it exists then not to be created again

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # We can also set logging.ERROR , since we also want all the information here we are using logging.INFO
)