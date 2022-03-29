'''
python -m pip install lmfit

'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import exp, pi, sqrt
from scipy.signal import find_peaks
from lmfit.models import GaussianModel, LinearModel


# Define Gaussian for fit
def gaussian(x, amplitude, center, width):
    return (amplitude / (sqrt(2*pi) * width)) * exp(-(x-center)**2 / (2*width**2))

# Define function to open data file
def Read_Two_Column_File(file_name):
    df = pd.read_csv(file_name, sep='[ \t]+', index_col=False, names=['x', 'y'])
    return df

# Open the data as a Pandas dataframe
df = Read_Two_Column_File('data/XRF_giallo_napoli_01_spectrum.txt')

#plot the data
plt.plot(df['x'], df['y'], 'b-', label='XRF giallo napoli 01')



peaks, properties = find_peaks(df['y'], prominence=70)
print("the peaks are: ", peaks)
print("properties: ", properties)
plt.vlines(x=[df['x'][peaks]], ymin=0, ymax=4500)

# fit the data using Gaussian model
peak = GaussianModel()
background = LinearModel()
model = peak + background

# paramenters for the fitting model
params = model.make_params(amplitude=1000, center=10.5, width=1, intercept=1, slope=0)

result = model.fit(df['y'], params, x=df['x'])
print(result.fit_report())

plt.plot(df['x'], df['y'], 'b-', label='data')
plt.plot(df['x'], result.best_fit, 'r-', label='fitted data')
plt.legend()
plt.show()

