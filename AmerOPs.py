import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def CRRPricer_A(TimeToExpiry, InitialPrice, mu, sigma, RiskfreeRate, TotalSteps, StrikePrice): 

    # Initialize parameters
    # Calculate the length of each time increment
    dt = TimeToExpiry/TotalSteps

    #Change of price going up/down
    u = np.exp(RiskfreeRate*dt + sigma*np.sqrt(dt))
    d = np.exp(RiskfreeRate*dt - sigma*np.sqrt(dt))

    # probability of an up move
    pu = 0.5*(1+((mu - RiskfreeRate - 0.5*(sigma**2))/sigma)*np.sqrt(dt))
    # probabiluty of a down move
    pd = 1 - pu
    # Risk neutral probability measure q
    q = 0.5*(1-0.5*sigma*np.sqrt(dt))

    # Building the binomial price tree
    # Create an array full of nan to store the stock prices
    priceTree =  np.full((TotalSteps, TotalSteps), np.nan)
    priceTree[0,0] = InitialPrice

    for ii in range(1, TotalSteps):
        # For each time increment, calculate the evolved up price vector at t
        priceTree[0:ii, ii] = priceTree[0:ii, (ii-1)]* u
        # However, there is the case at the bottom of the tree at any t that is only obtained by going down one step
        priceTree[ii, ii] = priceTree[(ii-1), (ii-1)] * d

    # Build the option value tree
    optionTree = np.full_like(priceTree, np.nan)
    exercise_boundary = np.full((TotalSteps,2), np.nan)

    # Start with the terminal value
    # Implement the put option formula for the last vector representing the option value at the end of Total Period
    optionTree[:,-1] = np.maximum(0, StrikePrice - priceTree[:,-1])

    # Discount rate for each time increment, by the rate that numirare asset changes
    discountfactor = np.exp(-RiskfreeRate*dt)

    backSteps = optionTree.shape[1] - 1

    for ii in range(backSteps, 0, -1):
        optionTree[0:ii,ii-1] = \
            discountfactor * \
            (q * optionTree[0:ii, ii] \
            + (1-q) * optionTree[1:ii + 1, ii])
        
        optionTree[0:ii, ii] = np.maximum(StrikePrice - priceTree[0:ii, ii], optionTree[0:ii, ii])
        
        # Try to record the first time it becomes optimal to exercise the option rather than holding it
        exercise_decision = 0
        # We keep increasing the decision 'spot' in each ii vector until we find it better to exercise, i.e. 
        # The option value because smaller than the exercise return
        while optionTree[exercise_decision,ii] > (StrikePrice - priceTree[exercise_decision, ii]):
            exercise_decision += 1
        
        # We record this position of first exercise decision for each step ii
        exercise_boundary[ii,0] = exercise_decision
        exercise_boundary[ii,1] = priceTree[exercise_decision,ii]

    print(exercise_boundary)
    plt.plot(exercise_boundary[:,1])
    plt.title('Exercise Boundary')
    plt.xlabel('Time Increments')
    plt.ylabel('Stock Price at t')
    plt.savefig('Exercise_Boundary_Time.png')

    return(optionTree[0,0])

    stoppingRegion = np.full_like(priceTree, np.nan)

if __name__ == "__main__":
        crr = CRRPricer_A(1, 10, 0.05, 0.2, 0.02, 5000, 10)
        print(crr)