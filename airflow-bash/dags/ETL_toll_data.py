# Import the libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define DAG arguments
default_args = {
    'owner': 'nonocho',
    'start_date': datetime.today(),
    'email': ['nonocho@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule='@daily',  # ✅ FIXED
    catchup=False,
)

# Task 1 - Unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='cd /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash && tar -xzf tolldata.tgz -C .',
    dag=dag,
)

# Task 2 - Extract data from CSV
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d',' -f1,2,3,4 /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/vehicle-data.csv > /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/csv_data.csv",
    dag=dag,
)

# Task 3 - Extract data from TSV
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -d$'\t' -f5,6,7 /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/tollplaza-data.tsv > /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/tsv_data.csv",
    dag=dag,
)

# Task 4 - Extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="awk '{print $(NF-1)\",\"$NF}' /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/payment-data.txt > /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/fixed_width_data.csv",
    dag=dag,
)

# Task 5 - Consolidate data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=(
        "paste -d',' "
        "/mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/csv_data.csv "
        "/mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/tsv_data.csv "
        "/mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/fixed_width_data.csv "
        "> /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/extracted_data.csv"
    ),
    dag=dag,
)

# Task 6 - Transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="tr '[a-z]' '[A-Z]' < /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/extracted_data.csv > /mnt/c/Users/Windows/Desktop/Coding/git-nonocho/data-engineering/airflow-bash/staging/transformed_data.csv",
    dag=dag,
)

# Task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data