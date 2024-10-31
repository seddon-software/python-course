import pandas as pd
import numpy as np
from io import StringIO


'''
How to split columns data
'''

def main():
    column_names = ['date', 'number', 'comment', 'duration']
    df = pd.read_csv(
        get_test_data(), 
        skipinitialspace = True, 
        sep=",", 
        engine='python',
        names=column_names)

# extract month and day from date column
    df['month'] = df['date'].str.slice(0,3)
    df['day'] = df['date'].str.slice(3)

# extract hours, minutes, seconds from duration field
    duration = df['duration'].str.split(':',expand=True)
    duration.columns = ['hours','mins','secs']
    df = df.join(duration)

# reorder columns (dropping date and duration)
    df = df[['month', 'day', 'number', 'hours', 'mins', 'secs', 'comment']]
    print(df)

def get_test_data():
    return StringIO("""
        Nov12,01844 273422,Calls to UK landlines,00:00:55
        Nov21,01989 770121,Calls to UK landlines,03:54:44
        Nov17,01491 615643,Calls to UK landlines,00:26:50
        Nov15,01753 862212,Calls to UK landlines,00:02:16
        Dec11,0121 559 1152,Calls to UK landlines,00:00:15
        Dec11,0121 559 1152,Calls to UK landlines,01:02:06
        Nov11,0121 559 1152,Calls to UK landlines,00:04:52
        Nov20,01491 613643,Calls to UK landlines,00:00:02
        Nov17,01491 613643,Calls to UK landlines,01:00:02
        Nov12,01844 275281,Calls to UK landlines,01:03:29
        Oct10,01684 491756,Calls to UK landlines,11:31:15
        Nov18,01905 420764,Calls to UK landlines,00:25:58
        Nov18,01491 634643,Calls to UK landlines,00:00:03
    """)

main()
