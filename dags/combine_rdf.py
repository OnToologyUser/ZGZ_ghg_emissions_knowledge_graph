from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datasets import idezar_barrios_rdf, idezar_distritos_rdf, zgz_residencial_rdf, rdf_combined

from datetime import datetime, timedelta

with DAG(
  dag_id='combine_rdf',   
  description="LD preprocessing DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=(idezar_barrios_rdf | idezar_distritos_rdf | zgz_residencial_rdf), 
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag1:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x mapping/join.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-batch-master/openrefine-batch.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine/refine")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-client/openrefine-client_0-3-10_linux ")
    combining = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [rdf_combined],
        task_id='combining',
        bash_command="./mapping/join.sh ",
        )
grant_permissions >> combining