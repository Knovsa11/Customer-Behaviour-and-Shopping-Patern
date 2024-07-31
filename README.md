# Customer-Behaviour-and-Shopping-Patern

## Overview
This project is designed to analyze consumer shopping patterns and behavior based on the available dataset. The analysis aims to provide recommendations to improve customer satisfaction and increase revenue. The dashboard is created using Kibana, with data processing done using Python and PostgreSQL.

## Project Purpose
The main purpose of this project is to understand consumer shopping behavior and identify patterns that can be leveraged to enhance customer satisfaction and drive revenue growth. By analyzing shopping patterns, businesses can make informed decisions on marketing strategies, product placements, and inventory management.

## Problem Statement
Understanding consumer shopping behavior is crucial for businesses to tailor their offerings and improve customer experiences. However, analyzing large volumes of transaction data to derive meaningful insights can be challenging. This project addresses this challenge by using data analysis techniques to identify key shopping patterns and provide actionable recommendations.

## Background
In the competitive retail environment, gaining insights into customer behavior is vital for staying ahead. By analyzing transaction data, businesses can understand what drives customer purchases, identify popular products, and detect trends over time. This project utilizes advanced data analysis and visualization tools to uncover these insights.

## Project Output
The output of this project includes:

A dashboard created using Kibana, displaying key metrics and insights.

Recommendations to improve customer satisfaction and increase revenue.

Visualizations of shopping patterns and behavior.

Cleaned and validated dataset ready for analysis.

## Methods
The project utilizes the following methods:

Data Cleaning and Transformation: Processing raw data to remove inconsistencies and prepare it for analysis.

Data Loading: Importing data into PostgreSQL and Elasticsearch for further processing and visualization.

Data Validation: Using Great Expectations to ensure data quality.

Visualization: Creating a dashboard in Kibana to display key insights.

Automation: Using Apache Airflow to automate data transformation and loading processes.

## Technology Stack
The project is developed using the following technologies:

Programming Language: Python

Database: PostgreSQL

Data Visualization: Kibana

Data Processing: Apache Airflow, Great Expectations


Containerization: Docker

## Files

Folder: image

This folder contains:

6 analysis result images
1 introduction image
1 conclusion image

P2M3_kelvin_rizky_data_raw.csv
This CSV file contains the raw dataset used in the analysis.

P2M3_kelvin_rizky_ddl.txt
This text file contains the SQL queries for creating the database schema in PostgreSQL.

P2M3_kelvin_rizky_DAG.py
This Python script contains the Apache Airflow DAG for automating the data transformation and loading process from PostgreSQL to Elasticsearch.

P2M3_kelvin_rizky_GX.ipynb
This Jupyter notebook contains the Python code for validating the data using Great Expectations.

airflow_ES.yaml
This YAML file contains the configuration for setting up Apache Airflow with Docker.
