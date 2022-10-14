import numpy as np
import matplotlib.pyplot as plt

def pricePaths(TimeToExpiry, InitialPrice, StrikePrice, mu, sigma, RiskfreeRate, TotalSteps, N_paths):

    # Initialize parameters
    # Calculate the length of each time increment
    dt = TimeToExpiry/TotalSteps

    # risk neutral probability of an up move
    pu = 0.5*(1+((mu - RiskfreeRate - 0.5*(sigma**2))/sigma)*np.sqrt(dt))

    #initialize matrix which contains all the paths
    S = np.full((N_paths, TotalSteps + 1), np.nan)
    #1st column of the price matrix is the initial price
    S[:,0] = InitialPrice

    #Each succesive column is calculated using the CRR model for the price
    for n in range(TotalSteps):
        
        U = np.random.rand(N_paths)
        x = 1*(U < pu) -1 * (U >= pu)

        S[:,n+1] = S[:,n] * np.exp(RiskfreeRate*dt + sigma * np.sqrt(dt)*x)

    return S
