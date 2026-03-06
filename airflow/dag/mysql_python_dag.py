from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import logging

# Add project path
sys.path.append("/opt/airflow/dags/repo/airflow")
from scripts.getMysqlData import MySQLDataExtractor


def run_mysql_extractor():

    db_config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "MySecretPassword123",
        "database": "ecommerce_db",
        "port": 14306
    }

    extractor = MySQLDataExtractor(db_config)
    extractor.run()


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}


with DAG(
    dag_id="mysql_data_extractor_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["mysql", "extractor"]
) as dag:

    extract_task = PythonOperator(
        task_id="run_mysql_extractor",
        python_callable=run_mysql_extractor
    )

    extract_task