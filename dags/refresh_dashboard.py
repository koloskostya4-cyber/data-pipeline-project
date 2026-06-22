"""
DAG для автоматического обновления данных компании
Данные берутся из CSV-файла на Mac: /Users/konstantin/Documents/project/data/data.csv
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def update_data():
    """Загрузка CSV в PostgreSQL"""
    # Путь к CSV на вашем Mac (смонтирован в контейнер)
    csv_path = '/opt/airflow/data/company/data.csv'
    
    # Подключение к PostgreSQL
    engine = create_engine('postgresql://data_user:data_password@postgres_data:5432/my_dataset')
    
    try:
        # Загрузка CSV
        df = pd.read_csv(csv_path)
        logger.info(f"📊 Загружено {len(df)} строк из CSV")
        
        # Сохранение в PostgreSQL
        df.to_sql('company_data', engine, if_exists='replace', index=False)
        logger.info(f"✅ Данные обновлены: {len(df)} записей")
        
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        raise

with DAG(
    'refresh_company_dashboard',
    default_args=default_args,
    description='Ежедневное обновление данных компании из CSV',
    schedule_interval='0 9 * * *',  # Каждый день в 9:00
    catchup=False,
    max_active_runs=1,
    tags=['company', 'etl'],
) as dag:
    
    update_task = PythonOperator(
        task_id='update_data',
        python_callable=update_data
    )
    
    update_task