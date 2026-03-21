from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


def task1():
    print('Task:-1 (Extract)')


def task2():
    print("Task:-2 (Transform)")


def task3():
    print("Task:-3 (Load)")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}


with DAG(
    dag_id = "simple_etl_dag",
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    t1 = PythonOperator(
        task_id = "extrack",
        python_collable = task1
    )

    t2 = PythonOperator(
        task_id = "transform",
        python_collable = task2
    )

    t3 = PythonOperator(
        task_id = "lad",
        python_collable = task3
    )

    t1 >> t2 >> t3
    