import geopandas as gpd 

path = "data/tl_2023_us_state.shp"
df = gpd.read_file(path)
df = df.to_crs(epsg="4326")

# remove non continental data
non_continental = ['HI','VI','MP','GU','AK','AS','PR']
usa = df
for abbreviation in non_continental:
    usa = usa[usa.STUSPS != abbreviation]

