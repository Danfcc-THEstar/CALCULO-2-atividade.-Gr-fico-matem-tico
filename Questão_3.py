import numpy as np

f = lambda x: x * np.sqrt(x**2 + 1)
a, b = 0, 2

I_exato = (5 * np.sqrt(5) - 1) / 3

def trapezio(func, a, b, n):
    xs = np.linspace(a, b, n + 1)
    ys = func(xs)
    dx = (b - a) / n
    return dx * (ys[0] / 2 + np.sum(ys[1:-1]) + ys[-1] / 2)

def simpson(func, a, b, n):
    if n % 2 != 0:
        n += 1
    xs = np.linspace(a, b, n + 1)
    ys = func(xs)
    dx = (b - a) / n
    return dx / 3 * (ys[0] + 4 * np.sum(ys[1:-1:2]) + 2 * np.sum(ys[2:-1:2]) + ys[-1])

n = 1000
I_num = simpson(f, a, b, n)
print(f"Analítico: {I_exato:.12f}")
print(f"Numérico (Simpson, n={n}): {I_num:.12f}")
print(f"f) Erro absoluto: {abs(I_num - I_exato):.3e}")