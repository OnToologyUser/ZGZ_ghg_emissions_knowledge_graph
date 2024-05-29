from airflow import DAG, Dataset
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
  
def extract_data():
  from owslib.wms import WebMapService
  wms = WebMapService('http://idezar.zaragoza.es/wms/IDEZar_base/IDEZar_base')
  data = wms.getmap(  layers=['BARRIO_DELIMITACION'],
                    styles=['BARRIO_DELIMITACION'],
                    srs='EPSG:4326',
                    bbox=(-1.1792692070827793, 41.4488949772607, -0.6664220744662599, 41.93490845284696),
                    size=(300, 250),
                    format='application/atom+xml',
                    transparent=True
                    )
  out = open('data/IDEZAR/Barrios/raw/BARRIO_DELIMITACION.xml', 'wb')
  out.write(data.read())
  out.close()
  print("Extraction complete")

idezar_barrios_dataset = Dataset("data/IDEZAR/Barrios/raw/BARRIO_DELIMITACION.xml")

with DAG(
  dag_id='idezar_barrios_extraction',
  description="LD extraction DAG for IDEZAR Barrios dataset",
  start_date=datetime(year=2024, month=5, day=28),
  catchup=False,
  schedule_interval=None,#'@daily', #timedelta(minutes=2),
  default_args={
    'owner': 'edgar',
    'retries': 5,
    'retry_delay': timedelta(minutes=0.5)
  }
) as dag:

  start_pipeline = EmptyOperator(
    task_id='start_pipeline',
  )

  extraction = PythonOperator(
    outlets = [idezar_barrios_dataset],
    task_id = 'extract_data',
    python_callable = extract_data
  )

  preprocessing = BashOperator(
    task_id='preprocessing',
    bash_command="pwd "
  )

start_pipeline >> extraction >> preprocessing

