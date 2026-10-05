import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x + 2
g = lambda x: x**2


x = np.linspace(-2, 3, 500)
plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label="f(x) = x + 2")
plt.plot(x, g(x), label="g(x) = x²")


raizes = np.roots([1, -1, -2])
x1, x2 = sorted(raizes)                       
print(f"b) Pontos de interseção: x = {x1:.0f} e x = {x2:.0f}")
print(f"   Pontos: ({x1:.0f}, {g(x1):.0f}) e ({x2:.0f}, {g(x2):.0f})")

plt.plot([x1, x2], [g(x1), g(x2)], "ko", label="Interseções")


x_teste = (x1 + x2) / 2
if f(x_teste) > g(x_teste):
    print("c) Entre as interseções, f(x) = x + 2 está acima de g(x) = x².")
else:
    print("c) Entre as interseções, g(x) = x² está acima de f(x) = x + 2.")

xx = np.linspace(x1, x2, 300)
plt.fill_between(xx, g(xx), f(xx), alpha=0.3, label="Área entre as curvas")
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.grid(True)
plt.legend()
plt.title("Área entre f(x) = x + 2 e g(x) = x²")
plt.show()


print("d) Área = ∫ de -1 até 2 de [(x + 2) - x²] dx")


h_ = lambda x: f(x) - g(x)

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
A_trap = trapezio(h_, x1, x2, n)
A_simp = simpson(h_, x1, x2, n)


F = lambda x: x**2 / 2 + 2*x - x**3 / 3
A_exata = F(x2) - F(x1)                       

print(f"\ne) Área numérica (trapézio, n={n}): {A_trap:.10f}")
print(f"   Área numérica (Simpson,  n={n}): {A_simp:.10f}")
print(f"f) Área analítica:                  {A_exata:.10f}")
print(f"   Erro absoluto (trapézio): {abs(A_trap - A_exata):.3e}")
print(f"   Erro absoluto (Simpson):  {abs(A_simp - A_exata):.3e}")