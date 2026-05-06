import numpy as np
import pandas as pd
import pylab as pl

from io import StringIO

def main():
    # get test data embedded in this script
    test_data = get_test_data()
    df = pd.read_csv(test_data, sep="[ ]+", engine = 'python')
    df[['year', 'month']] = df[['year', 'month']].astype(int)
    df[['tmax', 'tmin']] = df[['tmax', 'tmin']].astype(float)

    df['quarters'] = df.apply(lambda x : "{:.0f}'Q{}".format(x.year, int(x.month+2)//3), axis = 1)
    averages = df.groupby('quarters').aggregate(np.mean)
    averages.plot(figsize=(16, 8), title = 'Average Temperatures', y = ['tmin', 'tmax'], color = ['red', 'cyan'], kind = 'bar')
    pl.show()


def get_test_data():
    return StringIO("""
       year month tmax    tmin air-frost-days rain(mm) sun(hours)
    
       2012   1    9.8     3.6              6    34.6    85.7
       2012   2    7.3     1.2             12    21.3    71.7
       2012   3   14.0     3.6              2    24.3   164.3
       2012   4   12.6     4.6              2   143.0   135.1 
       2012   5   17.7     9.7              0    55.5   185.6 
       2012   6   18.9    11.6              0   151.7   128.3 
       2012   7   20.5    12.6              0   100.0   178.2 
       2012   8   21.8    13.6              0    85.6   168.4 
       2012   9   18.4     9.2              0    57.6   173.2
       2012  10   13.4     7.1              0   124.2    85.5
       2012  11   10.1     4.2              1    83.3    74.0
       2012  12    8.6     2.6              9   103.3    61.7
       2013   1    6.4     1.9             14    58.5    47.8
       2013   2    6.2     0.9              5    47.4    72.3
       2013   3    6.3     0.2             16    76.6    60.7
       2013   4   12.9     3.9              6    24.8   177.0
       2013   5   15.9     6.7              0    66.2   193.6
       2013   6   19.3    10.2              0    17.3   181.3
       2013   7   25.5    13.9              0    45.7   297.3
       2013   8   23.1    13.1              0    19.3   205.9
       2013   9   19.0     9.9              0    40.6   123.1
       2013  10   16.3     9.9              0    86.5   101.8 
       2013  11    9.9     3.8              2    55.2    85.7 
       2013  12   10.0     3.6              0    97.7    63.6 
       2014   1    9.3     3.5              3   146.9    77.7 
       2014   2    9.7     4.2              0    90.1    97.4 
       2014   3   12.8     3.5              2    39.2   135.6 
       2014   4   15.0     6.4              0    50.2   149.5 
       2014   5   17.1     8.9              0    90.3   185.7 
       2014   6   21.5    11.8              0    36.9   236.3 
       2014   7   24.9    13.5              0    45.5   264.6 
       2014   8   20.8    11.7              0    85.6   190.5 
       2014   9   21.1    11.4              0     4.1   143.7 
       2014  10   16.8     9.9              0    65.6   116.9 
       2014  11   11.5     5.7              2    98.6    60.9 
       2014  12    8.7     2.4              9    44.0    96.9 
    """)


main()
