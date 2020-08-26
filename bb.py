import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-1,1)
plt.plot(x,f(x))
plt.show()