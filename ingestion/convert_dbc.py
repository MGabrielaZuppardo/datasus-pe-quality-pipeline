"""Converte .dbc → parquet via pysus. Remove o .dbc após conversão (LGPD)."""
import argparse
import logging
from pathlib import Path

import pandas as pd
import pysus.ftp.databases as db

from ingestion.utils import build_lineage

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def convert(dbc_path: Path, destino: Path) -> Path:
    destino.mkdir(parents=True, exist_ok=True)

    df: pd.DataFrame = db.read_dbc(str(dbc_path))

    lineage = build_lineage(dbc_path.name)
    for campo, valor in lineage.items():
        df[f"_{campo}"] = valor

    parquet_path = destino / (dbc_path.stem + ".parquet")
    df.to_parquet(parquet_path, index=False)

    dbc_path.unlink()
    log.info("Convertido: %s → %s (original removido)", dbc_path.name, parquet_path)

    return parquet_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=".dbc → parquet")
    parser.add_argument("--input", required=True, help="Caminho do arquivo .dbc")
    parser.add_argument("--destino", default="data/parquet")
    args = parser.parse_args()

    convert(Path(args.input), Path(args.destino))
