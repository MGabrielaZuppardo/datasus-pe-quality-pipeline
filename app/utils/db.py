import os
import duckdb


def get_connection() -> duckdb.DuckDBPyConnection:
    path = os.getenv("DUCKDB_PATH", "../data/datasus_pe.duckdb")
    return duckdb.connect(path, read_only=True)
