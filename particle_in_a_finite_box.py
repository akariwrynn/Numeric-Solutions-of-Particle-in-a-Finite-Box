# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:07:34 2023

@author: BURGer
"""
import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# After entering the required libraries from Python, we can continue:
boxl = 6*10**-9 # You can define the box length
eta = 0.01  # This is our zero
# This is our index; when you decrease this, you will find more accurate results. However, one should be careful that there will be more solutions.
dx = 10.0**-6  # This is the step size of our manual root search. It should be adjusted for the specific cases.
k = 10 # This is our potential's amplitude as shown in Figure 1.a
sigma = 0# This is our initial value that we try to solve the equation
results = []  # This is our results
search_range=10 # This is the upper limit of the root finding loop. This should be increased when it is estimated to have large amounts of solutions, such that the loop can find the higher values of roots. To check this, the authors suggest using Particle_in_a_finite_box_bound_state_calculator.py beforehand.
# This is all the results where we can follow the equation that we want to solve
all_results = []
coefficients = []  # This is the list where we store our resulting parameters
while sigma < search_range:
    
    # This is our equation. For more information, you can check the paper
    eq = sigma**2+((sigma**2)*(mt.tan(sigma/2)**2))-((mt.pi**2)*k)
    all_results.append(eq)
    if abs(eq) <= eta:
        results.append(sigma)
        sigma += dx
    else:
        sigma += dx

for i in results:  # Here we calculate the coefficients and put them into the coefficient list.,
    alpha = i/boxl
    beta = (i*mt.tan(i/2))/boxl
    epsilon = mt.cos(i/2)*mt.exp((beta/2)*boxl)
    coefficients.append(alpha)
    coefficients.append(beta)
    coefficients.append(epsilon)

coeff_array=np.array(coefficients)

# These three contain our wave functions, res is the first solution in which n=1, and res_2 is n=3. x_array shows us x axis.
result_1 = [] # Wave function 1
result_2 = [] # Wave function 2
x_array = []
# Here is the most important and tricky part of the code. One has to choose the meaningful results out of all the results and then comment on which is which. This enables students to play with several solutions and clearly see the effects of changing the parameters, such as box length and amplitude of the potential.
# The coefficient matrix can be very confusing, but it is quite simple. First, students can check the location and number of solutions of an interested system with Particle_in_a_finite_box_bound_state_calculator.py. 
# After that, using a variable explorer (in Spyder) or a similar GUI-based editor, students can select the meaningful solutions. There will be degenerate and/or solutions that lead to unexpected results. These can be eliminated or ignored by either plotting and analyzing their result or doing a direct analysis of the obtained coefficient results.
alpha_1 = coefficients[0]
beta_1 = coefficients[1]
epsilon_1 = coefficients[2]
alpha_2 = coefficients[474]
beta_2 = coefficients[475]
epsilon_2 = coefficients[476]


 

# In these three loops, we calculate the wavefunctions using the above coefficients and the equation mentioned in the paper.
i=-boxl*2
while i < (-boxl/2):
    eq_1 = epsilon_1*mt.exp(beta_1*i)
    eq4 = epsilon_2*mt.exp(beta_2*i)
    result_1.append(eq_1)
    result_2.append(eq4)
    x_array.append(i)
    i+=0.1*10**-10
e=(-boxl/2)+0.1*10**-10
while e <boxl/2:
    eq_2 = mt.cos((alpha_1*e))
    eq5 = mt.cos((alpha_2*e))
    result_1.append(eq_2)
    result_2.append(eq5)
    x_array.append(e)
    e+=0.1*10**-10
d=(boxl/2)+0.1*10**-10
while d < (boxl*2):
    eq_3 = epsilon_1*mt.exp(-beta_1*d)
    eq6 = epsilon_2*mt.exp(-beta_2*d)
    result_1.append(eq_3)
    result_2.append(eq6)
    x_array.append(d)
    d+=0.1*10**-10      

# Here we plot and save as an Excel file in order to see if one student wants to play with other programs, such as Origin and Excel
plt.plot(x_array, result_1)
plt.show()
plt.plot(x_array, result_2)
df = pd.DataFrame({'X': x_array, 'k=10': result_1, 'k=10': result_2})

df.to_excel('k10kwfs.xlsx', sheet_name='new_sheet_name')

