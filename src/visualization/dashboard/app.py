from shared import gdf, df
import matplotlib.pyplot as plt
import seaborn as sns
from shiny.express import render, ui

ui.page_opts(title="Dengue Cachoeiro", fillable=True)

with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Mapa de Cachoeiro de Itapemirim")
        @render.plot
        def mapa():
            fig, ax = plt.subplots(figsize=(10, 10))
            gdf.plot(ax=ax)
            return fig
        
    with ui.card(full_screen=True):
        ui.card_header("Casos de dengue por bairro")
        @render.plot
        def grafico():
            sns.barplot(df, x="casos", y="local")
            plt.yticks(fontsize=5)