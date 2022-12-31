from pathlib import PurePath
import logging
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime, timedelta

dag_name = PurePath(__file__).name.split('.')[0]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 9, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'max_active_runs': 1,
    'email': ['test@mail.ru']
}

dag = DAG(
 dag_name,
 default_args=default_args, 
 schedule_interval='*/2 * * * *',
 catchup=False,
)

orders_sensor = ExternalTaskSensor(task_id='orders',
                                              external_task_id='orders',
                                              external_dag_id='extract_data',
                                              execution_delta=timedelta(minutes=2),
                                              timeout=(60),
                                              retries=3,
                                              dag=dag)

returns_sensor = ExternalTaskSensor(task_id='returns',
                                              external_task_id='returns',
                                              external_dag_id='extract_data',
                                              execution_delta=timedelta(minutes=2),
                                              timeout=(60),
                                              retries=3,
                                              dag=dag)

star_schema = BashOperator(
    task_id='dds',
    bash_command='python /opt/airflow/Python/store_orders.py',
    dag=dag
)

star_schema_2 = BashOperator(
    task_id='dds_2',
    bash_command='python /opt/airflow/Python/store_returns.py',
    dag=dag
)

orders_sensor >> star_schema
returns_sensor >> star_schema_2

