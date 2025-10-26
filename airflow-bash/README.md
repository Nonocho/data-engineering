
This repository contains my submission for the Final Assignment consisting of ***Hands-on Lab: Build an ETL Pipeline using Bash with Airflow*** 

## Objectives
* Create an ETL pipeline using an Airflow DAG
* Build a streaming ETL pipeline using Kafka

## Project Scenario

* Collect data available in different formats and consolidate it into a single file.
* Create a data pipeline that collects the streaming data and loads it into a database.

## Project layout

├── bash                                     <- Build an ETL Pipeline using Bash with Airflow
│   └── airflow/                             <- AIRFLOW_HOME
│       └── dags/                            <- DAGS_FOLDER
│           ├── csv_data.csv                 <- Extracted data from vehicle-data.csv
│           ├── ETL_toll_data.py             <- ETL_toll_data DAG using BashOperator
│           ├── Extract_Transform_data.sh    <- Shell script for ETL tasks
│           ├── extracted_data.csv           <- Consolidated data from extracted files
│           ├── fixed_width_data.csv         <- Extracted data from payment-data.txt
│           ├── payment-data.txt             <- Fixed width file
│           ├── tolldata.tgz                 <- Source data tarball
│           ├── tollplaza-data.tsv           <- Tab-separated values file  (see Notes)
│           ├── transformed_data.csv         <- Transformed extracted data
│           ├── tsv_data.csv                 <- Extracted data from tollplaza-data.tsv
│           └── vehicle-data.csv             <- Comma-separated values file
├
