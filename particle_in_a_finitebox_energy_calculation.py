# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 08:50:24 2024

@author: USER
"""
import pandas as pd
import numpy as np

# Function to calculate first derivative using two-point difference
def calculate_first_derivative(x, y):
    dy_dx = np.gradient(y, x)
    return dy_dx

# Function to calculate second derivative using two-point difference
def calculate_second_derivative(x, y):
    dy_dx = calculate_first_derivative(x, y)
    d2y_dx2 = np.gradient(dy_dx, x)
    return d2y_dx2

def normalize(x,y):
    return y/np.trapz(y**2,x=x)

def energycalc_1stder(x,y):
    return (np.trapz(np.gradient(y, x)**2,x=x) + 2*k*E0* np.trapz(y[:900]**2,x=x[:900]))/E0

# Read Excel file
excel_file_path = 'k61.xlsx'
df = pd.read_excel(excel_file_path)

# Extract x and y columns
x_column = df.columns[0]
y_columns = df.columns[1:]

x_values = df[x_column]

h=6.62607015E-34
m=9.1093837E-31
L=120E-10
k=50
q_e=1.9E-19
PI=3.1415926

E0 = h**2/(8*m*L**2) / (h**2/(8*PI**2*m))

# Calculate derivatives for each y column
for y_column in y_columns:
    df[y_column]=y_values = normalize(x_values,df[y_column])
    
    # Calculate first derivative
    first_derivative = calculate_first_derivative(x_values, y_values)
    
    # Calculate second derivative
    second_derivative = calculate_second_derivative(x_values, y_values)

    # Add the derivatives to the DataFrame
    df[f'{y_column}_1st_derivative_E={energycalc_1stder(x_values,y_values)}'] = first_derivative
    df[f'{y_column}_2nd_derivative'] = second_derivative
    print(energycalc_1stder(x_values,y_values))
# Save the results to a new Excel file
output_file_path = 'output_derivatives.xlsx'
df.to_excel(output_file_path, index=False)
