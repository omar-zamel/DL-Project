import os
import pandas as pd
import json
import time
import random
from google.cloud import bigquery

# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/HP/eloquent-theme-421216-94ba24fc204b.json'

# Create a BigQuery client
client = bigquery.Client()

# Define the dataset ID and table ID where you want to load the JSON data
dataset_id = 'python_test'
table_id = 'mm'
json_file_path = 'batch_data.json'

def generate_data():
    """
    Generate random JSON data for 100,000 records for 2 columns in each batch.

    :return: List of dictionaries containing generated data.
    """
    num_records = 100000  # Number of records to generate
    records = []
    for _ in range(num_records):
        record = {
            "Name": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)),  # Random name of length 5
            "Age": random.randint(20, 80)  # Random age between 20 and 80
        }
        records.append(record)
    return records

def write_to_json_file(data):
    """
    Write JSON data to a file.

    :param data: JSON data to be written to the file.
    """
    with open(json_file_path, 'w') as file:
        json.dump(data, file)

def load_json_to_bigquery():
    """
    Load JSON data from a file into BigQuery table.
    """
    # Load JSON data into BigQuery
    with open(json_file_path, 'rb') as source_file:
        job = client.load_table_from_json(
            json.loads(source_file.read().decode('utf-8')),
            f"{dataset_id}.{table_id}",
            job_config=bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
            ),
        )

    # Wait for the job to complete
    job.result()

    print(f"Loaded {job.output_rows} rows into {dataset_id}.{table_id}.")

# Run the process continuously
while True:
    # Generate random JSON data
    data = generate_data()

    # Write JSON data to a file
    write_to_json_file(data)

    # Load JSON data into BigQuery
    load_json_to_bigquery()

    # Wait for 1 minute before the next iteration
    time.sleep(10)  # Reduced sleep time for quicker demonstration
