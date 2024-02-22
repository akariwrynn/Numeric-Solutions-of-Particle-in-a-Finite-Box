import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def solve_infinite_well(box_length, num_points, n_values):
    x = np.linspace(-box_length/2,box_length/2, num_points)
    dx = x[1] - x[0]

    wavefunctions = {}

    for n in n_values:
        psi = np.sqrt(2 / box_length) * np.sin((n * np.pi / box_length) * (x + box_length / 2))
        normalization_factor = np.sqrt(np.trapz(psi**2, dx=dx))
        psi /= normalization_factor

        wavefunctions[f'n_{n}'] = psi

    return x, wavefunctions

def save_wavefunctions(x, wavefunctions, file_prefix):
    for key, psi in wavefunctions.items():
        filename = f'{file_prefix}_{key}.txt'
        np.savetxt(filename, np.column_stack((x, psi)), header=f'x {key}', comments='')
        df = pd.DataFrame({'X': x, 'k=61.1,inf,state.3':psi })
        df.to_excel('28aralıkinifnitex.xlsx', sheet_name='new_sheet_name')

# Updated box length in meters
box_length = 6e-9  # meters
num_points = 1200
n_values = [1]

x, wavefunctions = solve_infinite_well(box_length, num_points, n_values)
save_wavefunctions(x, wavefunctions, 'infinitebox_k10')

# Plot the wavefunctions for visualization
plt.figure(figsize=(10, 6))
for key, psi in wavefunctions.items():
    plt.plot(x, psi, label=key)
    plt.title('Particle in a Box Wavefunctions')
    plt.xlabel('Position (meters)')
    plt.ylabel('Wavefunction')
    plt.legend()
    plt.show()

