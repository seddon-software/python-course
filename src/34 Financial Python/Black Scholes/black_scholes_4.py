from greeks import greeks

parameters = {
    'stockPrice' : 31.55, 
    'strikePrice' : 22.75, 
    'timeUntilExpiry' : 3.5, 
    'riskFreeInterestRate' : 5.0, 
    'volativity' : 50.0
}

print(greeks("call", "",      **parameters))
print(greeks("put",  "",      **parameters))
print(greeks("call", "delta", **parameters))
print(greeks("put",  "delta", **parameters))
print(greeks("put",  "gamma", **parameters))
print(greeks("call", "theta", **parameters))
print(greeks("put",  "theta", **parameters))
print(greeks("call", "rho",   **parameters))
print(greeks("put",  "rho",   **parameters))
print(greeks("put",  "vega",  **parameters))
