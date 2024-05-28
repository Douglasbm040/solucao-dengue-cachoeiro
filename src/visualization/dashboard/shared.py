from pathlib import Path

import geopandas as gpd
import pandas as pd
import json
import numpy as np

app_dir = Path(__file__).parent
gdf_map = gpd.read_file('SHP\SHP - Comunidades Urbanas e Rurais\Limites de Comunidades Urbanas e Rurais de Cachoeiro de Itapemirim.shp')
# gdf_map['dengue'] = [0 for _ in range(len(gdf_map))]

df = pd.read_csv('dengue.csv')
gdf_map = gdf_map.merge(df, on='NOMES', how='left', )


print(gdf_map)

with open('GeoJSON - Unidades de Saude\GeoJSON - Unidades de Saude.geojson', 'r') as f:
        geojson_data = json.load(f)

df_points = pd.DataFrame([(point['properties']['longitude'], point['properties']["latitude"], point['properties']['nm_fantas']) for point in geojson_data['features']], columns=['longitude', 'latitude', 'nm_ubs'])
gdf = gpd.read_file('GeoJSON - Unidades de Saude\GeoJSON - Unidades de Saude.geojson')
