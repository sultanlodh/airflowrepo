from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# Add project path
sys.path.append("/opt/airflow/dags/repo/airflow")

from scripts.my_script import say_hello


with DAG(
    dag_id="run_external_script",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    run_task = PythonOperator(
        task_id="run_python_method",
        python_callable=say_hello,
    )