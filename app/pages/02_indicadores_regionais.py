import streamlit as st
from app.utils.db import get_connection

st.title("Indicadores por Regional de Saúde")

con = get_connection()

df = con.execute("""
    select nome_regional, mes_obito, causa_basica_obito, total_obitos
    from mart_serie_historica_regional
    order by mes_obito, nome_regional
""").df()

regionais = sorted(df["nome_regional"].dropna().unique().tolist())
regional_sel = st.selectbox("Regional de saúde", regionais)

df_filtrado = df[df["nome_regional"] == regional_sel]

st.line_chart(
    df_filtrado.groupby("mes_obito")["total_obitos"].sum(),
    use_container_width=True,
)

st.dataframe(df_filtrado, use_container_width=True)
