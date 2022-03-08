'''
Olympic Golds
=============

This example shows how to filter data from a dataframe.  Out objective is the print out the countries that
won more gold medals than South Korea.

First we read data into the dataframe "medal_table".  A sample of this file is:
            2012 Summer Olympics medal table
            Rank   Country       Id   Gold  Silver  Bronze  Total
            1    United States  (USA)    46    28     29   103
            2    China          (CHN)    38    28     22    88
            3    Great Britain  (GBR)    29    17     19    65
            4    Russia         (RUS)    24    25     32    81
            5    South Korea    (KOR)    13     8      7    28

As you can see, we should ignore the first line of the file.  The field separator is tricky; clearly we should
specify at least 2 spaces, because the country names have spaces, but later in the file we see: 
            19   Czech Republic (CZE)     4     3      3    10

In this line, there is only one space between the Country name and the Id.  The solution is to include the 
brackets in the separator.  Hence we choose:
            sep = '[ )(]{2,}'

which states the separator is a space, ( or ) in any order, repeated 2 or more times.  The repeat count of 2
or more is specified by
            {2,}

The first problem id to determine South Korean golds:
            korean_golds = medal_table[medal_table.Id == "KOR"]["Gold"].values[0]

Here, 
            medal_table[medal_table.Id == "KOR"]

selects rows with Id == "KOR".  But we only want to value of the Gold column, hence
            medal_table[medal_table.Id == "KOR"]["Gold"]

Unfortunately this returns
            4   13

where 4 is the index and 13 is the number of golds that we want.  When we try
            medal_table[medal_table.Id == "KOR"]["Gold"].values

we get
            [13]

which is a Numpy array.  This is nearly what we want; we just need the first element of this array and the
following does the trick:
            medal_table[medal_table.Id == "KOR"]["Gold"].values[0]

Now all we have to do is extract rows where the number of gold is greater than 13 to form a new dataframe with 
just 2 columns ("Country" and "Gold"):
            result = medal_table[medal_table["Gold"] > korean_golds][["Country", "Gold"]]

You'll find that this result also includes the index field.  Fortunately, you can use
            print(result.to_string(index=False))

to supress printing the index.
'''

import pandas as pd
import pylab as pl
pd.set_option('display.width', 100)



def main():
    # read in medal table (n.b. delimiters contain at least 2 spaces and sometimes a bracket) 
    medal_table = pd.read_csv("data/olympics_2012_medal_table.txt",
                               engine = 'python',
                               skiprows = 1,
                               sep = '[ )(]{2,}')
    
    korean_golds = medal_table[medal_table.Id == "KOR"]["Gold"].values[0]
    print(korean_golds, type(korean_golds))
    print(f"South Korea earned {korean_golds} golds")
    print("\nCountries with more golds than South Korea:")
    result = medal_table[medal_table["Gold"] > korean_golds][["Country", "Gold"]]
    print(result.to_string(index=False))
main()
