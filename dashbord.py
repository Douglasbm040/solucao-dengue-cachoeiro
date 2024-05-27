from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json

# Carregando os dados GeoJSON
with open('configuration\\repositories\\dados brutos\\DOUGLAS\\GeoJSON - Unidades de Saude.geojson', 'r') as f:
    geojson_data = json.load(f)

# Criando um aplicativo Dash
app = Dash(__name__)

# Definindo o layout do aplicativo
app.layout = html.Div([
    html.H1("Mapa de Unidades de Saúde - Exemplo Dash", style={'textAlign': 'center'}),  # Título centralizado
    dcc.Graph(id='mapa-com-pontos'),  # Gráfico de mapa
    dcc.RadioItems(id='mostrar-ubs-checkbox',  # Checkbox para mostrar/ocultar pontos
                   options=[
                       {'label': 'Exibir UBS', 'value': 'exibir'},
                       {'label': 'Ocultar UBS', 'value': 'ocultar'}
                   ],
                   value='exibir',  # Padrão para exibir pontos
                   labelStyle={'display': 'block', 'margin-left': '20px'}),  # Estilo dos rótulos
    # O Input foi removido, não é mais necessário
])

# Callback para atualizar o mapa com pontos
@app.callback(
    Output('mapa-com-pontos', 'figure'),
    [Input('mostrar-ubs-checkbox', 'value')]
)
def update_map(mostrar_pontos):
    # Carregando os dados GeoJSON
    with open('configuration\\repositories\\dados brutos\\DOUGLAS\\GeoJSON - Unidades de Saude.geojson', 'r') as f:
        geojson_data = json.load(f)

    # Criando um DataFrame a partir do GeoJSON
    df_points = pd.DataFrame([(point['properties']['longitude'], point['properties']["latitude"], point['properties']['nm_fantas']) for point in geojson_data['features']], columns=['longitude', 'latitude', 'nm_ubs'])

    # Criando o mapa com pontos usando Plotly Express
    fig = px.scatter_mapbox(df_points, lat="latitude", lon="longitude", hover_name="nm_ubs", zoom=13)

    # Atualizando a visibilidade dos pontos de acordo com a seleção do usuário
    if mostrar_pontos == 'ocultar':
        fig.update_traces(visible='legendonly')

    # Personalizando o layout do mapa
    fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0})

    return fig

# Executando o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
