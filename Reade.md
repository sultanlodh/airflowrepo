docker compose down -v
docker system prune -af 
docker compose up airflow-init
docker compose up -d

  
 