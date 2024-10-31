import pandas as pd

'''
Using and sorting a multi-column index
'''

def main(): 
    df = pd.read_csv("data/phone_extensions.txt", sep=r"\s+", engine="python")
    df.set_index(['FirstName', 'LastName'])
    df.sort_values(['LastName', 'FirstName'], inplace=True)
    print(df)

main()
