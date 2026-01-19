- .github/workflows folder so that further we will be focusing on deployment for which we will be using github-actions.
- main.yml is basically for writing github actions so that we will proceed with the deployment and all.
- Network_Data folder --> inside this i will upload my dataset.
- Inside network security i m going to create my entire project structure.
- Inside network security __init__.py file we will create bcoz i need to consider this entire folder --> networksecurity as a package.
- This is why we use this __init__.py file.
- Any constants that u will be defining will be in the constants folder.
- The reason to create folder structure in networksecurity is to consider this like a package.
- Pipeline folder for training and batch prediction pipeline.
- utils folder -> any generic code that u specifically want to apply for the entire project u can create here in utils folder.
- cloud --> this folder is for writing any information related to the cloud or functionalities realted to the cloud.
- in all these folders we will go and try to create our .py files.
- Dockerfile ---> to create docker image for all these files.
- setup.py file ---> i will be writing some code which will be packaging this entire content itself.

## Create github repository for this project then do the following commands
- echo "# networksecurity" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Amritanshu160/networksecurity.git
- git push -u origin main

- After git init ur notebooks folder will not be getting tracked initially bcoz its a empty folder.
- git init
- then : git add .  ---> it will take all the files currently here and will store it in the local repository.
- then : git commit -m "Project structure set up"
- Inside networksecurity not all folders will be added bcoz these are empty folders.
- Then create main branch : git branch -M main
- Then add remote repository : git remote add origin https://github.com/Amritanshu160/networksecurity.git  ---> repository link where we want to commit and push the code.
- Then : git push -u origin main -----> origin is our (from where its going) , and main is (where it needs to go) i.e. our main branch.

- As soon as u create files inside the folders present in networksecurity folder ur folders will start getting tracked --> U sign will be there ---> U means untracked here.
- Inside each and every folder in networksecurity we will add __init__.py file --> Why ?? ---> Bcoz it will treat the entire folder(the folder in which __init__.py file is present) as a package. 

- After adding files in folders inside the networksecurity folder when u do : git add . ---> All the files will be in added mode.
- then : git commit -m "The Message"
- then : git push origin main

- Now when u reload at github and go inside network security u will see the folders there.

## Note:
- If u do : git add . ----> all files checked
- if u do : git add filename ----> then only that particular file will be added.

- First we will create logger.py
- Then we created exception.py

- Running exception.py file:
- cd networksecurity
- then cd exception
- then: python exception.py
- If the above fails , directly run from the root : python -m networksecurity.exception.exception
- Run this in the exactly fresh terminal
- Note: Parent folder me wapas jaane ke liye do : - cd.. then again cd.. , as we earlier did two time cd to go inside exception folder and to execute exception.py file.

## Generic Project Structure
- MongoDB Database ----> (Data Ingestion Config->Data Ingestion Component->Data Ingestion Artifacts) ---> (Data Validation Config->Data Validation Component->Data Validation Artifacts) ---> (Data Transformation Config->Data Transformation Component->Data Transformation Artifacts) --->
(Model Trainer Config->Model Trainer Component->Model Trainer Artifacts) ---> (Model Evaluation Config->Model Evaluation Component->Model Evaluation Artifacts) ---> (Model Pusher Config->Model Pusher Component->Model Pusher Artifacts)   ------> Then Finally Push our model into the cloud(it can be Azure, AWS etc.)

## How the Data will be coming in the MongoDB database ??
- Here we need to understand something called as ETL Pipeline.
- Extract,Transform and Load ---> 3 components make up the entire ETL pipeline
- 3 important things in an ETL : 1.Source 2.Destination and between these two we have a step called as Transformation.
- Here dataset is present in local -> Take the dataset --> Do basic preprocessing(Cleaning Raw Data,Transformation Process(Converting to some other format like json etc.))  ----> Then after preprocessing we will save it in some destination.
- Here our source is our local from where we are reading our csv file ----> Then we will do preprocessing(where we will convert this into the json format) ---> Then we will save this in some destination database. In this scenario my destination database is nothing but its MongoDB.
- This is how data comes in our MongoDB database.
- Why is ETL important ??
- Bcoz in real world problems this data will be coming from various sources and not just one source. In real world scenarios : My data will be coming from API's , S3 bukcet , Paid API's and some other multiple sources(like companies internal data).
- So we combine all these data ----> Do transformation(Convert this into a json) ---> Then store it in Final Destination(Some Databse like MongoDb or AWS Dynamo DB, can be different databases).

- NOTE: MongoDB will be in Atlas Cloud.

## MongoDB Atlas
- Search for MongoDB atlas ---> create a free account.
- Sign Up with Google.
- There in ur profile page u will see clusters ---> A cluster named Cluster 0 will be there which will be paused , click on resume to resume ur cluster (this is a free cluster). It will then show that ur cluster is being created.
- Once ur cluster will be created click on connect to connect with the cluster , then choose Drivers , in version choose python 3.6 or later. Note that pymongo needs to be installed. After all this click done.
- After creating and connecting a cluster in the Choose a Connection Method page u will be able to see a option of : View Full Code Sample
this is just to check whether my connection is working or not(pymongo library required -> helps u to connect with MongoDB itself).
- In view full code sample ur uri will be there which will be ur MongoDB cluster connection.
- Create a file to push data to MongoDB database : push_data.py

## Data Ingestion
- In data ingestion we read the data from our MongoDB database. We read this data --> it can be used for training our model.
- We require here data ingestion config ---> it is nothing but these are soem basic informations like where my dataset needs to get stored, many steps that we can perform like we are doing feature engineering , convert data to train and test.
- Data Ingestion Config contains info like : - Data Ingestion Dir - Feature Store File Path - Training File Path - Testing File Path - Train Test Split Ratio - Collection Name
- Since we are exporting data from MongoDB it needs to be converted into a Raw CSV file. It should be stored like test.csv , train.csv.
- After we get our data we will do some feature engineering.
- Then split the data into train and test , Then give the data into Data Ingestion Artifact where then it will store the file as Train.csv and Test.csv

## Data Validation Component
- The artifact created in the data ingestion component is passed to the Data Validation component
- We will create data validation config --> we will have all the necessary path informations
- When we read data from MongoDB most important thing is that my data schema should not be changed.
- Schema means feature names ,number of features should not be changed , also if a feature is following a normal distribution and then it starts following some other distrbution then that is called data drift----> this should not happen. If data drift happens then that same data cannot be used by our model for training bcoz then there will be huge difference.
- Data Distribution changes with time  ---> Hence we should probably go and create data drift report.

- Our dataset should have the same schema : i.e. same no. of columns, same no. of features, distribution should also be same.
- 2nd thing we will be checking is the Data Drift  ---> Just to check whether the distribution of the data is same or not when we compare it with training the data (data we have used for training our model) and the new data that we specifically get.
- 3rd : Validate no. of columns , Whether numerical columns exist or not and many more checks.
- Basic Info Required in Data Validation Config : - Data Validation Dir - Valid Data Dir - Invalid Data Dir - Valid Train File Path - Invalid Train File Path - Invalid Test File Path - Drift Report File Path.

- Next we will initate the Data Validation ---> From the Data Ingestion Artifact , from the ingested folder we are going to read the train, test csv. Data Ingestion Artifact is given as a input to Data Validation(Folder named ingested --- Which contains Train.csv and Test.csv)
- Next step : Validate no. of columns ---> Train and Test data both should have same no. of columns.
- The above will give us a status : Whether True or False  ---> Columns and missing or not.
- Another check : Whether numerical column exist or not w.r.t our training data and test data  ---> Here also we will get a status.
- Next step : Detect Data Drift ---> To check whether distribution of Data is changing or not.
- How to check the above(Dataset drift) ?? ---> There is a mathematical way. ---> Here also we will get status , whether True or False.
- Data Validation Component will return : Validation Status, Valid Train File Path, Valid Test File Path, Invalid Train File Path, Invalid Test File Path, Drift Report File Path.
- All these will be in Data Validation Artifact Folder , along with report_yaml.

## Data Transformation
- Step 1 : Create our Data Transformation Config, there we will be having all this information : - Data Validation Dir - Valid Data Dir - Invalid Data Dir - Valid Train File PAth - Invalid Train File Path - Invalid Test File Path - Drift Report File Path
- The above information is coming from Data Validation Artifact from the previous stage.
- Step 2 : Initiate the Data Transformation --> We go to the Data Validation Artifact --> Then we go ahead and read all this train and test data. Once we read then we go ahead with data transformation step.
- Step 3 : Data Transformation : First we will take our train dataframe from which i will be dropping my target column --> From this we will get input features train dataframe and output feature train dataframe , we can combine input feature train dataframe and then we will get Input Feature Train Array
- Next we will be using SMOTETokmek --> If in ur dataset u have imbalance dataset then u can probably balance it with the help of SMOTETomek. In our project not required -> Bcoz our dataset is already balanced.
- SMOTETomek is one feature engineering process.
- Training data me se we will remove Nan values for this we will use imputer techniques(KNN imputer).
- Main Aim: Create a pipeline.
- After this we will get a processor object(preprocessing.pkl) we will apply it on test data.
- preprocessing.pkl file we will save it , we will create a folder called as DataTransformation inside Artifacts folder.

## SMOTETomek
- Feature engineering --> Imbalance data
- First i will apply this to my Input Feature Train Final , Target Feature Train Final , Input Feature Test Final , Target Feature Test Final
- Concat them to form train and test array.
- And then we will convert this to a numpy arrays. (train.npy,test.npy) --> Output will be nothing but artifact file in the form of numpy array. Array in form of numpy array --> .npy (numpy array format). --> this will be my transformed data.
- Then Finally this will be my Data Transformation Artifact.

- Note: For train we use fit_transform and for test we use transform(so that we don't have an data leakage problem).


## Model Trainer
- In Model Trainer component the input of data transformation artifact is also provided.
- Then we need to give input w.r.t the model trainer config(it includes details like: model trainer dir, trained model file path, expected accuracy, model config file path). These info will be here.
- Output of model trainer component is nothing but model trainer artifact.
- Here we will try to create model.pkl file.

## Architecture
- model trainer dir : Its the location where i will be saving my model.
- trained model file path : Entire model file path where we really want to save.
- expected accuracy
- model config file path : If i have any info regarding model config i will be putting it over here.

- After this we initiate the model training , then load the numpy array data(this we will take from the data transformation artifact).
- We will do split for train and test.
- Train our model w.r.t training data.
- Try multiple models.
- Take the best model(its details) -> will try to compare its score. Find out the best model and the best score, then convert it to the pkl file.
- Calculate metrics will be used to find out the best metrics.
- preprocessing.pkl file we will also be getting from my Data Transformation artifact, we will load it and combine them.

## MLFlow Tracking with Remote Repository DagsHub
- Click on create --> there choose a repository to connect with(in the option of connect with github).
- On ur repo click remote --> there u will have access to codes in the experiment section(for mlflow).
- Add that code in model_trainer.py file.
- import dagshub
- dagshub.init(repo_owner='amritanshubhardwaj12crosary', repo_name='networksecurity', mlflow=True)
- Bcoz of this it knows where we need to create our mlruns folder , or which remote repository it needs to track our entire data.
- This time when u runs this ur mlruns folder will not be created in ur local machine.
- Run the script : python main.py

- Why we did this ??
- This will allow us to share this URL to anyone --> i.e. allowing anyone to track this experiment/metrics.


- If u take a paid account of Dagshub then in ur team u can probably share the entire reports of the performance metrics or anything that u really want.
- This is what Dagshub helps in its a remote repository, with the help of this remote repository u will be able to just give the URL , and people will be able to just check it out. --> Hence Collaboratively u will be able to work in a team.
- Whatever commit and tracking u are doing here u are not doing it in a local , even though mlflow runs in local , tracking we are doing in a remote repository which can probably be shared with everyone.

- In ur repo in DagsHub on the top u will have header experiments where u will be able to see ur experiments.

## Model Pusher Implementation
- Note: model.pkl in artifacts will be the best model that u will specifically get.
- And we also have preprocessing.pkl file in transformed_object , this also we need.
- I need to take both of this pickle file and push it in one common folder from which i m actually going to do the prediction.
- Create the folder final_models

- For this we have made following changes:
- In model_trainer.py we have added the line : save_object("final_model/model.pkl",best_model)
- In data_transformation.py we have added the line: save_object("final_model/preprocessor.pkl", preprocessor_object)

- This is just like a model pusher, i m pushing this in one source and from there i can go and put it in s3 bucket or any other final cloud platform that i want.

- run: python main.py ---> In terminal

- This will just be like a model pusher : where in i m pushing this inside this particular folder.

- Note: main.py file is just like ur training_pipeline which is running each and every thing and creating ur artifacts.

## Pipeline
- In pipeline we create training_pipeline.py ----> To trigger this training pipeline we create an app i.e. app.py

- Note : In templates folder we are using table.html ---> the reason for this is that whatever output im getting i will display it in this particular html itself.
- This html is just like ur frontend application wherein we are just going to display all the details w.r.t our predicted data.
- We have also created a folder valid_data which will have test.csv which contains our test data(on which model has to be tested).
- test.csv only contains our independent features and no dependent feature(output feature) bcoz this has to be predicted by our model.

## Note
- preprocessing.pkl file if the file size is small we can push it in github and if its large we can push it in some s3 bucket.

## Notes
- If the model size is too big its not the good way to store it in the local folder(in form of pickle file).
- Here we should look for some cloud platform like AWS S3 Bucket.
- This model can be of any size hence it needs to be deployed in the AWS S3 bucket.
- This entire folder we will sync it with the cloud so that we also have various versions of this particular model bcoz we will be keep on continiuously training our data models with various different kinds of data. So we also need to have different different versions of data itself.
- So now we will sync this folder(final_model) to our AWS S3 cloud platform wherein we will also have this replica of this particular model itself and we will also be doing versioning for them.
- Now in training pipeline we will create two differnt functions: 1. sync_artifact_dir_to_s3(whatever my artifact folder is created i will also upload that into the s3 bucket ---> bcoz in artifacts folder i have the artifact of each and every modules : data_ingestion -> data_transformation -> model_trainer -> model evaluation , so we need to save that also in S3 bucket.)

- 2nd function: sync_saved_model_dir_to_s3 : To put our final_model in the S3 bucket(with versioning).
- Create a file s3_syncer.py inside the cloud folder.

## AWS
- AWS -> AWS S3 -> Buckets -> Ur networksecurity bucket -> their we will have artifact folder which will contain all the artifact details.
- Artifact details like data_ingestion, data_transformation, data_validation, model_trainer , these u will be able to get with different different timestamps.
- Steps:
- Download the AWS cli.(AWS Command Line Interface) -> Search AWS CLi windows installer.
- After Installation: In command prompt
- aws -> in cmd
- then : aws help ---> u will then see all options i.e. ur aws is working properly.

- Go to ur AWS account : Create IAM user -> click IAM , then in resources click on users(no. will be there denoting no. of users) --> then click create new user ---> give new user name : i.e. testsecurity --> click next --> In set permissions click on Attach Policies directly(it will attach any policies that u are specifically using like s3 bucket etc.) --> In permissions policies click on Administrator Access(giving the access)(In companies only specific access(whatever things u are using) only that will be given to u --> here administrator access bcoz u are the account owner) --> click next --> on next page click create user.

- Once u create the user click on it there u go to Security Credentials --> Then go to access keys click on create access key then in use case select command line interface, enable the confirmation , then next ---> on the next page u will have Set Description Tag option (if u want to give, give it otherwise okay).then click Create Access Key --> on next page u will get ur access key (Access key and ur secret access key).

- Now we have to set the access key and secret accesss key :
- Open Terminal
- Then command: aws configure
- Then it will ask for AWS Access Key ID: Give the access key here(copy and paste) then press enter
- Then it will ask for AWS Secret Access Key: Give the access key here(copy and paste) then press enter
- Then by default it will take us-east-1 region and default output format is json.
- So now u have configured.


- So now u will run ur training_pipeline to see that whether we are able to put our model in AWS S3 bucket or not.
- Run the code : uvicorn app:app --reload

- In AWS search for S3 bucket(u have to create the bucket) --> Click on Create bucket --> A general confirmation page will be there(make ensure that ur AWS region is us-east-1) , in bucket type select General Purpose , give the bucket name and click on Create Bucket. Make ensure one more thing the bucket name which u are giving here should match the name u have given in the code(AWS_BUCKET_URL me jo training bucket name hai) - in our case TRAINING_BUCKET_NAME is networksecurity , so here also u will give networksecurity as bucket name.

- Once we run , in our networksecurity bucket we will have two folders: artifacts and final_model, inside the artifacts and final_model i will have my versions(as per i execute the code).

- To run : uvicorn app:app --reload
- Then in swagger ui in train_route click try it out and then execute.
- Now the entire artifacts folder which contains logs with timestamps and final_model will be passed to the s3 bucket which u have created.

- Note: The artifact folder which is getting saved is for each and every stage.

## Building Docker Image and Github Actions
- Here we will talk abt deployment with AWS(we will use something called as AWS EC2 instance) --> mechanism of entire deployment we will try to follow a standard procedure(what we use in industries).
- Let's say i have my end to end project NetworkSecurity , next step -> Convert this entire application into a docker image.
- How to convert ?? ---> We really need to write a docker file.
- Once we convert it into a docker image we need to deploy this Docker image somewhere else. Like we want to deploy this docker image into a docker hub and in docker hub u can deploy it as a public or private repository. In our case we will be using AWS ECR. AWS ECR repo is nothing but just like a u can deploy ur own private image in the AWS cloud itself.
- Why using AWS ECR instead of Docker Hub ??
- Docker Hub u will need a paid account to deploy ur private docker image itself and similarily in the case of AWS ECR what we do is that if i really want to deploy a private image specifically in the AWS cloud i can use AWS ECR.
- Entire docker image will be deployed in AWS ECR so here u will be getting the entire docker image itself and after we deploy this we will take this entire docker image and deploy it in our AWS EC2 instance.
- This is the standard procedure that we follow whenever we have to deploy our end to end project.

- This entire process: Fron Application ---> Creating a docker image ---> deploying it to aws ecr ---> then taking this entire docker image and deploying it as a container in AWS EC2 we will be using something called as Github-Actions.
- This is where ur github actions will be very important bcoz here u really need to create a CI-CD pipeline.
- Without CI/CD u cannot do this in a Automated way.
- Another thing we will be doing in Github Actions is that we will be creating our own app runner, this app runner will be responsible in listening any kind of triggers that happens in the Github Repository and this will further take docker image into the ECR or from AWS ECR it will take to the AWS EC2 instance and deploy it as a container. This is the standard procedure that we are going to follow.
- AWS EC2 instance we can do a lot of configurations over here. Hence quest

- Process: Firstly i will see how to create a docker image, then we will go ahead and create simple github-actions yaml file, then we will see how we can go and create a app runner, deploy our docker image into AWS ECR and then run this docker image as a container in AWS EC2 instance.


## Note:
- B4 i was using uvicorn to run my file but inside this app.py we are using app_run() --> Once we use this what it does is that this app_run is coming from uvicorn itself , if i write in terminal python app.py it is going to use uvicorn only to run this entire page.
- U can run in two ways: by using uvicorn directly or directly running it(by using python app.py).
- We are directly using app.py , hence in docker command also u can see we are running app.py directly only.

- Next we will go to github workflows --> .github->workflows->main.yml file.
- Here we will configure for our github actions.

- After writing github-actions(.github->workflows->main.yml) we just have to commit the code.

- After this u can visit ur particular repository at github and go to github actions for what particular repo , there u will have on top ur recent worklflows named "Deployment Changes" --> this is the same name on which u commited ur code if u would have used some other name in ur github commit command then that name would have appeared.
- Click on that workflow there u will have ur job named : "Continious Integration" (the name which u have given in ur main.yml file in .github->workflows->main.yml)
- Click on that job and u will be able to see the entire stages of execution of that job.
- U can write any unit test cases and compare it.

## Building the Docker Image
- Now we are going to build this docker image, we are going to write something in the github actions which is automatically going to do this docker image build and then it should probably deploy this in AWS ECR instance(2nd step).
- Whenever i m trying to work with ECR i will make ensure that i will create a private docker image.

- Go to your AWS account Home Page , search for ECR and create ur ECR repository(ECR is nothing but Elastic Container Regisrtry). It is a full managed docker container registry which allows u to share and deploy container.
- Click : Create Repository.
- There on next page it will be : Create private repository, in general settings give the repository name and then click create.
- Ur repository will be created(private repo). When u go inside ur repo initially there are no images to display , with ur repository u will have ur URI copy it.

- Setup github secrets:
- AWS_ACCESS_KEY_ID = 
- AWS_SECRET_ACCESS_KEY = 
- AWS_REGION = us-east-1
- AWS_ECR_LOGIN_URI = "Here ur copied uri will be there" --> This entire thing needs to be setuped in github actions.
- ECR_REPOSITORY_NAME = networksecurity (ur repo name which u gave at earlier stages).
- These two informations: AWS_ECR_LOGIN_URI and ECR_REPOSITORY_NAME i will be adding as a secret variable inside my github actions.
- Note: U can also create public repository.

- We have to update our main.yml file for building the dockers along with this we need to push the image into the ECR.
- So i will create another job just like how we created for integration.

## Creating AWS EC2 Instance
- Search for EC2 instance, click on it , first step : setup my EC2 instance. Right now if u will click on instances it will show 0 instances running. Click Launch Instance --> There enter the name of the instance that u want --> in name enter : networksecurity , under quick start select ubuntu.
- When u scroll below it will ask u to enter instance type : Choose type as : t2.medium , then u have key-pair login(no need to create).
- Under network settings: Enable all Allow SSH traffic , Allow HTTPS traffic , Allow HTTP traffic from internet.
- Then in configure storage i have 8 GB RAM --> click launch an instance --> there a dialog box will appear , select Proceed without Key Pair and click Launch Instance.
- Creating Key-Pair is not compulsory its upto u. In key pair u can click Create new key pair --> enter key pair name , then also u can launch the instance.
- Then in instances u will be able to see ur instance.
- Click on the instance id , then on top right u have connect click on that : Now there are various ways of connecting to ur instance , choose EC2 instance connect and then move on , in connection type select Connect using EC2 instance Connect and then finally click on "Connect".
- Once i click connect it will open a command prompt like of thing.
- There are some pre-requisite installation that everybody needs to run and that is basically doing some basic setups.

## Docker Setup In EC2 commands to be Executed

# Optional
- sudo apt-get update -y    ---> Pre-requisites that u need to install in EC2 instance
- sudo apt-get upgrade

# Required
- curl -fsSL https://get.docker.com -o get-docker.sh  --> i need to go and install the docker(for this we will use this curl command) , this step u need to do for the first time and later u don't have to do it.
- sudo sh get-docker.sh   --> to provide permissions
- sudo usermod -aG docker ubuntu    --> setting up the sudo mode
- newgrp docker    ---> creating a newgrp docker 

- Once this is done go back to ur github repository --> go to setting ---> Actions --> There u have something called as Runners(we are going to create runners) --> click on New self-hosted runner(this will be responsible in listening any kind of events that are happening in the github repository(like push,pull merge))
- There we click on linux , under that we have commands(Download,Configure) we have to run all these commands(in the AWS EC2 terminal where u ran above commands).
- When u execute the commands it will authenticate and connect with the github actions.
- While executing commands in terminal it will ask u to give the name of the runner : U have to give self-hosted.
- Once we configure it will start listening for jobs.
- Now when we go back and click on runners u will see that : there is something called as self-hosted and it is in idle state(basically it is now listening).
- Now whatever EC2 configuration i have written in main.yml file in .github/workflows/main.yml i will push it(like now we push normally).(Now that app runner is going to listen)


- Apne instance me public IPv4 Dns address ko open karo --> we know this is working in 8080 , address ke aage :8080/docs lgao.

- Go to your instance , then go to security there we have security groups click on it , inside security groups go to in-bound rules here i need to edit the inbound rules , in edit inbound rules click add , select type as Custom TCP, Port range give it as : 8080(docker run port ko expose kar rhe hai so that we can access the URL) , then enter : 0.0.0.0/0 request will be from every URL. Source u have to keep it as Anywhere. Then click save rules.
- Once we save this rule again we can go to our EC2 instance. From there inside ur EC2 instance copy ur Public IPv4 address, copy it open another browser there enter it there , then give :8080(in front of it) and then press enter.
- It will open : Swagger UI where u will be getting two API's , train and predict.
- Execute the API's like we have done before.
