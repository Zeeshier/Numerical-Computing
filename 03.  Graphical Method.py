# Graphical Method

import matplotlib.pyplot as plt
import numpy as np

# Define the function
f = lambda x: np.sin(x) - x

# Create a range of x values
x = np.linspace(-2, 2, 100)
y = f(x)

# Plot the function
plt.axhline(0, color='black', linestyle='--')
plt.plot(x, y, label='sin(x) - x')
plt.legend()
plt.title("Graphical Solution")
plt.show()
