from AmerOPs import CRRPricer_A
from PricePath import pricePaths
from KDE import KDE_profit

if __name__ == "__main__":
    T = 1; S0 = 10; mu = 0.05; sigma =  0.2; r = 0.02; N = 5000; paths = 100; K = 10
    dt = T/N
    crr, exercise_boundary = CRRPricer_A(T, S0, mu, sigma, r, N, K)
    S = pricePaths(T, S0, K, mu, sigma, r, N, paths)
    X = KDE_profit(crr, exercise_boundary, S, K, r, dt)

#Exercise Boundaries with varying volatilities and varying risk free interest rates   
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


