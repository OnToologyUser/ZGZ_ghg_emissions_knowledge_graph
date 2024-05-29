from airflow import DAG, Dataset
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

idezar_barrios_dataset = Dataset("data/IDEZAR/Barrios/raw/BARRIO_DELIMITACION.xml")

with DAG(
  dag_id='idezar_barrios_preprocessing',
  description="LD preprocessing DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=[idezar_barrios_dataset],
  # template_searchpath="$AIRFLOW_HOME",
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(minutes=0.25)
  }
) as dag:

  preprocessing = BashOperator(
    cwd = "/home/edgar/GitHub/USAGE-LD",
    task_id='preprocessing',
    bash_command="./pipeline.sh ",
  )

preprocessing