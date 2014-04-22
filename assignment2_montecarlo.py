#Lucero Rogel
#lrogel@ucsc.edu
#CMPS 5P
#Assignment2 

import random
import math

#Simple program to observe how stock and investment portfolios behave.
#Single run of the monte carlo simulation to obtain the ratio.
#ratio= between new current balance and what you originally had in the account (current balance.


def monte_finances(avg_return,stddev_return,leverage_ratio,num_of_periods):
    current_balance=1000
    for i in range(num_of_periods):
        distribution_number = random.normalvariate(avg_return,stddev_return)
        rate_of_return = distribution_number *(leverage_ratio * current_balance)
        current_balance = rate_of_return+current_balance
        if current_balance <0:
           current_balance=0
    ratio=current_balance/1000
    print ratio
print monte_finances(2.0,10.0,1.0,5)


#Simulating multiple runs to determine if its a good investment.

