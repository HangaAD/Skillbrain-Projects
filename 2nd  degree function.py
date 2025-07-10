import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 6, 1000)


f = x**2 - 4*x + 3

plt.plot(x, f, label='f(x) = x² - 4x + 3')


plt.title('Graficul funcției f(x) = x² - 4x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')


plt.legend()
plt.grid(True)
plt.show()