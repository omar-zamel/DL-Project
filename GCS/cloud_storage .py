import os
from google.cloud import storage
import numpy as np

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/HP/eloquent-theme-421216-94ba24fc204b.json'

def list_all_buckets():
    """List all buckets."""
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    if buckets:
        print("Buckets:")
        for bucket in buckets:
            print(f"\t{bucket.name}")
    else:
        print("No buckets found.")

def create_bucket(bucket_name, storage_class='STANDARD', location='us-central1'):
    """Create a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
    bucket = storage_client.create_bucket(bucket, location=location)
    return f'Bucket {bucket.name} successfully created.'

def upload_blob(bucket_name, source_file_path, destination_blob_name):
    """Upload a file to the specified bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path, timeout=120)
    return True

def list_files_in_bucket(bucket_name):
    """List files in the specified bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    files = [blob.name for blob in bucket.list_blobs()]
    
    print(f"Files in Bucket '{bucket_name}':")
    if files:
        for file in files:
            print(f"  - {file}")
    else:
        print("  No files found.")

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Download a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    return True

def delete_files_in_bucket(bucket_name):
    """Delete files inside a bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        blob.delete()
    print(f"All objects in Bucket '{bucket_name}' deleted successfully.")

def delete_bucket(bucket_name):
    """Delete a bucket (must be empty)."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.delete(force=True)
    print(f"Bucket '{bucket_name}' deleted successfully.")

# Example usage:
#list_all_buckets()
#print(create_bucket('new_bucket_created6544'))
#print(upload_blob('new_bucket_created6544', 'C:/Users/HP/combined_roi_plot.png', 'combined_roi_plot.png'))
#print(list_files_in_bucket('new_bucket_created111'))
#print(download_blob('new_bucket_created6544', 'combined_roi_plot.png', 'C:/Cloud_data/combined_roi_plot.png'))
#delete_files_in_bucket('new_bucket_created6544')
#delete_bucket('new_bucket_created6544')
