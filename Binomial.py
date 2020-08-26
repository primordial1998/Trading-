from math import *
import numpy as np


u = 1.02
d = 0.98
r = 0.01 
T = 1
So = 100
K = 110
n = 4


def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)



def stock(So, u, d, n):
    s = np.zeros((n+1,1))
    for i in range(n+1):
            s[i] = So*(d**i)*(u**(n-i))
    return s

def risk_neutral_prob(u, d, r, n, T):
    delta_T = T/n
    q = (exp(r*delta_T) - d)/(u-d)
    Q = np.zeros((n+1,1))
    for i in range(n+1):
            Q[i] = nCr(n,i) * ((1-q)**i)*(q**(n-i))
            if Q[i] < 0 or Q[i] > 1 :
                print("Arbitrage condition not satisfied !")
                return np.zeros((n+1,1))
    return Q

Q = risk_neutral_prob(u, d, r, n, T)



def Euro_Call(So, u, d, K, n):
    S = stock(So, u,d, n)
    C = np.zeros((n+1,1))
    for i in range(n+1):
        C[i] = max(S[i]-K, 0)
    return C



def Euro_Put(So, u, d, K, n):
    S = stock(So, u, d, n)
    P = np.zeros((n+1,1))
    for i in range(n+1):
        P[i] = max(K - S[i], 0)
    return P



def Butterfly(So, u, d, K1, K2, K3, n):
    S = stock(So, u,d, n)
    B = np.zeros((n+1,1))
    for i in range(n+1):
        if K1 <= S[i] < K2:
            B[i]= S[i] - K1
        if K2 <= S[i] < K3:
            B[i] = K3 - S[i]
    return B



def Strangle(So, u, d, K1, K2, n):
    S = stock(So, u,d, n)
    Strangle = np.zeros((n+1,1))
    for i in range(n+1):
        if S[i] <= K1:
            Strangle[i]=  K1 - S[i]
        if S[i] >= K2:
            Strangle[i] = S[i] - K2
    return Strangle



def risk_neutral_pricing(So, u, d, n, T, pay_off):
    v = 0
    S = stock(So, u, d, n)
    Q = risk_neutral_prob(u,d,r,n, T)
    delta_T = T/n
    v = exp(-r*delta_T * n)*np.dot(np.transpose(Q), pay_off)
    return v



if Q.any() :
    
    print("The risk neutral probability vector at period ", n,  " is \n", Q)    
    print("...\n\n")
    
    print("The stock price vector at period ", n, " is \n", stock(So,u,d,n))    
    print("...\n\n")

    print("The call payoff vector at period ", n, " is \n", Euro_Call(So, u, d, K, n)) 
    print("...\n\n")
    
    print("The put payoff vector at period ", n, " is \n", Euro_Put(So, u, d, K, n)) 
    print("...\n\n")
    
    call_0 = risk_neutral_pricing(So, u, d, n, T, Euro_Call(So, u, d, K, n))
    print("The price of Euro call in the ", n, " period model with strike ", K, " is \n", call_0)  
    print("...\n\n")
    
    put_0 = risk_neutral_pricing(So, u, d, n, T, Euro_Put(So, u, d, K, n))
    print("The price of Euro put in the ", n, " period model with strike ", K, " is \n", put_0)  
    print("...\n\n")