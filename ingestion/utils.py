"""Utilitários compartilhados entre scripts de ingestão."""
import subprocess
from datetime import date


def get_git_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        return "unknown"


def build_lineage(arquivo_origem: str) -> dict:
    return {
        "arquivo_origem": arquivo_origem,
        "data_extracao": date.today().isoformat(),
        "versao_pipeline": get_git_hash(),
    }
