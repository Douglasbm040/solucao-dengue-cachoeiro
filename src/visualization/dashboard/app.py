from shared import gdf, df, gdf_map, geojson_data
import matplotlib.pyplot as plt
import seaborn as sns
from shiny.express import render, ui
import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
import branca
import numpy as np


ui.page_opts(title="Dengue Cachoeiro", fillable=True)

with ui.card():
    ui.card_header("Mapa de Cachoeiro de Itapemirim")
    @render.ui
    def mapa():

        m = folium.Map(location=[-20.838016, -41.132593], zoom_start=10, width='100%', height='60%')



        tooltip = folium.GeoJsonTooltip(
            fields=[ 'NOMES', 'AREA_KM2', 'Casos'],
            aliases=['Nome: ', 'Àrea(Km²): ', 'Casos de dengue: '],
            localize=True,
            sticky=False,
            labels=True,
            style="""
                background-color: #F0EFEF;
                border: 2px solid black;
                border-radius: 3px;
                box-shadow: 3px;
            """,
            max_width=800,
        )

        colormap = branca.colormap.linear.OrRd_09.scale(
            vmin=gdf_map["Casos"].quantile(0.0),
            vmax=gdf_map["Casos"].quantile(1),
            #colors=["red", "orange", "lightblue", "green", "darkgreen"],
            #caption="State Level Median County Household Income (%)",
        )

        # Adiciona os limites dos estados a partir do GeoDataFrame
        folium.GeoJson(
            gdf_map,
            name='geojson',
            style_function=lambda x: {
                "fillColor": colormap(x["properties"]["Casos"])
                if x["properties"]["Casos"] is not None
                else "transparent",
                "color": "black",
                "fillOpacity": 1,
            },
            tooltip=tooltip
        ).add_to(m)
        for feature in geojson_data['features']:
            coordinates = [feature['properties']['latitude'], feature['properties']['longitude']]
            folium.Marker(location=coordinates, popup=str(feature['properties']['nm_fantas'] + '\n'+ str(coordinates))).add_to(m)
        
        
        folium.LayerControl().add_to(m)
        # Adiciona a camada de controle
        
        # Renderiza o mapa como HTML e passa para o Shiny
        return ui.HTML(m._repr_html_())