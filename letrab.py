import numpy as np

f = lambda x: np.sin(x) + 2

a, b = 0, np.pi


I_exato = (-np.cos(b) + 2*b) - (-np.cos(a) + 2*a)   


def ponto_medio(f, a, b, n):
    h = (b - a) / n
    x_medios = a + h * (np.arange(n) + 0.5)   
    alturas = f(x_medios)                     #
    return h * np.sum(alturas), h

print(f"Valor exato (c): {I_exato:.10f}\n")
print(f"{'n':>5} | {'h':>10} | {'Aproximação':>14} | {'Erro absoluto':>14} | {'Erro relativo (%)':>18}")
print("-" * 75)

erros = {}
for n in [10, 50, 100, 500]:
    I_aprox, h = ponto_medio(f, a, b, n)
    erro_abs = abs(I_aprox - I_exato)         
    erro_rel = erro_abs / abs(I_exato) * 100
    erros[n] = erro_abs
    print(f"{n:>5} | {h:>10.6f} | {I_aprox:>14.10f} | {erro_abs:>14.3e} | {erro_rel:>18.6f}")


n_melhor = min(erros, key=erros.get)
print(f"\nMenor erro: n = {n_melhor}")

ns = list(erros)
print("\nRazão entre erros (n_anterior -> n_atual):")
for i in range(1, len(ns)):
    razao_erro = erros[ns[i-1]] / erros[ns[i]]
    razao_h2 = (ns[i] / ns[i-1]) ** 2
    print(f"  n={ns[i-1]} -> n={ns[i]}: erro caiu {razao_erro:.1f}x  (esperado ~ (n2/n1)^2 = {razao_h2:.1f}x)")