import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
T = 1; S0 = 10; mu = 0.05; sigma = 0.2; r = 0.02; N = 500; K = 10
dt = T/N

#The up and down factors
u = np.exp(r*dt + sigma*np.sqrt(dt))
d = 1/u

# probability of up and down moves
pu = 0.5*(1+((mu - r - 0.5*(sigma**2))/sigma)*np.sqrt(dt))
pd = 1 - pu

#Risk neutral probability measure q  
q = 0.5*(1-0.5*sigma*np.sqrt(dt))

#Building the binomial price tree
priceTree =  np.full((N, N), np.nan)
priceTree[0,0] = S0

for i in range(1, N):
    priceTree[0:i, i] = priceTree[0:i, (i-1)]* u
    priceTree[i, i] = priceTree[i-1, i-1] * d

# Build the option value tree
optionTree = np.full_like(priceTree, np.nan)
optionTree[:,-1] = np.maximum(K- priceTree[:,-1], 0)

discountfactor = np.exp(-r*dt)

backSteps = optionTree.shape[1] - 1

for i in range(backSteps, 0, -1):
    optionTree[0:i,i-1] = discountfactor * (q*optionTree[0:i, i]+(1-q)*optionTree[1:i+1, i])
    optionTree[0:i, i] = np.maximum(K - priceTree[0:i, i], optionTree[0:i, i])

#finding the optimum exercise prices
stoppingRegion = np.full_like(priceTree, np.nan)
B_i = []
eps_star = K * (10**-5)
for i in range(0, N):
    for j in range(0, N):
        optionPrice = optionTree[j,i]
        price = priceTree[j,i]
        if (np.abs(optionTree[j,i]-K+priceTree[j,i]) <  eps_star and np.isnan(optionTree[j,i]) == False):
            stoppingRegion[j,i] = priceTree[j,i] 
        else:
            pass
    B_i.append(np.nanmax(stoppingRegion[:,i]))

#plotting the exercise boundary

plt.plot(B_i, label = 'Exercise Boundary')
plt.axhline(y = K, color = 'r', label = 'Strike Price')
plt.legend()
plt.title('Exercise boundary for an American Put option with Strike 10')
plt.xlabel('Time Steps')
plt.ylabel('Option Price, P(t)')
plt.show()

#finding the hedge positions for the S Asset
hedge_position = np.full_like(priceTree, np.nan)

for i in range(1, N):
    hedge_position[0:i, i-1] = (optionTree[0:i, i]-optionTree[1:i+1, i])/(priceTree[0:i,i-1]*(u-d)*np.exp(r*dt))
    #print("\n", hedge_position)

hedgetimes = [0, 0.25, 0.5, 0.75]
hedgetimes2 = list(map(lambda x: x*N, hedgetimes))

for i in hedgetimes2:
    print(priceTree[:,int(i)])
    plt.plot(priceTree[:,int(i)], hedge_position[:,int(i)], label = f't ={hedgetimes[hedgetimes2.index(i)]}')

plt.xlabel('Stock Price')
plt.ylabel(r'$\alpha$')
plt.title('Position in asset S for different time periods, t ')
plt.legend()
plt.show()
