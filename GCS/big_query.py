import os
from google.cloud import bigquery
# Commit test
# anotrher test
# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/HP/eloquent-theme-421216-94ba24fc204b.json'

# Create a BigQuery client
client = bigquery.Client()

from google.cloud import bigquery

import os
from google.cloud import bigquery

# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/HP/eloquent-theme-421216-94ba24fc204b.json'

# Create a BigQuery client
client = bigquery.Client()

def list_datasets():
    """
    List datasets in BigQuery.
    """
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # List datasets
    datasets = list(client.list_datasets())

    if datasets:
        print("Datasets:")
        for dataset in datasets:
            print(f"\t{dataset.dataset_id}")
    else:
        print("No datasets found.")

def list_tables(dataset_id):
    """
    List tables in a given dataset.

    :param dataset_id: The ID of the dataset.
    """
    dataset = client.get_dataset(dataset_id)  # Make an API request.

    # View tables in dataset.
    tables = list(client.list_tables(dataset))  # Make an API request(s).
    if tables:
        for table in tables:
            print("\t{}".format(table.table_id))
    else:
        print("\tThis dataset does not contain any tables.")

def execute_query(query):
    """
    Execute a custom query in BigQuery for operations like deleting records.

    :param query: The SQL query to execute.
    """
    query_job = client.query(query)  # API request
    query_job.result()  # Waits for query to finish
    print("Query executed successfully.")


def retrieve_data(query):
    """
    Retrieve data from BigQuery using a custom query.

    :param query: The SQL query to execute.
    """
    query_job = client.query(query)  # API request
    rows = query_job.result()  # Waits for query to finish

    # Print the results
    for row in rows:
        for key, value in row.items():
            print(f"{key}: {value}")
        print()  # Add a blank line between rows


def create_dataset(dataset_id):
    """
    Create a dataset in BigQuery.

    :param dataset_id: The ID of the dataset to be created.
    """
    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_id)

    # Specify the geographic location where the dataset should reside.
    dataset.location = "US"

    # Send the dataset to the API for creation, with an explicit timeout.
    # Raises google.api_core.exceptions.Conflict if the Dataset already
    # exists within the project.
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
    print("Created dataset {}".format(dataset_id))


def create_table(table_id):
    """
    Create a table in BigQuery.

    :param table_id: The ID of the table to be created.
    """
    table = bigquery.Table(table_id)

    # Specify schema autodetection
    table.schema = []

    # Create the table with schema autodetection
    table = client.create_table(table)  # Make an API request.
    print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))


def extract_schema(project, dataset_id, table_id):
    """
    the extraction of schema fields from a table in BigQuery.

    :param project: The project ID.
    :param dataset_id: The dataset ID.
    :param table_id: The table ID.
    """
    dataset_ref = client.dataset(dataset_id, project=project)
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)  # API Request

    # View table schema fields
    print("Schema fields:")
    for field in table.schema:
        print(f"\tName: {field.name}, Type: {field.field_type}, Mode: {field.mode}")




def create_external_table(table_id, source_uri):
    """
    Create an external table in BigQuery.

    :param table_id: The ID of the table to be created.
    :param source_uri: The URI of the external data source.
    """
    client = bigquery.Client()

    external_config = bigquery.ExternalConfig("CSV")
    external_config.source_uris = [source_uri]
    external_config.autodetect = True

    table = bigquery.Table(table_id)
    table.external_data_configuration = external_config
    table = client.create_table(table)

    print("Created table with external source format CSV and schema autodetection")



def add_column_to_table(table_id, column_name, column_type):
    """
    Add a new column to an existing table in BigQuery.

    :param table_id: The ID of the table.
    :param column_name: The name of the new column.
    :param column_type: The data type of the new column.
    """
    table = client.get_table(table_id)  # Make an API request.
    original_schema = table.schema
    new_schema = original_schema[:]  # Creates a copy of the schema.
    new_schema.append(bigquery.SchemaField(column_name, column_type))
    table.schema = new_schema
    table = client.update_table(table, ["schema"])  # Make an API request.

    if len(table.schema) == len(original_schema) + 1 == len(new_schema):
        print("A new column has been added.")
    else:
        print("The column has not been added.")



# Example usage:

#list_datasets()
#list_tables("eloquent-theme-421216.Batch_Watches_Dataset")
#custom_query = 'SELECT * FROM `eloquent-theme-421216.Watches_Dataset.rollex_data` ORDER BY Datetime DESC LIMIT 5'
#retrieve_data(custom_query)
#project = 'eloquent-theme-421216'
#dataset_id = 'Batch_Watches_Dataset'
#table_id = 'Batch_Stream_Watches'
#extract_schema(project, dataset_id, table_id)
#create_dataset("eloquent-theme-421216.python_test_from_vs")
#create_table("eloquent-theme-421216.python_test_from_vs.vs_rollex_test")
#table_id = "eloquent-theme-421216.python_test_from_vs.vs_watches"
#source_uri = "gs://rollexdata/watches.csv"
#create_external_table(table_id, source_uri)
#add_column_to_table("eloquent-theme-421216.python_test_from_vs.vs_rollex_test", "phone", "STRING")
#execute_query("DELETE FROM `eloquent-theme-421216.python_test.mm` WHERE True")