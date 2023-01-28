import pandas as pd
from pathlib import PurePath
from datetime import datetime, timedelta
from clickhouse_driver import Client


from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def extract_data(url, **context):
    client = Client(host="clickhouse")

    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{url}/export?format=csv")
    df["Person_id"] = df.Person.map(hash).abs()

    client.execute(
        """CREATE TABLE IF NOT EXISTS DDS.people(
                   Person_id UInt64 NOT NULL
                  ,Person   String NOT NULL 
                  ,Region   String NOT NULL)
                        ENGINE = MergeTree()
                        ORDER BY Person;"""
    )

    client.execute("INSERT INTO DDS.people VALUES", df.to_dict("records"))


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

extract_data = PythonOperator(
    task_id="people",
    python_callable=extract_data,
    op_kwargs={"url": "1NKb_sdrg1aRvPw2DnWLVMXF7lFIR7vc5p-xWiCr8Mww"},
    dag=dag,
)

extract_data
