#!/bin/bash
echo "🚀 Starting Data Pipeline..."
docker network create data_network 2>/dev/null || true
docker-compose up -d

echo "⏳ Waiting for containers to start..."
sleep 10

echo "🔧 Initializing Superset..."
docker exec -it superset_app superset db upgrade
docker exec -it superset_app superset fab create-admin
docker exec -it superset_app superset init

echo "✅ All services are running!"
echo "🌐 Superset: http://localhost:8088 (admin/admin)"
echo "🌐 Airflow: http://localhost:8080 (admin/admin)"
echo "🐘 PostgreSQL: localhost:5433 (data_user/data_password)"
