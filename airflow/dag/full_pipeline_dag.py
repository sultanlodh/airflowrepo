from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

from scripts.spark_job import run_spark_job

with DAG(
    dag_id="full_data_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    spark_task = PythonOperator(
        task_id="run_spark",
        python_callable=run_spark_job
    )

    dbt_task = BashOperator(
        task_id="run_dbt",
        bash_command="docker exec airflow-dbt dbt run"
    )

    spark_task >> dbt_task