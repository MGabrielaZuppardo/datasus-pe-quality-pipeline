"""Download de arquivos .dbc do FTP DATASUS filtrados por UF."""
import argparse
import ftplib
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

FTP_HOST = "ftp.datasus.gov.br"
BASE_PATH = "/dissemin/publicos"

SISTEMAS = {
    "SIM": "SIM/CID10/DORES",
    "SINAN": "SINAN/DADOS/FINAIS",
    "SIH": "SIHSUS/DADOS",
    "SINASC": "SINASC/DADOS/FINAIS",
    "CNES": "CNES/DADOS",
}


def download(sistema: str, uf: str, ano: int, destino: Path) -> list[Path]:
    destino.mkdir(parents=True, exist_ok=True)
    pasta_ftp = f"{BASE_PATH}/{SISTEMAS[sistema]}"
    prefixo = f"{sistema[:2]}{uf}{str(ano)[2:]}".upper()

    baixados = []
    with ftplib.FTP(FTP_HOST, timeout=30) as ftp:
        ftp.login()
        ftp.cwd(pasta_ftp)
        arquivos = [a for a in ftp.nlst() if a.upper().startswith(prefixo)]
        if not arquivos:
            log.warning("Nenhum arquivo encontrado para prefixo %s em %s", prefixo, pasta_ftp)
        for arquivo in arquivos:
            destino_arquivo = destino / arquivo
            log.info("Baixando %s...", arquivo)
            with open(destino_arquivo, "wb") as f:
                ftp.retrbinary(f"RETR {arquivo}", f.write)
            log.info("Salvo em %s", destino_arquivo)
            baixados.append(destino_arquivo)

    return baixados


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download DATASUS FTP → .dbc")
    parser.add_argument("--sistema", required=True, choices=SISTEMAS.keys())
    parser.add_argument("--uf", default="PE")
    parser.add_argument("--ano", type=int, required=True)
    parser.add_argument("--destino", default="data/raw")
    args = parser.parse_args()

    download(args.sistema, args.uf, args.ano, Path(args.destino))
