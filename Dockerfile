FROM apache/airflow:2.2.3-python3.9

COPY dags $AIRFLOW_HOME/dags