# Ejercicio 2: ecuación logística con retraso

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator
from scipy.integrate import odeint
from scipy.signal import find_peaks
from ddeint import ddeint

# MODEL, WITH UNKNOWN PARAMETERS
# model = lambda Y,t, k,d,r :  1/(1+(Y(t-d)/k)**2) - r*Y(t)
# g = lambda t:0 # history before t=0

# tt = np.linspace(0,50,10000)
# print(tt)
# yy = ddeint(model, g, tt, fargs=(0.1, 5, 1)) # K=0.1, d=5, r=1

# y_list = yy[1:]
# yy = [yy[0]] + [y[0] for y in y_list]

# plt.plot(tt,yy,lw=2)

# plt.xlabel('Time')
# plt.ylabel('Y(t)')

# plt.show()

save_path = r"C:\Users\Propietario\Desktop\ib\5-Maestría\Matematica de los sistemas biológicos\Practica_1\Practico\Ej_02"

# Resuelve la ecuación logistica con retardo
def resuelve_logistica(N0, t0, tf,  r, K, T):
    logistic_delayed = lambda N, t, r, K, T : r*N(t)*(1-N(t-T)/K)
    g = lambda t: N0
    tt = np.linspace(t0,tf,10000)
    yy = ddeint(logistic_delayed, g, tt, fargs=(r, K, T)) # r=0.3, K=10, T=1

    y_list = yy[1:]
    yy = [yy[0]] + [y[0] for y in y_list]

    return tt, yy


def analiza_regimenes():

    # Parametros
    rs = [0.3, 1.2, 2.0]
    K = 10
    N0 = 2
    T = 1
    t0 = 0
    tf = 50

    # Graficamos la solución aproximada para distintos valores de r
    plt.figure()
    for r in rs:
        t, N = resuelve_logistica(N0, t0, tf, r, K, T)
        plt.plot(t, N, label=f'r = {r}')
    plt.xlabel('t')
    plt.ylabel('N(t)')
    plt.legend()
    plt.title('$K$ = ' + str(K) + ', $T$ = ' + str(T))
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().xaxis.set_ticks_position('both')
    plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    plt.legend(fontsize=10, loc="best")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.tight_layout()
    file_name = os.path.join(save_path, "Logistica_delay.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()


# analiza_regimenes()

# Verificar la validez usando una solución aproximada, esta es periódica así que analizo solo r = 2.0
# Al c lo saco tomando N(0) = 2
def sol_aproximada(t, epsilon, r, c=-0.8, K=10.0):
    exp1 = (t*epsilon*r)/(1 + np.pi**2/4)
    exp2 = 1j * t * r * (1 - (epsilon*np.pi)/(2*(1 + np.pi**2/4)))
    return K * (1 + c * np.exp(exp1) * np.exp(exp2))

def analiza_aproximada():
    r = 2.0
    epsilon = 1e-3
    T = np.pi / (2.0 * r) + epsilon
    t0 = 0
    tf = 50
    N0 = 2
    K = 10

    t, N = resuelve_logistica(N0, t0, tf, r, K, T)
    N_aprox = sol_aproximada(t, epsilon, r)

    plt.figure()
    plt.plot(t, N, label='Solución numérica')
    plt.plot(t, N_aprox, label='Solución aproximada')
    plt.xlabel('t')
    plt.ylabel('N(t)')
    plt.legend()
    plt.title('$K$ = ' + str(K) + ', $T$ = ' + str(T))
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().xaxis.set_ticks_position('both')
    plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    plt.legend(fontsize=10, loc="best")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.tight_layout()
    file_name = os.path.join(save_path, "Aproximacion_vs_exacta.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()

analiza_aproximada()
    
def veficar_amplitud_graficamente(N0s):
    K = 10
    tau = 1
    t0 = 50
    tf = 100
    r = 2.0

    # Primero que nada grafiquemos las dos soluciones para ver que es lo que tenemos
    t1, sol1 = resuelve_logistica(N0s[0], t0, tf, r, K, tau)
    t2, sol2 = resuelve_logistica(N0s[1], t0, tf, r, K, tau)
    t3, sol3 = resuelve_logistica(N0s[2], t0, tf, r, K, tau)

    print(max(sol1), max(sol2), max(sol3))

    idx = len(t1)//2
    plt.figure()
    plt.plot(t1[idx:], sol1[idx:], label="$N_0$ = " + str(N0s[0]))
    plt.plot(t2[idx:], sol2[idx:], label="$N_0$ = " + str(N0s[1]))
    plt.plot(t3[idx:], sol3[idx:], label="$N_0$ = " + str(N0s[2])) 
    plt.xlabel('$t$', fontsize=12)
    plt.ylabel('$N(t)$', fontsize = 12)
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().xaxis.set_ticks_position('both')
    plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    plt.legend(fontsize=10, loc = "best")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.tight_layout()
    file_name = os.path.join(save_path, "Verificacion_amplitud.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()

# N0s = np.linspace(2, 11, 3)
# veficar_amplitud_graficamente(N0s)
    
N0s = np.linspace(2, 25, 25)

def verifica_amplitud_diferencias(N0s):
    K = 10
    T = 1
    r = 2.0
    t0 = 50
    tf = 100

    amplitudes = []

    for N0 in N0s:
        t, sol = resuelve_logistica(N0, t0, tf, r, K, T)
        amplitudes.append(max(sol))
    
    print(amplitudes)

    plt.figure()
    plt.scatter(N0s[:len(amplitudes)], amplitudes, label='Amplitud')
    plt.xlabel('$N_0$')
    plt.ylabel('Amplitud')
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().xaxis.set_ticks_position('both')
    plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    plt.legend(fontsize=10, loc = "best")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.tight_layout()
    file_name = os.path.join(save_path, "Verificacion_diferencias_amplitud.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()

# verifica_amplitud_diferencias(N0s)

# amplitudes = [28.504410918894276, 28.52718832275614, 28.5281896120043, 28.528631609960296, 28.533377778420384, 28.51975884115352, 28.519409135252676, 28.53235710413404, 28.535309270592446, 28.501299765060125, 28.517331180128096, 28.506723356927505, 28.479233003233556, 28.485284344874927, 28.533611604690854, 28.51739789147864, 28.52893742914294, 28.531688082875647, 28.528673906024565, 28.497041446909417, 28.55422078154176, 28.49536119214357, 28.5404906744351, 28.512425181516225, 28.531714742950303]

# print(max(abs(np.diff(amplitudes))))

#La diferencia máxima es de 0.06

rs = np.linspace(2, 3, 3)

def verifica_periodo(rs):
    K = 10
    tau = 1
    t0 = 20
    tf = 100
    N0 = 2

    periodos = []
    soluciones = []

    for r in rs:
        t, sol = resuelve_logistica(N0, t0, tf, r, K, tau)
        peaks, _ = find_peaks(sol)
        periodos.append(t[peaks[1]] - t[peaks[0]])

        soluciones.append(sol)

    plt.figure()
    for i in range(len(rs)):
        plt.plot(t, soluciones[i], label='r = ' + str(rs[i]))
    plt.xlabel('$t$', fontsize=12)
    plt.ylabel('Población $N(t)$', fontsize = 12)
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().xaxis.set_ticks_position('both')
    plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    plt.legend(fontsize=10, loc = "best")
    plt.grid(linestyle='--', linewidth=0.5)
    plt.tight_layout()
    file_name = os.path.join(save_path, "Verificacion_graficos_periodo.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()

    # plt.figure()
    # plt.scatter(rs, periodos, label='Periodo')
    # plt.xlabel('$r$', fontsize = 12)
    # plt.ylabel('Periodo', fontsize = 12)
    # plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    # plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    # plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    # plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    # plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    # plt.gca().yaxis.set_ticks_position('both')
    # plt.gca().xaxis.set_ticks_position('both')
    # plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    # plt.legend(fontsize=10, loc = "best")
    # plt.grid(linestyle='--', linewidth=0.5)
    # plt.tight_layout()
    # file_name = os.path.join(save_path, "Verificacion_periodo.pdf")
    # plt.savefig(file_name, format='pdf')
    # plt.show()

# print(rs)
# verifica_periodo(rs)
