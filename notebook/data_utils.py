import boto3
import tarfile
from io import BytesIO

def download_tar_from_s3(bucket_name, file_key):
    s3_client = boto3.client('s3')
    try:
        # Download the file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        data = response['Body'].read()
        print("Downloaded file from S3 successfully.")
        return data
    except Exception as e:
        print(f"Error downloading from S3: {e}")
        return None

def extract_tar_to_disk(data, extract_to="."):
    try:
        with tarfile.open(fileobj=BytesIO(data), mode="r:gz") as tar:
            tar.extractall(path=extract_to)
        print("Extraction to disk successful.")
    except tarfile.TarError as e:
        print(f"Extraction failed: {e}")

def get_data():
    bucket_name = "seyeddata"
    file_key = "data.tar.gz"
    extract_to = "."

    # Step 1: Download the data from S3 and keep it in memory
    data = download_tar_from_s3(bucket_name, file_key)

    # Step 2: Extract the data from memory to disk
    if data:
        extract_tar_to_disk(data, extract_to)
