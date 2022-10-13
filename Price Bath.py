import numpy as np
import matplotlib.pyplot as plt


def CRRPricer_A(TimeToExpiry, InitialPrice, mu, sigma, RiskfreeRate, TotalSteps, StrikePrice): 

    # Initialize parameters
    # Calculate the length of each time increment
    dt = TimeToExpiry/TotalSteps

    #Change of price going up/down
    u = np.exp(RiskfreeRate*dt + sigma*np.sqrt(dt))
    d = np.exp(RiskfreeRate*dt - sigma*np.sqrt(dt))

    # risk neutral probability of an up move
    pu = 0.5*(1-0.5*sigma*np.sqrt(dt))*np.sqrt(dt)
    # risk neutral probabiluty of a down move
    pd = 1 - pu

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
            (pu * optionTree[0:ii, ii] \
            + pd * optionTree[1:ii + 1, ii])
        
        optionTree[0:ii, ii-1] = np.maximum(StrikePrice - priceTree[0:ii, ii-1], optionTree[0:ii, ii-1])
        
        # Try to record the first time it becomes optimal to exercise the option rather than holding it
        exercise_decision = 0
        # We keep increasing the decision 'spot' in each ii vector until we find it better to exercise, i.e. 
        # The option value because smaller than the exercise return
        while optionTree[exercise_decision,ii] > (StrikePrice - priceTree[exercise_decision, ii]):
            exercise_decision += 1
        
        # We record this position of first exercise decision for each step ii
        exercise_boundary[ii,0] = exercise_decision
        exercise_boundary[ii,1] = priceTree[exercise_decision,ii]

    #print(exercise_boundary)
    #plt.figure("Figure 1")
    #plt.plot(exercise_boundary[:,1], label = f'$\sigma = {sigma*100}$%')
    #plt.title('Exercise Boundary')
    #plt.xlabel('Time Increments')
    #plt.ylabel('Stock Price at t')
    #plt.show()
    #plt.savefig('Exercise_Boundary_Time.png')

    return(optionTree[0,0], exercise_boundary)

"""
    #finding the hedge positions for the S Asset
    hedge_position = np.full_like(priceTree, np.nan)

    for i in range(1, TotalSteps):
        hedge_position[0:i, i-1] = (optionTree[0:i, i]-optionTree[1:i+1, i])/(priceTree[0:i,i-1]*(u-d)*np.exp(RiskfreeRate*dt))
        #print("\n", hedge_position)

        hedgetimes = [0, 0.25, 0.5, 0.75]
        hedgetimes2 = list(map(lambda x: x*TotalSteps, hedgetimes))

        for i in hedgetimes2:
            #print(priceTree[:,int(i)])
            plt.plot(priceTree[:,int(i)], hedge_position[:,int(i)], label = f't ={hedgetimes[hedgetimes2.index(i)]}')

    plt.xlabel('Stock Price')
    plt.ylabel(r'$\alpha$')
    plt.title('Position in asset S for different time periods, t ')
    plt.legend()
    plt.show()

    return(optionTree[0,0])

"""

def pricePaths(TimeToExpiry, InitialPrice, StrikePrice, mu, sigma, RiskfreeRate, TotalSteps, N_paths):

    # Initialize parameters
    # Calculate the length of each time increment
    dt = TimeToExpiry/TotalSteps

    # risk neutral probability of an up move
    pu = 0.5*(1+((mu - RiskfreeRate - 0.5*(sigma**2))/sigma)*np.sqrt(dt))

    #initialize matrix which contains all the paths
    S = np.full((N_paths, TotalSteps + 1), np.nan)
    S[:,0] = InitialPrice

    for n in range(TotalSteps):
        
        U = np.random.rand(N_paths)
        x = 1*(U < pu) -1 * (U >= pu)

        S[:,n+1] = S[:,n] * np.exp(RiskfreeRate*dt + sigma * np.sqrt(dt)*x)
    
    AmerOption = np.maximum(StrikePrice - S, 0)

    for i in range(TotalSteps):
        AmerOption[:,i] = np.exp(-RiskfreeRate*dt*i) * AmerOption[:,i]

    plt.plot(S)
    plt.show()

    return S, AmerOption

if __name__ == "__main__":

    """
    sigmas = [0.1, 0.15, 0.2, 0.25, 0.3]
    risk_free_rates = [0.005, 0.02, 0.035, 0.05]

    for sigma in sigmas:
        crr, exercise_boundary = CRRPricer_A(1, 10, 0.05, sigma, 0.02, 5000, 10)

        plt.figure("Figure 1")
        plt.plot(exercise_boundary[:,1], label = f'$\sigma = {sigma*100}$%')

    plt.title('Exercise Boundary at different volatility levels')
    plt.xlabel('Time Increments')
    plt.ylabel('Stock Price at t')
    plt.legend()
    plt.show()
    plt.savefig("Exercise Boundary at different volatility levels")


    for rate in risk_free_rates:
        crr, exercise_boundary = CRRPricer_A(1, 10, 0.05, 0.2, rate, 5000, 10)


        plt.figure("Figure 2")
        plt.plot(exercise_boundary[:,1], label = f'rate = {rate}')
        
    plt.title('Exercise Boundary at different interest rate levels')
    plt.xlabel('Time Increments')
    plt.ylabel('Stock Price at t')
    plt.legend()
    plt.show()
"""
    S, AmerOption = pricePaths(1, 10, 10, 0.05, 0.2, 0.02, 5, 500)
    print(S)