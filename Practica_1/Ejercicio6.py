# Efecto Alle

import numpy as np
import scipy as sci
from scipy.integrate import solve_ivp
import os
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator


# Define la función de la ecuación diferencial
def alle_equation(t, N, r, K, A):
    return r * N * (1 - N / K) * (N/A - 1)

# Vamos a setear los parámetros de la ecuación
A = 10
K = 20
r = 0.1
N0s = [5, 15, 25]

# Para cada valor inicial N0, resuelve la ecuación diferencial y grafica la solución
for N0 in N0s:
    # Tiempo de integración desde 0 a 50
    t_span = (0, 50)
    # Resolvemos la ecuación diferencial
    sol = solve_ivp(alle_equation, t_span, [N0], args=(r, K, A), dense_output=True, max_step=0.1)
    # Graficar la solución
    plt.plot(sol.t, sol.y[0], label=f"$N_0$ = {N0}")

plt.xlabel("$t$", fontsize=12)
plt.ylabel("$N(t)$", fontsize=12)
plt.legend(fontsize=10, loc="best")
plt.grid(linestyle='--', linewidth=0.5)
plt.gca().xaxis.set_major_locator(plt.AutoLocator())
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_major_locator(plt.AutoLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_ticks_position('both')
plt.gca().xaxis.set_ticks_position('both')
plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
plt.savefig(r"C:\Users\Propietario\Desktop\ib\5-Maestría\Matematica de los sistemas biológicos\Practica_1\Practico\Ej06\Ejercicio6.pdf")
plt.show()
