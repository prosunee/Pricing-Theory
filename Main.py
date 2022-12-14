from AmerOPs import CRRPricer_A
from PricePath import pricePaths
from KDE import KDE_profit, KDE_time
import matplotlib.pyplot as plt
import random 

if __name__ == "__main__":
    random.seed(10)
    T = 1; S0 = 10; mu = 0.05; sigma =  0.2; r = 0.02; N = 5000; paths = 100; K = 10
    dt = T/N

    """
    #Vary Parameters for PL and time plots
    crr, exercise_boundary = CRRPricer_A(T, S0, mu, sigma, r, N, K)
    #stimulated price paths
    S = pricePaths(T, S0, K, mu, sigma, r, N, paths)
    #profit and loses
    PL20, PL20_2 = KDE_profit(crr, exercise_boundary, S, K, r, dt)
    T20 = KDE_time(exercise_boundary, S, N)

    
    T = PL20_2.drop(columns=["row_num"])
    T.columns = [r'$\sigma$ =0.2']
    ax = T.plot(kind='kde')
    plt.xlabel = ("Profit and Loss")
    plt.show()
     

    #Parameter mu 0.02, 0.08
    crrmu2, exercise_boundarymu2 = CRRPricer_A(T, S0, 0.02, sigma, r, N, K)
    Smu1 = pricePaths(T, S0, K, 0.01, sigma, r, N, paths)
    Smu2 = pricePaths(T, S0, K, 0.02, sigma, r, N, paths)
    Smu8 = pricePaths(T, S0, K, 0.08, sigma, r, N, paths)
    
    PLmu2, PLmu2_2 = KDE_profit(crrmu2, exercise_boundarymu2, Smu2, K, r, dt)


    df = PLmu1.merge(PLmu2,how ='left', on = 'row_num').merge(PL20,how ='left', on = 'row_num')
    df.columns = ["row_num",r'$\mu$ =0.01',r'$\mu$ =0.02',r'$\mu$ =0.05']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel("Profit and Loss")
    plt.show()
    

    df2 = PLmu1_2.merge(PLmu2_2, how = 'left', on = 'row_num').merge(PL20_2, how = 'left', on = 'row_num')
    df2.columns = ["row_num",r'$\mu$ =0.01',r'$\mu$ =0.02',r'$\mu$ =0.05']
    df2.drop(["row_num"], axis = 1, inplace = True)
    ax2 = df2.plot(kind = 'kde')
    plt.xlabel = ("Profit and Loss")
    plt.show()

    Tmu2 = KDE_time(exercise_boundarymu2, Smu2, N)
    df = Tmu1.merge(Tmu2,how ='left', on = 'row_num').merge(T20,how ='left', on = 'row_num')
    df.columns = ["row_num",r'$\mu$ =0.01',r'$\mu$ =0.02',r'$\mu$ =0.05']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel = ("Time")
    plt.show()


    #Parameter sigma 0.1,0.3
    crrv1, exercise_boundaryv1 = CRRPricer_A(T, S0, mu, 0.1, r, N, K)
    crrv3, exercise_boundaryv3 = CRRPricer_A(T, S0, mu, 0.3, r, N, K)
    Sv1 = pricePaths(T, S0, K, mu, 0.1, r, N, paths)
    Sv3 = pricePaths(T, S0, K, mu, 0.3, r, N, paths)

    PLv1, PLv1_2 = KDE_profit(crrv1, exercise_boundaryv1, Sv1, K, r, dt)
    PLv3, PLv3_2 = KDE_profit(crrv3, exercise_boundaryv3, Sv3, K, r, dt)

    df = PLv1.merge(PL20,how ='left', on = 'row_num').merge(PLv3,how ='left', on = 'row_num')
    df.columns = ["row_num",r'$\sigma$ =0.1',r'$\sigma$ =0.2',r'$\sigma$ =0.3']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel("Profit and Loss")
    plt.show()

    df2 = PLv1_2.merge(PL20_2,how ='left', on = 'row_num').merge(PLv3_2,how ='left', on = 'row_num')
    df2.columns = ["row_num",r'$\sigma$ =0.1',r'$\sigma$ =0.2',r'$\sigma$ =0.3']
    df2.drop(["row_num"], axis = 1, inplace = True)
    ax2 = df2.plot(kind='kde')
    plt.xlabel = ("Profit and Loss")
    plt.show()

    
    Tv1 = KDE_time(exercise_boundaryv1, Sv1, N)
    Tv3 = KDE_time(exercise_boundaryv3, Sv3, N)
    df = Tv1.merge(T20,how ='left', on = 'row_num').merge(Tv3,how ='left', on = 'row_num')
    df.columns = ["row_num",r'$\sigma$ =0.1',r'$\sigma$ =0.2',r'$\sigma$ =0.3']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel("Time")
    plt.show()
    

    #Parameter r 0.05,0.08
    crrr5, exercise_boundaryr5 = CRRPricer_A(T, S0, mu, sigma, 0.05, N, K)
    crrr8, exercise_boundaryr8 = CRRPricer_A(T, S0, mu, sigma, 0.08, N, K)
    Sr5 = pricePaths(T, S0, K, mu, sigma, 0.05, N, paths)
    Sr8 = pricePaths(T, S0, K, mu, sigma, 0.08, N, paths)
    
    PLr5, PLr5_2 = KDE_profit(crrr5, exercise_boundaryr5, Sr5, K, r, dt)
    PLr8, PLr8_2 = KDE_profit(crrr8, exercise_boundaryr8, Sr8, K, r, dt)


    df = PL20.merge(PLr5,how ='left', on = 'row_num').merge(PLr8,how ='left', on = 'row_num')
    df.columns = ["row_num",r'r =0.02',r'r =0.05',r'r =0.08']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel("Profit and Loss")
    plt.show()
    
    df2 = PL20.merge(PLr5_2,how ='left', on = 'row_num').merge(PLr8_2,how ='left', on = 'row_num')
    df2.columns = ["row_num",r'r =0.02',r'r =0.05',r'r =0.08']
    df2.drop(["row_num"], axis = 1, inplace = True)
    ax2 = df2.plot(kind = 'kde')
    plt.xlabel = ("Profit and Loss")
    plt.show()
    Tr5 = KDE_time(exercise_boundaryr5, Sr5, N)
    Tr8 = KDE_time(exercise_boundaryr8, Sr8, N)
    df = T20.merge(Tr5,how ='left', on = 'row_num').merge(Tr8,how ='left', on = 'row_num')
    df.columns = ["row_num",r'r =0.02',r'r =0.05',r'r =0.08']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel = ("Time")
    plt.show()
    '''

    """

#Parameters T = 0.5, T = 2
    crr, exercise_boundary = CRRPricer_A(T, S0, mu, sigma, r, N, K)
    #stimulated price paths
    S = pricePaths(T, S0, K, mu, sigma, r, N, paths)
    #profit and loses
    T20 = KDE_time(exercise_boundary, S, N)

    crrT05, exercise_boundaryT05 = CRRPricer_A(0.5, S0, mu, sigma, r, N, K)
    crrT2, exercise_boundaryT2 = CRRPricer_A(2, S0, mu, sigma, r, N, K)
    ST05 = pricePaths(0.5, S0, K, mu, sigma, r, N, paths)
    ST2 = pricePaths(2 , S0, K, mu, sigma, r, N, paths)

    T05 = KDE_time(exercise_boundaryT05, ST05, N, 0.5)
    T2 = KDE_time(exercise_boundaryT2, ST2, N, 2)

    df = T20.merge(T05,how ='left', on = 'row_num').merge(T2,how ='left', on = 'row_num')
    df.columns = ["row_num",r'T=1',r'T=0.5',r'T=2']
    df.drop(["row_num"], axis = 1, inplace = True)
    ax = df.plot(kind='kde')
    plt.xlabel("Time")
    plt.show()



#stimulated profit and loses at various volatility with 20% volatility excercise boundary
    crr, exercise_boundary = CRRPricer_A(T, S0, mu, sigma, r, N, K)
    #stimulated price paths
    S = pricePaths(T, S0, K, mu, sigma, r, N, paths)
    #profit and loses
    PL20, PL20_2 = KDE_profit(crr, exercise_boundary, S, K, r, dt)
    #profit and loses plot for 20% volatility
    PL = PL20.drop(columns=["row_num"])
    PL.columns = [r'$\sigma$ =0.2']


    ax = PL.plot(kind='kde')
    plt.xlabel("Profit and Loss")
    plt.show() 
    

    #Stimulate price paths for various realized volatility 
    S10 = pricePaths(T, S0, K, mu, 0.1, r, N, paths)
    S15 = pricePaths(T, S0, K, mu, 0.15, r, N, paths)
    S25 = pricePaths(T, S0, K, mu, 0.25, r, N, paths)
    S30 = pricePaths(T, S0, K, mu, 0.3, r, N, paths)

    #Calculate Profit and Loses with different realized volatility and appling 20% volatility trading strategy
    PL10, PL10_2 = KDE_profit(crr, exercise_boundary, S10, K, r, dt)
    PL15, PL15_2 = KDE_profit(crr, exercise_boundary, S15, K, r, dt)
    PL25, PL25_2 = KDE_profit(crr, exercise_boundary, S25, K, r, dt)
    PL30, PL30_2 = KDE_profit(crr, exercise_boundary, S30, K, r, dt)

    df = PL10.merge(PL15,how ='left', on = 'row_num').merge(PL20,how ='left', on = 'row_num').merge(PL25,how ='left', on = 'row_num').merge(PL30,how ='left', on = 'row_num')
    df.columns = ["row_num",r'$\sigma$ =0.1',r'$\sigma$ =0.15',r'$\sigma$ =0.2',r'$\sigma$ =0.25', r'$\sigma$ =0.3']
    df.drop(["row_num"], axis = 1, inplace = True)
    #print(df)
    ax = df.plot(kind='kde')
    plt.xlabel = ("Profit and Loss")
    plt.show()


    df2 = PL10_2.merge(PL15_2,how ='left', on = 'row_num').merge(PL20_2,how ='left', on = 'row_num').merge(PL25_2,how ='left', on = 'row_num').merge(PL30_2,how ='left', on = 'row_num')
    df2.columns = ["row_num",r'$\sigma$ =0.1',r'$\sigma$ =0.15',r'$\sigma$ =0.2',r'$\sigma$ =0.25', r'$\sigma$ =0.3']
    df2.drop(["row_num"], axis = 1, inplace = True)
    #print(df2)
    ax = df2.plot(kind='kde')
    #plt.xlabel("Profit and Loss")
    plt.show()



"""
#Exercise Boundaries with varying volatilities and varying risk free interest rates   

    sigmas = [0.1, 0.15, 0.2, 0.25, 0.3]
    risk_free_rates = [0.005, 0.02, 0.035, 0.05]

    for sigma in sigmas:
        CRRPricer_A(1, 10, 0.05, sigma, 0.02, 5000, 10)
    for rate in risk_free_rates:
        CRRPricer_A(1, 10, 0.05, 0.2, rate, 5000, 10)

"""



