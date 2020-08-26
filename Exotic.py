import itertools
import numpy as np
from math import *

u = 1.05
d = .98
r = .01
T = 1
n = 4
K_put = 108
L_put = 97
K_call = 80
L_call = 99
S0 = 100

def bin_paths_generating(n):
    bin_outcomes = list(itertools.product([0, 1], repeat=n))
    return bin_outcomes

def S_paths_generating(S0, n):
    S_outcomes = []
    bin_outcomes = bin_paths_generating(n)
    for path in bin_outcomes:
        outcome = [S0]
        for i in path:
            outcome.append(round(outcome[-1]*u**i*d**(1-i),4))
        S_outcomes.append(outcome)
    return S_outcomes

def risk_neutral_prob_generating(u, d, r, n, T):
    delta_T = T/n
    q = (exp(r*delta_T) - d)/(u-d)
    Q = []
    bin_outcomes = bin_paths_generating(n)
    for path in bin_outcomes:
        prob = 1
        for i in path:
            prob = prob*q**i*(1-q)**(1-i)
        Q.append(round(prob,4))
    return Q

def pricing(u, d, r, n, T, pay_off):
    return exp(-r*T)*np.dot(np.transpose(risk_neutral_prob_generating(u, d, r, n, T)), pay_off)

def look_back_payoff(n):
    payoff = []
    S_outcomes = S_paths_generating(S0, n)
    for path in S_outcomes:
        payoff.append(round(max(path),4))
    return payoff

def Asian_payoff(n):
    payoff = []
    S_outcomes = S_paths_generating(S0, n)
    for path in S_outcomes:
        payoff.append(round(sum(path)/n,4))
    return payoff

def down_and_out_put_payoff(n, K, L):
    payoff = []
    S_outcomes = S_paths_generating(S0, n)
    for path in S_outcomes:
        if (min(path) >= L ):
            payoff.append(round(max( K - path[-1],0),4))
        else:
            payoff.append(0)
    return payoff

def down_and_in_call_payoff(n, K, L):
    payoff = []
    S_outcomes = S_paths_generating(S0,n)
    for path in S_outcomes:
        if (min(path) < L ):
            payoff.append(round(max(path[-1]- K,0),4))
        else:
            payoff.append(0)
    return payoff


print("All possible paths with 0 for d and 1 for u are ")
print(bin_paths_generating(n))
print("... \n")

print("All possible outcomes for S are")
print(S_paths_generating(S0, n))
print("... \n")

print("The risk neutral probabilities of the paths are")
print(risk_neutral_prob_generating(u, d, r, n, T))
print("... \n")

print("All possible payoff of lookback is")
print(look_back_payoff(n))
print("The price of lookback is")
print(pricing(u, d, r, n, T, look_back_payoff(n)))
print("... \n")

print("All possible payoff of Asian is")
print(Asian_payoff(n))
print("The price of Asian is")
print(pricing(u, d, r, n, T, Asian_payoff(n)))
print("... \n")

print("All possible payoff of down and out put with strike", K_put, "and barrier", L_put, "is")
print(down_and_out_put_payoff(n, K_put, L_put))
print("The price of down and out put is")
print(pricing(u, d, r, n, T, down_and_out_put_payoff(n, K_put, L_put)))
print("... \n")

print("All possible payoff of down and in call with strike", K_call, "and barrier", L_call, "is")
print(down_and_in_call_payoff(n, K_call, L_call))
print("The price of down and in call is")
print(pricing(u, d, r, n, T, down_and_in_call_payoff(n, K_call, L_call)))
print("... \n")