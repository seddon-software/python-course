import time
import pandas as pd

pd.set_option('display.precision', 1)
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 500)

# read in WIND data
WIND_df = pd.read_csv("data/wtk_site_metadata.csv")
print(WIND_df.head(5))
time.sleep(5)
print(WIND_df.sample(5))
time.sleep(5)
print(WIND_df.tail(5))

