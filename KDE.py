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
    
    data = {'AmerPut_Val': AmerPut_Val}
    PL = pd.DataFrame(data)
    PL['row_num'] = PL.reset_index().index
    PL = PL[["row_num","AmerPut_Val"]]

    return PL

def KDE_time():

    return 0