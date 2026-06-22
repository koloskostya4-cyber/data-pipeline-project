# Data Pipeline Project: Analytics Dashboard with Airflow, Superset, and PostgreSQL

[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.9.0-blue)](https://airflow.apache.org/)
[![Apache Superset](https://img.shields.io/badge/Apache%20Superset-latest-blue)](https://superset.apache.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-27.0-blue)](https://www.docker.com/)

## 🎯 Project Overview

This project implements a complete data pipeline for business analytics:
- **Data Source**: CSV files containing company data (sales, employees, etc.)
- **Orchestration**: Apache Airflow for automated ETL workflows
- **Storage**: PostgreSQL for structured data storage
- **Visualization**: Apache Superset for interactive dashboards
- **Containerization**: Docker for reproducible deployment

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────────────┐
│ Docker Network │
├─────────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ │
│ │ Superset │ │ PostgreSQL │ │ Airflow │ │
│ │ :8088 │ │ :5433 │ │ :8080 │ │
│ └─────────────────┘ └─────────────────┘ └─────────────────┘ │
│ │
│ ┌─────────────────────────────────────────────────────────────┐│
│ │ Shared Volume: /Users/username/data/ ││
│ │ └── data.csv ││
│ └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘

text

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git
- DBeaver (optional, for database exploration)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/data-pipeline-project.git
   cd data-pipeline-project
Create network and run containers

bash
docker network create data_network
docker-compose up -d
Initialize Superset

bash
docker exec -it superset_app superset db upgrade
docker exec -it superset_app superset fab create-admin
docker exec -it superset_app superset init
Access services

Superset: http://localhost:8088 (admin/admin)
Airflow: http://localhost:8080 (admin/admin)
PostgreSQL: localhost:5433 (data_user/data_password)
📊 Data Pipeline Workflow

CSV Upload: Place your data.csv in the ./data/ directory
Load Data: Manual or automated loading via Airflow DAG
Transform: Data cleaning and aggregation in Python
Store: PostgreSQL for persistent storage
Visualize: Superset dashboards for business insights
Automate: Airflow DAG runs daily at 9:00 AM
📂 Project Structure

text
.
├── README.md
├── docker-compose.yml          # Docker services configuration
├── .env.example                # Environment variables template
├── dags/
│   ├── refresh_dashboard.py    # Main ETL DAG
│   └── ab_test_analysis.py     # AB-testing DAG
├── scripts/
│   ├── load_data.py            # CSV loading script
│   ├── ab_test_calculator.py   # AB-test calculations
│   └── sql_queries.sql         # Analytical SQL queries
├── data/
│   └── data.csv                # Source data (gitignored)
└── notebooks/                  # Jupyter notebooks for exploration
🔧 Available DAGs

DAG Name	Description	Schedule
refresh_dashboard	Updates company data from CSV	Daily at 9:00 AM
ab_test_analysis	Runs AB-test calculations	Daily at 8:00 AM
📈 Sample Dashboards

Sales Overview: Revenue, profit, and growth trends
Employee Analytics: Department distribution, salaries, headcount
AB-Test Results: Statistical significance, conversion rates
Operational Metrics: Daily KPIs and alerts
🛠️ Development

Run ETL script locally

bash
python scripts/load_data.py
Test DAGs

bash
docker exec -it airflow python /opt/airflow/dags/refresh_dashboard.py
Connect to PostgreSQL

bash
docker exec -it postgres_data psql -U data_user -d my_dataset
