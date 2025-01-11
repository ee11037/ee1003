import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
diff_eq = ctypes.CDLL('./diff_eq.so')

# Define arrays for y and y'
N = 1000
y_points = np.zeros(N, dtype=np.double)
y_prime_points = np.zeros(N, dtype=np.double)

# Call the C function to get the solution
diff_eq.solve_diff_eq(y_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       y_prime_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Generate the theoretical solution y = e^x + 1
x_vals = np.linspace(0, N * 0.001, N)
y_theory = np.exp(x_vals) + 1

# Plot the simulation and the theory
plt.plot(x_vals, y_points, label='Simulation (Trapezoidal)', color='blue')
plt.plot(x_vals, y_theory, label='Theory (e^x + 1)', color='red', linestyle='--')

# Add legend and labels
plt.legend()
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.savefig('./figs/curve.png')

