import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x) + 2  

pi = np.pi
x = np.linspace(0, pi, 300)
y = f(x)

plt.figure(figsize=(8, 5))


plt.plot(x, y, label=r'f(x) = sen(x) + 2', color='blue', linewidth=2)

plt.fill_between(x, y, color='skyblue', alpha=0.5, label='Área a ser calculada')
pi = np.pi
plt.title(f'Gráfico de $f(x) = \sin(x) + 2$ no intervalo [0, {pi}]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=1) 
plt.xlim(0, pi)
plt.ylim(0, 3.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()