import pandas as pd
import pylab as pl
import codecs
import re
from copy import deepcopy
from matplotlib.backends.backend_pdf import PdfPages

FILENAME = "results/guildford_2016.txt"
# FILENAME = "results/guildford_2015.txt"
# FILENAME = "results/bournemouth_2016.txt"
# FILENAME = "results/berks_and_bucks_2016.txt"
# FILENAME = "results/berks_and_bucks_2015.txt"
# FILENAME = "results/reading_29_sep_16.txt"

pl.rcParams['font.family'] = 'Arial Unicode MS'
xticks = ["VOID", "PO",
          "1♣", "1♦", "1♥", "1♠", "1NT", 
          "2♣", "2♦", "2♥", "2♠", "2NT",
          "3♣", "3♦", "3♥", "3♠", "3NT",
          "4♣", "4♦", "4♥", "4♠", "4NT",
          "5♣", "5♦", "5♥", "5♠", "5NT",
          "6♣", "6♦", "6♥", "6♠", "6NT",
          "7♣", "7♦", "7♥", "7♠", "7NT",
          ]

def setOptions():
    pd.set_option('display.precision', 1)
    pd.set_option('display.width', 100)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # pd.describe_option('display')
    
def set_title(title):
    figure = pl.gcf()
    event = re.split('[/.]', FILENAME)[1]
    title = event + " : " + title
    figure.canvas.set_window_title(title)
    figure.suptitle(title, fontsize=14, fontweight='bold')

def createDataFrames():
    df = pd.read_csv(FILENAME)

    # create new columns
    df['doubled'] = df.apply(lambda row:row['bid'][-1:] == '*', raw = True, axis = 1)
    df['redoubled'] = df.apply(lambda row:row['bid'][-2:] == '**', raw = True, axis = 1)

    # drop columns we are not using
    df.drop(['by', 'lead', 'NS_pts', 'EW_pts'], axis = 1, inplace = True)
    
    # return data frames
    undoubled = df
    doubled = df[df.doubled == True]
    redoubled = df[df.redoubled == True]
    return undoubled, doubled, redoubled

def plot(pdf, title, df):    
    ticks = deepcopy(xticks)
    def frequency(bid):
        try:
            y.append(100*len(df[df.bid == bid]) / len(df))
        except:
            y.append(0.0)
            
    y = []
    fig = pl.figure(figsize=(20,10))
    fig = pl.figure(figsize=(10,5))
    x = list(range(len(ticks)))
    if title == "Undoubled Contracts": stars = ""
    if title == "Doubled Contracts":   stars = "*" 
    if title == "Redoubled Contracts": stars = "**" 

    for bid in ticks:
        frequency(bid + stars)

    pl.xticks(x, ticks)
    set_title(title)
    pl.bar(x, y, align='center')
    pdf.savefig()
    pl.show()
    return pl
    
setOptions()
undoubled, doubled, redoubled = createDataFrames()
event = re.split('[/.]', FILENAME)[1] + '.pdf'

with PdfPages("pdf/" + event) as pdf:
    plot(pdf, "Undoubled Contracts", undoubled)
    plot(pdf, "Doubled Contracts", doubled)
    plot(pdf, "Redoubled Contracts", redoubled)

