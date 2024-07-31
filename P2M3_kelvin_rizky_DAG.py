'''
============================================================================================================================================================================================================
Customer Shopping Analysis Automation File

This program was created to automate the transformation and loading of data from PostgreSQL to ElasticSearch using Apache Airflow.
This data set is available in Kaggle data sets to be able to allowing them to create, practice, and learn from a dataset that mirrors real world customer shopping behavior.
============================================================================================================================================================================================================
'''



# Import Libraries
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2 as db
import re
import pandas as pd
from elasticsearch import Elasticsearch

# Default arguments for the DAG
default_args = {
    'owner': 'kelvin',
    # change the datetime for proceeding the automation accordingly
    'start_date': datetime(2024, 3, 23, 14, 13, 0) - timedelta(hours = 7),
    'catchup': False
}

# Function to fetch data from PostgreSQL
def fetch_data_from_postgres():
    """
    This function will Fetch data from a PostgreSQL database named 'airflow'. It reads the contents of the table 'table_m3' 
    and saves it as a CSV file named 'P2M3_kelvin_rizky_raw.csv' in the directory '/opt/airflow/dags'.

    """
    conn_string = "dbname='airflow' user='airflow' password='airflow' host='postgres' port=5432"
    conn = db.connect(conn_string)
    # Take data from the table
    df = pd.read_sql("SELECT * FROM table_m3", conn)
    df.to_csv('/opt/airflow/dags/P2M3_kelvin_rizky_raw.csv')
    conn.close()

# Function to cleaning data
def data_cleaning_task():
    """
    This function aims to perform data cleaning tasks on a CSV file located at '/opt/airflow/dags/P2M3_kelvin_rizky_raw.csv'. 
    It preprocesses column names, handles duplicate rows, and handles missing values. The cleaned data 
    is then saved as a new CSV file named 'P2M3_kelvin_rizky_clean.csv' in the same directory.

    """
    csv_file_path = '/opt/airflow/dags/P2M3_kelvin_rizky_raw.csv'
    dataset = pd.read_csv(csv_file_path)
    # Preprocess Column Name
    preprocess_col = []
    for col in dataset.columns:
        # Case Folding
        col = col.lower()

        # Mengganti '-' dan ' ' menjadi '_'
        col = re.sub(r'[-\s]', '_', col)

        # replace '(usd)' to ''
        col = col.replace('(usd)', '')
        
        # Remove white space
        col = col.rstrip('_')
        preprocess_col.append(col)

    dataset.columns = preprocess_col

    # Handle Duplicate
    if dataset.duplicated().sum() > 0:
        dataset.drop_duplicates(keep='last')

    # Handle missing value
    for col in dataset.columns:
        if dataset[col].isnull().sum() > 0:
            if col in dataset.select_dtypes(include='object').columns:
                dataset[col].fillna(dataset[col].mode())
            elif col in dataset.select_dtypes(include='number').columns:
                dataset[col].fillna(dataset[col].mean())

    # Save the cleaned data to CSV
    data_csv= dataset.to_csv('/opt/airflow/dags/P2M3_kelvin_rizky_clean.csv', index=False)
    
    return data_csv

# Function to transport dataset to elasticsearch
def transport_to_elasticsearch():
    """
    Transports data from a CSV file ('P2M3_kelvin_rizky_clean.csv') to Elasticsearch.
    It connects to an Elasticsearch instance hosted at 'elasticsearch', reads the CSV file,
    and indexes each row as a document in the 'milestone_3' index.
    """ 
    es = Elasticsearch(hosts='elasticsearch') 
    df=pd.read_csv('/opt/airflow/dags/P2M3_kelvin_rizky_clean.csv') 
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index="milestone_3", doc_type = "doc", body=doc)

# Define the DAG
with DAG(
    "project_m3",
    description='Project Milestone 3',
    schedule_interval='30 6 * * *',
    default_args=default_args,
    catchup=False
) as dag:
    
    # Task 1: Fetch data from PostgreSQL
    fetch_data = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data_from_postgres,
    )

    # Task for data cleaning
    data_cleaning = PythonOperator(
        task_id='data_cleaning_process',
        python_callable=data_cleaning_task,
    )

    # Task 3: Transport clean CSV into Elasticsearch
    post_to_elasticsearch = PythonOperator(
        task_id='send_to_elasticsearch_task',
        python_callable=transport_to_elasticsearch,
    )
# Define task dependencies
fetch_data >> data_cleaning >> post_to_elasticsearch