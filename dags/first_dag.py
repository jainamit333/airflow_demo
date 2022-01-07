from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {

    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['jainamit333@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        'first_dag',
        default_args=default_args,
        description='First Simple Dag',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=['example', 'bash_operator']
) as dag:
    task1 = DummyOperator(task_id='task_1')
    task2 = DummyOperator(task_id='task_2')
    task3 = DummyOperator(task_id='task_3')
    task4 = DummyOperator(task_id='task_4')

    task1 >> [task2, task3] >> task4

