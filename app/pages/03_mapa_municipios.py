import streamlit as st
from app.utils.db import get_connection

st.title("Mapa Coroplético — Municípios de PE")

con = get_connection()

df = con.execute("""
    select codigo_municipio, nome_municipio, completude_pct, qualidade_suficiente
    from mart_indicadores_municipio
""").df()

st.info(
    "Para renderizar o mapa coroplético, adicione o shapefile dos municípios PE (IBGE) "
    "em data/shapefiles/municipios_pe.geojson e descomente o bloco Folium abaixo."
)

st.dataframe(df, use_container_width=True)

# import folium
# from streamlit_folium import st_folium
# m = folium.Map(location=[-8.5, -37.5], zoom_start=7)
# folium.Choropleth(
#     geo_data="data/shapefiles/municipios_pe.geojson",
#     data=df,
#     columns=["codigo_municipio", "completude_pct"],
#     key_on="feature.properties.CD_MUN",
#     fill_color="RdYlGn",
#     legend_name="Completude (%)",
# ).add_to(m)
# st_folium(m, use_container_width=True)
