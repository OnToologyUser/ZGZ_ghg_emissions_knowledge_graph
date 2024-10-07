from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from datasets import usage_ontology

with DAG(
  dag_id='ontology_conceptualisation_to_code',
  description="Ontology transformation from conceptual model to code",
  start_date=datetime(year=2024, month=6, day=11),
  schedule_interval=None,#'@daily', #timedelta(minutes=2),
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
  }
) as dag:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x ontology/conceptualisation_to_code.sh ")
    conceptualisation_to_code = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [usage_ontology],
        task_id='conceptualisation_to_code',
        bash_command="./ontology/conceptualisation_to_code.sh ",
        )
grant_permissions >> conceptualisation_to_code
