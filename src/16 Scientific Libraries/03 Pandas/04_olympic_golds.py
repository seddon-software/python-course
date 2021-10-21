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
