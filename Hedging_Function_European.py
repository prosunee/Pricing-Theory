# Hedging_in_a_function
import numpy as np
import matplotlib.pyplot as plt

def Hedge_Position  (TimeToExpiry, InitialPrice, mu, sigma, RiskfreeRate, TotalSteps, StrikePrice): 

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

    #finding the hedge positions for the S Asset
    hedge_position = np.full_like(priceTree, np.nan)
    hedge_position[0, 0] = (optionTree[1, 0]-optionTree[1, 1])/(priceTree[0,0]*(np.exp(sigma*np.sqrt(dt))-np.exp(-sigma*np.sqrt(dt)))*np.exp(RiskfreeRate*dt))

    for i in range(1, TotalSteps):
        hedge_position[0:i, i-1] = (optionTree[0:i, i]-optionTree[1:i+1, i])/(priceTree[0:i,i-1]*(np.exp(sigma*np.sqrt(dt))-np.exp(-sigma*np.sqrt(dt)))*np.exp(RiskfreeRate*dt))
        #print("\n", hedge_position)

    hedgetimes = [0, 0.25, 0.5, 0.75]
    hedgetimes2 = list(map(lambda x: x*TotalSteps, hedgetimes))

    for i in hedgetimes2:
        #print(priceTree[:,int(i)])
        plt.plot(priceTree[:,int(i)], hedge_position[:,int(i)], label = f't ={hedgetimes[hedgetimes2.index(i)]}')
    
    plt.xlabel('Stock Price')
    plt.ylabel(r'$\alpha$')
    plt.xlim(5, 20)
    plt.ylim( -1.25,0.25)
    plt.scatter(priceTree[0,0], hedge_position[0,0])
    plt.title('Position in asset S for different time periods, t, with European Option ')
    plt.legend()
    plt.savefig('Hedging_Strategy_Risky_Euro.png')
    plt.close()

    #finding the hedge positions for the B Asset
    B_price =  np.full_like(priceTree, np.nan)
    hedge_position_B = np.full_like(priceTree, np.nan)
    B_price[0, 0] = 1

    #finding the hedge positions for the B Asset
    B_price =  np.full_like(priceTree, np.nan)
    hedge_position_B = np.full_like(priceTree, np.nan)
    B_price[0, 0] = 1
    hedge_position_B[0, 0] = (optionTree[0,0]- hedge_position[0,0]*priceTree[0,0])/B_price[0,0]


    for i in range(1, TotalSteps):
        B_price[0:i, i] = np.exp(RiskfreeRate*i*dt)
        hedge_position_B[0:i, i] = (optionTree[0:i, i]- hedge_position[0:i,i]*priceTree[0:i,i])/B_price[0:i,i]
        #print("\n", hedge_position_B)
        
    for i in hedgetimes2:
        #print(priceTree[:,int(i)])
        plt.plot(priceTree[:, int(i)], hedge_position_B[:,int(i)], label = f't ={hedgetimes[hedgetimes2.index(i)]}')

    plt.xlabel('S Price')
    plt.ylabel(r'$\beta$')
    plt.xlim(5, 20)
    plt.ylim(-1,11)
    plt.scatter(priceTree[0,0], hedge_position_B[0,0])
    plt.title('Position in asset B for different time periods, t, with European Option ')
    plt.legend()
    plt.savefig('Hedging_Strategy_Rf_Euro.png')

if __name__ == "__main__":
        Hedge_Position(1, 10, 0.05, 0.2, 0.08, 5000, 10)
        