## This file is responsible in syncing with the aws s3 bucket so u need to create this file inside the cloud folder.
## folder --> is the folder in local and aws_bucket_url --> is the cloud folder in the s3 bucket
import os

class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        commnad = f"aws s3 sync {folder} {aws_bucket_url}" ## Here we are creating a command to sync ur local folder to s3 , we are creating a command and with the help of aws-cli if the cli is installed
        os.system(commnad)  ## Our python script will run this command using this
    
    ## U can also get details from s3 back to the local folder
    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder}" ## Here in command we need to first give our aws_bucket_url and then folder
        os.system(command)    ## This is to execute the above command
