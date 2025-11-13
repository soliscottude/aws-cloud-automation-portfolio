import os
import logging
from botocore.exceptions import ClientError


def upload_file(s3, file_path: str, bucket_name: str, object_key: str | None = None):
    try:
        if object_key is None:
            object_key = os.path.basename(file_path)

        logging.info(
            f"(Simulation) Uploading file: {file_path} → s3://{bucket_name}/{object_key}"
        )

        print(f"(Simulation) Uploaded: {file_path} → s3://{bucket_name}/{object_key}")

    except ClientError as e:
        logging.error(
            f"Upload failed: local={file_path}, bucket={bucket_name}, key={object_key}, error={e}"
        )
        print(f"Upload failed: {e}")
