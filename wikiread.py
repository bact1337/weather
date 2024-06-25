import numpy as np
import pandas as pd

# URL containing the HTML table
url = 'https://de.wikipedia.org/wiki/Liste_von_Windkraftanlagen_in_Nordrhein-Westfalen'

# Read the table(s) from the URL
dfs = pd.read_html(url)

# Display the first DataFrame
print(dfs[0].columns)
df = dfs[0].dropna(axis=0)

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

dfdata = pd.DataFrame(columns=['City', 'Longitude', 'Latitude'])





for index, row in df.iterrows():
    position = str(row['Koordinaten'])

    ps = position.split('°')
    ps2 = ps[1].rsplit(' ')
    long = ps[0]
    lat = ps2[1]
   # print(ps[0],ps2[1])
    wikis = {
        'City': row['Ort'],
        'Latitude': ps[0],
        'Longitude': ps2[1]
    }
    dfdata = dfdata._append(wikis, ignore_index=True)

dfdata['Latitude'] = dfdata['Latitude'].str.replace(',', '.').astype(float)
dfdata['Longitude'] = dfdata['Longitude'].str.replace(',', '.').astype(float)
print(dfdata.to_string())









# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(dfdata, geometry=gpd.points_from_xy(dfdata.Longitude, dfdata.Latitude))

# Set the coordinate reference system (CRS) to WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Load a world basemap
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter to get Germany only
germany = world[world.name == "Germany"]

# Plot the basemap of Germany
ax = germany.plot(color='whitesmoke', edgecolor='black')

# Plot the points on the map
gdf.plot(ax=ax, marker='o', color='red', markersize=1)

# Add titles and labels
plt.title('Cities in Germany')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()
