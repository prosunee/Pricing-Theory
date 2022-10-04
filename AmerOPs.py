import numpy as np

# Initialize parameters
T = 0.5; S0 = 80; mu = 0.05; sigma = 0.2; r = 0.05; N = 20000; K = 100
dt = T/N

#The up and down factors
u = np.exp(r*dt + sigma*np.sqrt(dt))
d = 1/u

# probability of up and down moves
pu = 0.5*(1+((mu - r - 0.5*(sigma**2))/sigma)*np.sqrt(dt))
pd = 1 - pu

#Risk neutral probability measure q  
q = (np.exp(r*dt)-np.exp(-sigma*np.sqrt(dt)))/(np.exp(sigma*np.sqrt(dt))-np.exp(-sigma*np.sqrt(dt)))

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

print(optionTree[0,0])

stoppingRegion = np.full_like(priceTree, np.nan)
