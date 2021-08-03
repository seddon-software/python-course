from scipy.stats import norm
import numpy as np

def greeks(call_or_put, option, stockPrice, strikePrice, timeUntilExpiry, riskFreeInterestRate, volativity):
    id = call_or_put + " " + option 
    S = stockPrice
    K = strikePrice
    t = timeUntilExpiry
    r = riskFreeInterestRate / 100.0
    sigma = volativity / 100.0
    days_per_year = T = 365.25
    
    d1 = ( np.log(S/K) + (r + sigma**2/2.0)*t ) / (sigma * t**0.5)
    d2 = d1 - sigma * t**0.5
    
    def cumulativeStandardNormalDistribution(d):
        return norm.cdf(d)
    
    def normalProbabilityDensityFunction():
        return np.exp(-d1**2/2) / (2 * np.pi)**0.5
    
    # define abbreviations for functions
    npdf = normalProbabilityDensityFunction
    N = cumulativeStandardNormalDistribution
    
    def format(data):
        return "{:12s}: {:5f}".format(id, data)
    def formula():
        if(call_or_put == "call"): return format(S * N(d1) - K * np.exp(-r*t) * N(d2))
        if(call_or_put == "put"):  return format(K * np.exp(-r*t) * N(-d2) - S * N(-d1))
    def delta():
        if(call_or_put == "call"): return format(N(d1))
        if(call_or_put == "put"):  return format(N(d1) - 1)
    def gamma():
        if(call_or_put == "put"):  return format((1.0/(S * sigma * t**0.5)) * npdf())
    def rho():
        if(call_or_put == "call"): return format(+K * t * np.exp(-r*t) * N(+d2) / 100)
        if(call_or_put == "put"):  return format(-K * t * np.exp(-r*t) * N(-d2) / 100)
    def theta():
        if(call_or_put == "call"): return format((-S * sigma * npdf() / (2 * t**0.5) - r * K * np.exp(-r*t) * N(+d2)) / T)
        if(call_or_put == "put"):  return format((-S * sigma * npdf() / (2 * t**0.5) + r * K * np.exp(-r*t) * N(-d2)) / T)
    def vega():
        return format(S * t**0.5 * npdf() / 100)
    
    if option == "": return formula()
    if option == "delta":  return delta()
    if option == "gamma":  return gamma()
    if option == "rho":  return rho()
    if option == "theta": return theta()
    if option == "vega": return vega()

