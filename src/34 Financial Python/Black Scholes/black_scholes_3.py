from greeks import greeks

print(greeks("call", "", 31.55, 22.75, 3.5, 5.0, 50.0))
print(greeks("put",  "",                   \
             stockPrice           = 31.55, \
             strikePrice          = 22.75, \
             timeUntilExpiry      = 3.5,   \
             riskFreeInterestRate = 5.0,   \
             volativity           = 50.0))

print(greeks("call", "delta", stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))
print(greeks("put",  "delta", stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))

print(greeks("put",  "gamma", stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))

print(greeks("call", "theta", stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))
print(greeks("put",  "theta", stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))

print(greeks("call", "rho",   stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))
print(greeks("put",  "rho",   stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))

print(greeks("put",  "vega",  stockPrice = 31.55, strikePrice = 22.75, timeUntilExpiry = 3.5, riskFreeInterestRate = 5.0, volativity = 50.0))
