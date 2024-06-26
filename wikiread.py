import numpy as np
import pandas as pd

# URL containing the HTML table
urls = ['https://de.wikipedia.org/wiki/Liste_von_Windkraftanlagen_in_Nordrhein-Westfalen',
        'https://de.wikipedia.org/wiki/Liste_von_Windkraftanlagen_in_Baden-W%C3%BCrttemberg']

# Read the table(s) from the URL
dfs = pd.read_html(urls[1])

print(dfs[0].columns)

df = dfs[0]
df = df.dropna(subset=['Koordinaten'])
#print(df.to_string())



import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

dfdata = pd.DataFrame(columns=['City', 'Longitude', 'Latitude'])



print(dfdata.to_string())


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
    print(position)
    dfdata = dfdata._append(wikis, ignore_index=True)

#print(dfdata.to_string())

dfdata['Latitude'] = dfdata['Latitude'].str.replace(',', '.').astype(float)
dfdata['Longitude'] = dfdata['Longitude'].str.replace(',', '.').astype(float)









# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(dfdata, geometry=gpd.points_from_xy(dfdata.Longitude, dfdata.Latitude))

# Set the coordinate reference system (CRS) to WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Step 5: Load the shapefile into a GeoDataFrame
shapefile_path = 'ne_110m_admin_0_countries.shp'  # Update this path to where you extracted the shapefile
world = gpd.read_file(shapefile_path)

# Step 6: Filter the GeoDataFrame for Germany
germany = world[world['NAME'] == "Germany"]

# Plot the basemap of Germany
ax = germany.plot(color='whitesmoke', edgecolor='black')

# Plot the points on the map
gdf.plot(ax=ax, marker='o', color='red', markersize=1)

# Add titles and labels
plt.title('Windräder')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()
