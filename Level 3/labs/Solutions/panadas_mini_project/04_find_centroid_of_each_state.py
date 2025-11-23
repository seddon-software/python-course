import pandas as pd
pd.set_option('display.precision', 1)

df = pd.read_csv("data/wtk_site_metadata.csv")

# convert to a series, removing enties where the state is unknown
states = df['State'][df['State'] != 'Unknown']
states = states.drop_duplicates().values

# use aggregate to calculate the centroid of each state
dfs_of_states = []
for state in states:
    df_of_state = df[['latitude', 'longitude', 'State']][df['State']==state]
    df_of_state = df_of_state.groupby(['State']).aggregate("mean")
    df_of_state['State'] = state
    dfs_of_states.append(df_of_state)

# combine indivual state dataframes
centroid_for_states = pd.concat(dfs_of_states, ignore_index=True)
print(centroid_for_states)
