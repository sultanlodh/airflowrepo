from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# Add project path
sys.path.append("/opt/airflow/dags/repo/airflow")

from scripts.test_case import hello


with DAG(
    dag_id="run_external_script-1",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    run_task = PythonOperator(
        task_id="run_python_method-1",
        python_callable=hello,
    )