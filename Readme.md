docker compose up -d --build
docker exec airflow-webserver airflow db init
docker exec -it airflow-webserver bash