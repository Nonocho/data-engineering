# Traffic Flow Optimization with Airflow and Kafka
This repository contains my submission for the Final Assignment, consisting of ***Hands-on Lab: Build a Streaming ETL Pipeline using Kafka***. 

## Objectives
* Build a streaming ETL pipeline using Kafka

## Project layout
├── kafka                            <- Creating Streaming Data Pipelines using Kafka
│   ├── create_topic_toll.sh         <- Exercise 2.3 - Create a topic named 'toll'
│   ├── kafka_install.sh             <- Exercise 1 - Prepare the lab environment (Steps 1-2)
│   ├── start_kafka.sh               <- Exercise 2.2 - Start Kafka server
│   ├── start_zookeeper.sh           <- Exercise 2.1 - Start Zookeeper
│   ├── streaming_data_reader.py     <- Customized Streaming Data Consumer program
│   └── toll_traffic_generator.py    <- Customized Toll Traffic Simulator program

### Creating Streaming Data Pipelines using Kafka

1. Start a MySQL Database server.
1. Create a table to hold the toll data.
1. Start Zookeeper server.
1. Start Kafka server.
1. Create a Kafka topic named `toll`.
1. Download the Toll Traffic Simulator `toll_traffic_generator.py` program.
1. Configure the Toll Traffic Simulator and set the topic to `toll`.
1. Run the Toll Traffic Simulator program.
1. Download the Streaming Data Consumer `streaming_data_reader.py` program.
1. Customize the consumer program to write into a MySQL database table.
1. Run the Streaming Data Consumer program.
1. Verify that streamed data is being collected in the database table.
