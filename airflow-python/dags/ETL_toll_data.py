# Import libraries
import csv
import os
import tarfile
import requests
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd

# ============ FUNCTIONS ============

def download_dataset(url, destination):
    """
    Downloads a dataset from the specified URL to the destination path.
    
    Args:
        url (str): URL of the dataset to download.
        destination (str): Path where the file will be saved.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination, 'wb') as f:
            f.write(response.content)
        print(f"Dataset downloaded successfully to {destination}")
    except Exception as e:
        print(f"Error downloading dataset: {e}")


def unzip_tolldata(source, destination):
    """
    Extracts the contents of the source dataset .tgz file to the specified
    destination directory.

    Args:
        source (str): Path to the source .tgz file.
        destination (str): Directory where the contents will be extracted.
    """
    try:
        with tarfile.open(source, "r:gz") as tgz:
            tgz.extractall(destination)
        print(f"Dataset extracted successfully to {destination}")
    except Exception as e:
        print(f"Error extracting {source}: {e}")


def extract_csv_data(infile, outfile):
    """
    Extracts the specified columns from an input CSV file and saves the result
    to an output CSV file.

    Args:
        infile (str): Path to the input CSV file.
        outfile (str): Path to the output CSV file.
    """
    try:
        with open(infile, "r") as readfile, open(outfile, "w") as writefile:
            for line in readfile:
                # Split the line by comma and
                # select columns 1 to 4 (0-based index)
                selected_columns = ",".join(line.strip().split(",")[:4])
                writefile.write(selected_columns + "\n")
        print(f"CSV data extracted successfully to {outfile}")
    except Exception as e:
        print(f"Error processing {infile}: {e}")


def extract_tsv_data(infile, outfile):
    """
    Extracts the specified columns from an input TSV file and saves the result
    to an output CSV file.

    Args:
        infile (str): Path to the input TSV file.
        outfile (str): Path to the output CSV file.
    """
    try:
        with open(infile, "r") as readfile, open(outfile, "w") as writefile:
            for line in readfile:
                # Split the line by tab and
                # select columns 5 to 7 (0-based index)
                selected_columns = ",".join(line.strip().split("\t")[4:7])
                writefile.write(selected_columns + "\n")
        print(f"TSV data extracted successfully to {outfile}")
    except Exception as e:
        print(f"Error processing {infile}: {e}")


def extract_fixed_width_data(infile, outfile):
    """
    Extracts the specified columns from an input fixed width file and
    saves the result to an output CSV file.

    Args:
        infile (str): Path to the input fixed width file.
        outfile (str): Path to the output CSV file.
    """
    try:
        with open(infile, "r") as readfile, open(outfile, "w") as writefile:
            for line in readfile:
                # Remove extra spaces and split by space
                cleaned_line = " ".join(line.split())

                # Select columns 10 and 11 (0-based index) directly
                selected_columns = cleaned_line.split(" ")[9:11]
                writefile.write(",".join(selected_columns) + "\n")
        print(f"Fixed width data extracted successfully to {outfile}")
    except Exception as e:
        print(f"Error processing {infile}: {e}")


def consolidate_data_extracted(infile, outfile):
    """
    Combine data from the specified files into a single CSV file.

    Args:
        infile (list): List of input CSV file paths.
        outfile (str): Path to the output CSV file.
    """
    try:
        combined_csv = pd.concat([pd.read_csv(f, header=None) for f in infile], axis=1)
        combined_csv.to_csv(outfile, index=False, header=False)
        print(f"Data consolidated successfully to {outfile}")
    except Exception as e:
        print(f"Error consolidating data: {e}")


def transform_load_data(infile, outfile):
    """
    Transform the fourth column in a CSV file to uppercase

    Args:
        infile (str): Path to the input CSV file.
        outfile (str): Path to the output CSV file.
    """
    try:
        with open(infile, "r") as readfile, open(outfile, "w") as writefile:
            reader = csv.reader(readfile)
            writer = csv.writer(writefile)

            for row in reader:
                # Modify the fourth field (index 3) and convert to uppercase
                row[3] = row[3].upper()
                writer.writerow(row)
        print(f"Data transformed successfully to {outfile}")
    except Exception as e:
        print(f"Error processing {infile}: {e}")


# ============ DAG DEFINITION ============

# Define DAG arguments (Airflow 3.1.0 compatible)
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 10, 26),
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG (Airflow 3.1.0 compatible)
with DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule=timedelta(days=1),  # Changed from schedule_interval to schedule
    catchup=False,
    tags=['etl', 'toll_data'],
) as dag:

    # ============ PATHS ============
    DESTINATION = "/mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-python/dags/python_etl"
    STAGING = os.path.join(DESTINATION, "staging")

    # Source URL
    DATASET_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"

    # File paths
    source = os.path.join(DESTINATION, "tolldata.tgz")
    vehicle_data = os.path.join(DESTINATION, "vehicle-data.csv")
    tollplaza_data = os.path.join(DESTINATION, "tollplaza-data.tsv")
    payment_data = os.path.join(DESTINATION, "payment-data.txt")
    csv_data = os.path.join(STAGING, "csv_data.csv")
    tsv_data = os.path.join(STAGING, "tsv_data.csv")
    fixed_width_data = os.path.join(STAGING, "fixed_width_data.csv")
    extracted_data = os.path.join(STAGING, "extracted_data.csv")
    transformed_data = os.path.join(STAGING, "transformed_data.csv")

    # ============ TASKS ============

    # Download the dataset
    download_data = PythonOperator(
        task_id='download_data',
        python_callable=download_dataset,
        op_kwargs={'url': DATASET_URL, 'destination': source},
    )

    # Unzip data
    unzip_data = PythonOperator(
        task_id='unzip_data',
        python_callable=unzip_tolldata,
        op_kwargs={'source': source, 'destination': DESTINATION},
    )

    # Extract data from csv file
    extract_data_from_csv = PythonOperator(
        task_id='extract_data_from_csv',
        python_callable=extract_csv_data,
        op_kwargs={'infile': vehicle_data, 'outfile': csv_data},
    )

    # Extract data from tsv file
    extract_data_from_tsv = PythonOperator(
        task_id='extract_data_from_tsv',
        python_callable=extract_tsv_data,
        op_kwargs={'infile': tollplaza_data, 'outfile': tsv_data},
    )

    # Extract data from fixed width file
    extract_data_from_fixed_width = PythonOperator(
        task_id='extract_data_from_fixed_width',
        python_callable=extract_fixed_width_data,
        op_kwargs={'infile': payment_data, 'outfile': fixed_width_data},
    )

    # Consolidate data extracted from previous tasks
    consolidate_data = PythonOperator(
        task_id='consolidate_data',
        python_callable=consolidate_data_extracted,
        op_kwargs={'infile': [csv_data, tsv_data, fixed_width_data], 'outfile': extracted_data},
    )

    # Transform and load the data
    transform_data = PythonOperator(
        task_id="transform_data",
        python_callable=transform_load_data,
        op_kwargs={'infile': extracted_data, 'outfile': transformed_data},
    )

    # ============ TASK PIPELINE ============
    # Define the task dependencies
    download_data >> unzip_data >> [extract_data_from_csv, extract_data_from_tsv, extract_data_from_fixed_width] >> consolidate_data >> transform_data