# AWS Automation Manager

A small learning project to practice AWS automation with **boto3**, packaged as a reusable Python module.

## Features

- List current EC2 instances and their Name tags
- List all S3 buckets
- Simulated EC2 start/stop actions (real calls commented out for safety)
- Simulated S3 file upload
- Logging of all actions to `aws_automation.log`
- Controlled entirely via environment variables (good for Docker / CI/CD)

## Project Structure

- `main.py` – Entry point, reads environment variables and triggers actions  
- `ec2_functions.py` – EC2 start/stop helpers  
- `s3_functions.py` – S3 upload helper  
- `utils.py` – Shared helpers (e.g. get instance Name tag, print resources)  
- `requirements.txt` – Python dependencies

## Run locally

```bash
pip install -r requirements.txt

AWS_DEFAULT_REGION=ap-southeast-2 \
INSTANCE_ID=i-0123456789abcdef0 \
START_INSTANCE=1 \
python -m automation_manager.main
```

## Notes

Real AWS actions (start/stop instance, upload file) are commented out to keep the project safe and portable.
Logs are written to aws_automation.log.