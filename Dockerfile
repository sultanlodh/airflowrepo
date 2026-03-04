FROM apache/airflow:2.9.0-python3.10

USER airflow

RUN pip install --no-cache-dir \
    apache-airflow-providers-mysql \
    apache-airflow-providers-databricks \
    databricks-sql-connector \
    pymysql \
    mysqlclient \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.10.txt"