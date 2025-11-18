## This base image below is prsent in docker itself.
FROM python:3.10-slim-buster 
## My working directory will be /app that basically means whatever working directory i wanted to create inside the docker that will be /app
WORKDIR /app 
## Then i will copy entire content in my current working directory inside this app folder.    
COPY . /app
## Then i will update by updating pip and installing aws cli(also we have to configure it)
RUN apt update -y && apt install awscli -y
## Again we are going to update and then install requirements.txt
RUN apt-get update && pip install -r requirements.txt
## The command is that i just need to run app.py
CMD ["python3","app.py"] 