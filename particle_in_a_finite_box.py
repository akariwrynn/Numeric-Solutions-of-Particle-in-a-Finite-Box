# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:07:34 2023

@author: BURGer
"""
import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# After entering the required libraries from python, we can continue:
boxl = 6*10**-9 # You can define the box length
defined_zero = 0.01  # This is our zero
# This is our index, when you decrease this you will find more accurate results. However, one should be careful that there will be more solutions.
dx = 10.0**-4
k = 10 # This is our potentials amplitude
sigma = 0# This is our inital value that we try to solve the equation
results = []  # This is our results
search_range=10
# This is the all results where we can follow the equation that we want to solve
all_results = []
coefficents = []  # This is the list where we store our resulting parameters
while sigma < search_range:
    
    # This is our equation. For more information, you can check the paper
    eq = sigma**2+((sigma**2)*(mt.tan(sigma/2)**2))-((mt.pi**2)*k)
    all_results.append(eq)
    if abs(eq) <= defined_zero:
        results.append(sigma)
        sigma += dx
    else:
        sigma += dx

for i in results:  # Here we calculate the coefficents and put them into the coefficent list.,
    alpha = i/boxl
    beta = (i*mt.tan(i/2))/boxl
    epsilon = mt.cos(i/2)*mt.exp((beta/2)*boxl)
    coefficents.append(alpha)
    coefficents.append(beta)
    coefficents.append(epsilon)

coeff_array=np.array(coefficents)
np.savetxt("coefficents.txt",coeff_array)
# These three contains our wave functions, res is the first solution in which n=1 and res_2 is n=3. x_array shows us x axis.
result_1 = [] # Wave function 1
result_2 = [] # Wave function 2
x_array = []
# Here is the most important part of the code. One has to choose the meaningful results out of all results and then comment on which is which. This enables students to play with several solutions and see the clearly see the effects of changing the parameters such as box length, amplitude of the potential.
alpha_1 = coefficents[0]
beta_1 = coefficents[1]
epsilon_1 = coefficents[1]
alpha_2 = coefficents[3]
beta_2 = coefficents[4]
epsilon_2 = coefficents[5]


 

# In these three loops, we calculate the wavefunctions using the above coefficents and equation mentioned in the paper.
i=-boxl*2
while i < (-boxl/2):
    eq_1 = epsilon*mt.exp(beta*i)
    eq4 = epsilon_2*mt.exp(beta_2*i)
    result_1.append(eq_1)
    result_2.append(eq4)
    x_array.append(i)
    i+=0.1*10**-10
e=(-boxl/2)+0.1*10**-10
while e <boxl/2:
    eq_2 = mt.cos((alpha*e))
    eq5 = mt.cos((alpha_2*e))
    result_1.append(eq_2)
    result_2.append(eq5)
    x_array.append(e)
    e+=0.1*10**-10
d=(boxl/2)+0.1*10**-10
while d < (boxl*2):
    eq_3 = epsilon*mt.exp(-beta*d)
    eq6 = epsilon_2*mt.exp(-beta_2*d)
    result_1.append(eq_3)
    result_2.append(eq6)
    x_array.append(d)
    d+=0.1*10**-10    

# Here we plot and save as excel file in order to if one student wants to play with other programs such as origin and excel
plt.plot(x_array, result_1)
plt.show()
plt.plot(x_array, result_2)
df = pd.DataFrame({'X': x_array, 'k=10,state.1': result_1, 'k=10,state.3': result_2})

df.to_excel('k10kwfs.xlsx', sheet_name='new_sheet_name')

