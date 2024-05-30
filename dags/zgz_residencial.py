from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datasets import zgz_residencial_dataset, zgz_residencial_refined, zgz_residencial_rdf
from datetime import datetime, timedelta

with DAG(
  dag_id='zgz_residencial_preprocessing',
  description="LD preprocessing DAG for ZGZ residencial dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=[zgz_residencial_dataset],
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag2:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/ZGZ/Residencial/preprocessingZGZResidencial.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-batch-master/openrefine-batch.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine/refine")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-client/openrefine-client_0-3-10_linux ")

    preprocessing = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [zgz_residencial_refined],
        task_id='preprocessing',
        bash_command="./preprocessing/ZGZ/Residencial/preprocessingZGZResidencial.sh ",
        )
grant_permissions >> preprocessing

with DAG(
  dag_id='zgz_residencial_materialisation',
  description="LD materialisation DAG for ZGZ residencial dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=[zgz_residencial_refined],
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag3:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x mapping/ZGZ/Residencial/materialisationZGZResidencial.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-batch-master/openrefine-batch.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine/refine")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-client/openrefine-client_0-3-10_linux ")
    materialisation = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [zgz_residencial_rdf],
        task_id='mapping',
        bash_command="./mapping/ZGZ/Residencial/materialisationZGZResidencial.sh ",
        )
grant_permissions >> materialisation