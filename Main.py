from AmerOPs import CRRPricer_A
from PricePath import pricePaths
from KDE import KDE_profit
import matplotlib.pyplot as plt

if __name__ == "__main__":


#stimulated profit and loses at various volatility with 20% volatility excercise boundary
    T = 1; S0 = 10; mu = 0.05; sigma =  0.2; r = 0.02; N = 5000; paths = 100; K = 10
    dt = T/N
    crr, exercise_boundary = CRRPricer_A(T, S0, mu, sigma, r, N, K)
    #stimulated price paths
    S = pricePaths(T, S0, K, mu, sigma, r, N, paths)
    #profit and loses
    PL20 = KDE_profit(crr, exercise_boundary, S, K, r, dt)
    #profit and loses plot for 20% volatility
    PL = PL20.drop(columns=["row_num"])
    ax = PL.plot(kind='kde')
    plt.show()

    #Stimulate price paths for various realized volatility 
    S10 = pricePaths(T, S0, K, mu, 0.1, r, N, paths)
    S15 = pricePaths(T, S0, K, mu, 0.15, r, N, paths)
    S25 = pricePaths(T, S0, K, mu, 0.25, r, N, paths)
    S30 = pricePaths(T, S0, K, mu, 0.3, r, N, paths)

    #Calculate Profit and Loses with different realized volatility and appling 20% volatility trading strategy
    PL10 = KDE_profit(crr, exercise_boundary, S10, K, r, dt)
    PL15 = KDE_profit(crr, exercise_boundary, S15, K, r, dt)
    PL25 = KDE_profit(crr, exercise_boundary, S25, K, r, dt)
    PL30 = KDE_profit(crr, exercise_boundary, S30, K, r, dt)

    df = PL10.merge(PL15,how ='left', on = 'row_num').merge(PL20,how ='left', on = 'row_num').merge(PL25,how ='left', on = 'row_num').merge(PL30,how ='left', on = 'row_num')
    df.columns = ["row_num","PL10","PL15","PL20","PL25", "PL30"]
    df.drop(["row_num"], axis = 1, inplace = True)
    print(df)
    ax = df.plot(kind='kde')
    plt.show()



'''
#Exercise Boundaries with varying volatilities and varying risk free interest rates   

    sigmas = [0.1, 0.15, 0.2, 0.25, 0.3]
    risk_free_rates = [0.005, 0.02, 0.035, 0.05]

    for sigma in sigmas:
        CRRPricer_A(1, 10, 0.05, sigma, 0.02, 5000, 10)
    for rate in risk_free_rates:
        CRRPricer_A(1, 10, 0.05, 0.2, rate, 5000, 10)

'''



