from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

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
    task_1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )
    task_2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=2
    )
    task_3 = BashOperator(
        task_id='print_message',
        bash_command='echo Message from Airflow'
    )
    task_4 = BashOperator(
        task_id='print_time',
        bash_command='time'
    )
    task_1 >> [task_2, task_3] >> task_4
