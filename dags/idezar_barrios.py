from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datasets import idezar_barrios_dataset, idezar_barrios_refined, idezar_barrios_rdf

from datetime import datetime, timedelta

with DAG(
  dag_id='idezar_barrios_extraction',
  description="LD extraction DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule_interval=None,
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag1:
    BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [idezar_barrios_dataset],
        task_id = 'extract_data',
        bash_command = "python extraction/IDEZAR/Barrios/extractionIDEZARBarrios.py "
        )

with DAG(
  dag_id='idezar_barrios_preprocessing',
  description="LD preprocessing DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=[idezar_barrios_dataset],
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag2:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-batch-master/openrefine-batch.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine/refine")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-client/openrefine-client_0-3-10_linux ")
    preprocessing = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [idezar_barrios_refined],
        task_id='preprocessing',
        bash_command="./preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ",
        )
grant_permissions >> preprocessing

with DAG(
  dag_id='idezar_barrios_materialisation',
  description="LD materialisation DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule=[idezar_barrios_refined],
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
  }
) as dag3:
    grant_permissions = BashOperator(task_id = 'permissions', cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x mapping/IDEZAR/Barrios/materialisationIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x preprocessing/IDEZAR/Barrios/preprocessingIDEZARBarrios.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-batch-master/openrefine-batch.sh ")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine/refine")
    # BashOperator(cwd = "/home/edgar/GitHub/USAGE-LD", bash_command="chmod +x tools/openrefine-client/openrefine-client_0-3-10_linux ")
    materialisation = BashOperator(
        cwd = "/home/edgar/GitHub/USAGE-LD",
        outlets = [idezar_barrios_rdf],
        task_id='mapping',
        bash_command="./mapping/IDEZAR/Barrios/materialisationIDEZARBarrios.sh ",
        )
grant_permissions >> materialisation