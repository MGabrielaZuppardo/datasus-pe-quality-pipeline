import streamlit as st
from app.utils.db import get_connection

st.title("Qualidade dos Dados por Município")

con = get_connection()

df = con.execute("""
    select
        nome_municipio,
        nome_regional,
        total_obitos,
        completude_pct,
        qualidade_suficiente
    from mart_qualidade_por_fonte
    order by completude_pct asc
""").df()

col1, col2, col3 = st.columns(3)
col1.metric("Total de municípios", len(df))
col2.metric("Com qualidade suficiente (>=70%)", int(df["qualidade_suficiente"].sum()))
col3.metric("Completude média", f"{df['completude_pct'].mean():.1f}%")

st.dataframe(
    df.style.background_gradient(subset=["completude_pct"], cmap="RdYlGn"),
    use_container_width=True,
)
