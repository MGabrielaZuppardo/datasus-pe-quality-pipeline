import streamlit as st

st.set_page_config(
    page_title="DATASUS PE — Qualidade de Dados",
    layout="wide",
)

st.title("Pipeline de Qualidade de Dados — DATASUS Pernambuco")
st.markdown(
    """
    Dashboard de monitoramento do pipeline de qualidade de dados do DATASUS
    para o estado de Pernambuco (SES-PE).

    Use o menu lateral para navegar:
    - **Qualidade dos Dados** — completude e score por município
    - **Indicadores Regionais** — série histórica por regional de saúde
    - **Mapa de Municípios** — visualização coroplética dos 185 municípios
    """
)
