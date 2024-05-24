from pathlib import Path

import geopandas as gpd
import pandas as pd

app_dir = Path(__file__).parent
gdf = gpd.read_file('SHP\SHP - Comunidades Urbanas e Rurais\Limites de Comunidades Urbanas e Rurais de Cachoeiro de Itapemirim.shp')
df = pd.read_csv('dengue.csv')