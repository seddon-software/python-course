import pandas as pd
import numpy as np
pd.set_option('display.precision', 1)
pd.set_option('display.width', None)        # None means all data displayed
pd.set_option('display.max_rows', None)

'''
Calculate the total time of all phone calls, taken from datafile
'''

def main(): 
    column_names = ['A', 'B', 'time', 'D', 'E']
    df = pd.read_csv("data/phonecalls.dat", 
                               skiprows = 14,
                               engine = 'python',
                               names = column_names, 
                               sep = '(£|Calls to UK landlines|calls|mobiles)')
    
# extract time column and split into hours, mins, secs
    df2 = df['time'].str.split(':',expand=True)
    df2.columns = ['hour','min','sec']
    df2 = df2.astype('int')
    hours, mins, secs = df2[['hour', 'min','sec']].sum()

    def convertTime(hours, mins, secs):
        mins += secs // 60
        secs = secs % 60
        hours += mins//60
        mins = mins %60
        print(f"Total time = {hours:02}:{mins:02}:{secs:02}")    

    convertTime(hours, mins, secs)

main()
