from pyspark.sql import SparkSession

def run_spark_job():

    spark = SparkSession.builder \
        .master("spark://spark:7077") \
        .appName("airflow_spark_job") \
        .getOrCreate()

    data = [("Sultan", 30), ("Airflow", 5)]
    df = spark.createDataFrame(data, ["name", "age"])

    df.show()

    spark.stop()