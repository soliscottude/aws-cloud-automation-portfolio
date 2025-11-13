import os
import logging
import boto3

from .utils import print_current_resources
from .ec2_functions import start_instance, stop_instance
from .s3_functions import upload_file

# Logging
logging.basicConfig(
    filename="aws_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# AWS session
session = boto3.session.Session(
    region_name=os.getenv("AWS_DEFAULT_REGION", "ap-southeast-2")
)
ec2 = session.resource("ec2")
s3 = session.resource("s3")


if __name__ == "__main__":
    print_current_resources(ec2, s3)

    instance_id = os.getenv("INSTANCE_ID")
    bucket_name = os.getenv("BUCKET_NAME")
    file_path = os.getenv("FILE_PATH")

    start_flag = os.getenv("START_INSTANCE") == "1"
    stop_flag = os.getenv("STOP_INSTANCE") == "1"
    upload_flag = os.getenv("UPLOAD_FILE") == "1"

    # EC2 Start
    if instance_id and start_flag:
        print(f"[INFO] (Simulation) Starting EC2: {instance_id}")
        start_instance(ec2, instance_id)

    # EC2 Stop
    if instance_id and stop_flag:
        print(f"[INFO] (Simulation) Stopping EC2: {instance_id}")
        stop_instance(ec2, instance_id)

    # S3 Upload
    if bucket_name and file_path and upload_flag:
        print(f"[INFO] (Simulation) Uploading file → {bucket_name}")
        upload_file(s3, file_path, bucket_name)

    if not any([start_flag, stop_flag, upload_flag]):
        print("No operations requested. Set env variables to trigger actions.")

    print("AWS actions executed in simulation mode for safety.")
