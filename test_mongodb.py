from pymongo.mongo_client import MongoClient

## Note : Driver me select python ---> <db_password> this complete has to be replaced with ur original password in uri. This driver comes when u click Connect --> Drivers ---> Select Python
## Also : python -m pip install "pymongo[srv]"  This needs to be installed first (this is ur driver(for python) which u are installing)  ---> This is basically ur pymongo library.
## Also make ensure that ur current ip address must be added ---> This will come above ur mongo db database
uri = "mongodb+srv://amritanshubhardwaj12crosary:Admin123@cluster0.etgxyfj.mongodb.net/?appName=Cluster0" ## This u will get after clicking View Full Code Sample Option.
## Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successfull connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
## Next thing to be done is to update db_password(pymongo needs to be installed)
# How to create password --> go to security ---> database and network access ---> click edit and edit/create the passoword.
# Paste the created/updated password in the above URI in the place of db_password
## Check this code : python push_data.py --> Run in terminal