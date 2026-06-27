from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.python import PythonOperator

from ingestion.download_datasus import download
from ingestion.convert_dbc import convert

RAW = Path("/opt/airflow/data/raw")
PARQUET = Path("/opt/airflow/data/parquet")


def _download(**context):
    ano = context["logical_date"].year
    download("SIH", "PE", ano, RAW)


def _convert(**context):
    ano = context["logical_date"].year
    for dbc in RAW.glob(f"RD*PE*{str(ano)[2:]}*.dbc"):
        convert(dbc, PARQUET)


with DAG(
    dag_id="ingest_sih_pe",
    start_date=datetime(2024, 1, 1),
    schedule="@monthly",
    catchup=False,
    tags=["ingest", "sih", "pe"],
) as dag:
    download_task = PythonOperator(task_id="download_sih_pe", python_callable=_download)
    convert_task = PythonOperator(task_id="convert_dbc_to_parquet", python_callable=_convert)

    download_task >> convert_task
