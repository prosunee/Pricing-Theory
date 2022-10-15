import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def KDE_profit(option_price, exercise_boundary, prices, strike_price, r, dt):
    
    S = prices[:,1:]

    exercise_prices = []; AmerPut_Val = []

    for i in range(len(S)):
        for j in range(len(S[0,:])):
            if (S[i,j] <= exercise_boundary[j,1]):
                exercise_prices.append([j+1, S[i,j]])
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

def KDE_time(exercise_boundary, prices, TimeSteps):
    S = prices[:,1:]
    exercise_times = []

    for i in range(len(S)):
        for j in range(len(S[0,:])):
            if (prices[i,j] <= exercise_boundary[j,1]):
                exercise_times.append(j+1)
                break
            else:
                pass
        
    data = {'Exercise Times': exercise_times}
    ex_times = pd.DataFrame(data)
    ex_times['row_num'] = ex_times.reset_index().index
    ex_times = ex_times[["row_num", "Exercise Times"]]

    return ex_times

    return 0