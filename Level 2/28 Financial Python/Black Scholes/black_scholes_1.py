from scipy.stats import norm
import numpy as np

def N(d):  # Cumulative Standard Normal Distribution
    return norm.cdf(d)

def npdf(): # Normal Probability Density Function
    return np.exp(-d1**2/2) / (2 * np.pi)**0.5

stockPrice = S = 31.55
strikePrice = K = 22.75
timeUntilOptionExpiresInYears = t = 3.5
riskFreeInterestRate = r = 5.0 / 100.0
volitivity = sigma = 50.0 / 100.0
days_per_year = T = 365.25
d1 = ( np.log(S/K) + (r + sigma**2/2.0)*t ) / (sigma * t**0.5)
d2 = d1 - sigma * t**0.5

CallOption = S * N(d1) - K * np.exp(-r*t) * N(d2)
PutOption = K * np.exp(-r*t) * N(-d2) - S * N(-d1)
CallDelta = N(d1)
PutDelta = N(d1) - 1
PutGamma = (1.0/(S * sigma * t**0.5)) * npdf()
CallTheta = (-S * sigma * npdf() / (2 * t**0.5) - r * K * np.exp(-r*t) * N(+d2)) / T
PutTheta  = (-S * sigma * npdf() / (2 * t**0.5) + r * K * np.exp(-r*t) * N(-d2)) / T
PutVega = S * t**0.5 * npdf() / 100
CallRho =  K * t * np.exp(-r*t) * N(+d2) / 100
PutRho  = -K * t * np.exp(-r*t) * N(-d2) / 100

print("CallOption = {:.3f}".format(CallOption))
print("PutOption = {:.3f}".format(PutOption))
print("CallDelta = {:.3f}".format(CallDelta))
print("PutDelta = {:.3f}".format(PutDelta))
print("PutGamma = {:.6f}".format(PutGamma))
print("CallRho = {:.6f}".format(CallRho))
print("PutRho = {:.6f}".format(PutRho))
print("CallTheta = {:.6f}".format(CallTheta))
print("PutTheta = {:.6f}".format(PutTheta))
print("PutVega = {:.6f}".format(PutVega))
