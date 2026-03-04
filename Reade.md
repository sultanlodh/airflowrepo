docker compose build --no-cache
docker compose up airflow-init
docker compose up -d

docker compose down -v   
docker system prune -af  