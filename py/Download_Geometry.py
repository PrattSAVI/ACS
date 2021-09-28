#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

path = r"zip:C:\Users\csucuogl\Downloads\tl_2019_us_county.zip"

df = gpd.read_file( path )
df.head(5)

#%% Filter STATE

df = df[ df['STATEFP']== '06' ].copy()
df.head(5)

# %%

water = gpd.GeoDataFrame()
for i,r in df.iterrows():
    text = r['GEOID']

    name = 'https://www2.census.gov/geo/tiger/TIGER2019/AREAWATER/tl_2019_' + text + '_areawater.zip'
    temp = gpd.read_file( name )

    water = water.append( temp )

water.head( 5 )

# %%

water.to_file( r'C:\Users\csucuogl\Desktop\DATA\tracts\CA_Water.shp' )

# %%
