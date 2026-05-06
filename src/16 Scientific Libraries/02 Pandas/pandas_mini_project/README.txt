
	
1) You will need to install GeoPandas to get this mini-project to work:
			pip install geopandas

2) The data for this mini-project is a spreadsheet with metadata for the WIND Toolkit US national dataset:
			https://data.nrel.gov/submissions/54

NOTE: it has already been downloaded:
			data/wtk_site_metadata.csv	# 9.77 MB	Data	

3) The mini-project uses a map of the USA; files containing the geopandas data are:

			data/tl_2023_us_state.dbf
			data/tl_2023_us_state.prj
			data/tl_2023_us_state.shp
			data/tl_2023_us_state.shx

4) To create a map of the USA use the preprepared file "usa_data.py" and include it in your code as:
			# extract map of USA (from local file) and plot
			from usa_data import usa
			usa.plot(ax=ax, color='orange', edgecolor='black')
