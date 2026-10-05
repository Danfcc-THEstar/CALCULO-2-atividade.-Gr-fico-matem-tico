import numpy as np
import matplotlib.pyplot as plt

v = lambda t: 4*t - t**2
a, b = 0, 4

# a) gráfico de v(t) em [0, 4]
t = np.linspace(a, b, 500)
plt.figure(figsize=(8, 5))
plt.plot(t, v(t), label="v(t) = 4t − t²")
plt.fill_between(t, 0, v(t), alpha=0.3, label="Área = D")
plt.axhline(0, color="gray", lw=0.8)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade em função do tempo")
plt.grid(True)
plt.legend()
plt.show()

# b) a velocidade é não negativa em todo o intervalo?
# v(t) = t(4 - t): raízes em t=0 e t=4, e a parábola abre para baixo,
# então v >= 0 entre as raízes. Verificação numérica:
print(f"b) Mínimo de v em [0,4]: {v(t).min():.6f}")
print(f"   v(t) >= 0 em todo o intervalo? {np.all(v(t) >= -1e-12)}")
print(f"   Velocidade máxima: {v(t).max():.4f} m/s em t = {t[np.argmax(v(t))]:.4f} s")

# c) cálculo numérico de D (sem scipy)
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
D_trap = trapezio(v, a, b, n)
D_simp = simpson(v, a, b, n)

# d) valor analítico: ∫(4t - t²)dt = 2t² - t³/3
V = lambda t: 2*t**2 - t**3/3
D_exato = V(b) - V(a)    # = 32 - 64/3 = 32/3

print(f"\nc) D numérico (trapézio, n={n}): {D_trap:.10f}")
print(f"   D numérico (Simpson,  n={n}): {D_simp:.10f}")
print(f"d) D analítico = 32/3 = {D_exato:.10f}")
print(f"   Erro absoluto (trapézio): {abs(D_trap - D_exato):.3e}")
print(f"   Erro absoluto (Simpson):  {abs(D_simp - D_exato):.3e}")