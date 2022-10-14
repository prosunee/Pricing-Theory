import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def KDE_profit(option_price, exercise_boundary, prices, strike_price, r, dt):
    
    exercise_prices = []; AmerPut_Val = []

    for i in range(len(prices)):
        for j in range(len(exercise_boundary)):
            if (prices[i,j] <= exercise_boundary[j,1]):
                exercise_prices.append([j, prices[i,j]])
                break
            else:
                pass


    for i in range(len(exercise_prices)):
        x = np.exp(-r*dt*exercise_prices[i][0])*(strike_price-exercise_prices[i][1]) - option_price
        AmerPut_Val.append(x)

    if len(AmerPut_Val) < len(prices):
        AmerPut_Val.extend([-option_price]*(len(prices)-len(AmerPut_Val)))
    else:
        pass

    AmerPut_Val = pd.DataFrame(AmerPut_Val)

    ax = AmerPut_Val.plot(kind='hist')
    AmerPut_Val.plot(kind='kde', secondary_y= True)
    plt.show()
    
    return AmerPut_Val

def KDE_time():

    return 0