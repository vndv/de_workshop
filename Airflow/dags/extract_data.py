from pathlib import PurePath
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


dag_name = PurePath(__file__).name.split(".")[0]

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 9, 1),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "max_active_runs": 1,
    "email": ["test@mail.ru"],
}

dag = DAG(
    dag_name,
    default_args=default_args,
    schedule_interval="*/2 * * * *",
    catchup=False,
)

orders = BashOperator(
    task_id="orders",
    bash_command="python /opt/airflow/Python/orders.py",
    dag=dag,
)

returns = BashOperator(
    task_id="returns",
    bash_command="python /opt/airflow/Python/returns.py",
    dag=dag,
)


[orders, returns]
