FROM apache/airflow:2.9.0-python3.10

USER root

# Install system dependencies required by mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Install Python packages using Airflow constraints
RUN pip install --no-cache-dir \
    apache-airflow-providers-mysql \
    apache-airflow-providers-apache-spark \
    apache-airflow-providers-databricks \
    databricks-sql-connector \
    pymysql \
    mysqlclient \
    pyspark \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.10.txt"