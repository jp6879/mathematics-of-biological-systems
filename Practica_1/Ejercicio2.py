# Ejercicio 2: ecuación logística con retraso

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator
from scipy.integrate import odeint
from scipy.signal import find_peaks

save_path = "C:/Users/Propietario/Desktop/ib/5-Maestría/Matematica de los sistemas biológicos/Practica_1/Informe/Figuras/Ej_02"

if not os.path.exists(save_path):
    os.makedirs(save_path)

# Ecuacion diferencial con delay de la ecuacion logistica, con N_delay = N(t - tau)
def dNdt(N, t, r, K, N_delay):
    return r * N * (1 - N_delay / K)

# Funcion que resuelve la ecuacion diferencial con delay
def logistica_delay(r, K, N0, tau, t0, tf, niter):
    # Inicializamos el vector de tiempo para el cual vamos a resolver la ecuacion diferencial seteando el tiempo inicial, final y el numero de iteraciones
    t = np.linspace(t0, tf, niter)
    # Inicializamos el vector que contendra la solucion N(t) de la ecuacion diferencial
    N = np.zeros(niter)
    # Como hay condiciones iniciales para -tau < t < 0, inicializamos el vector de condiciones iniciales para N_delay, primero del mismo tamaño del numero de iteraciones
    N_delay = np.zeros(niter)
    # Luego seteamos las condiciones iniciales para -tau < t < 0
    N_delay[t < tau] = N0
    # Nos deshacemos de los ceros que quedaron en el vector de condiciones iniciales
    N_delay = N_delay[N_delay != 0]
    
    # Seteamos la condicion inicial para N(t) = N0
    N[0] = N0

    # Hay que ser cuidadosos con la forma en que se resuelve la ecuacion diferencial, ya que en cada paso de tiempo, la condicion inicial para N_delay va a cambiar
    for i in range(1, niter):
        # Seteamos el intervalo de tiempo para el cual vamos a resolver la ecuacion diferencial
        tspan = [t[i-1], t[i]]
        # Para resolver la ecuacion diferencial, necesitamos la condicion inicial N0 y el valor de N_delay, por esto para el intervalo de tiempo t_i-1, t_i, resolvemos la ecuacion diferencial con
        # el tiempo de dalay N_delay[i]
        N[i] = odeint(dNdt, N0, tspan, args=(r, K, N_delay[i]))[1]

        # Actualizamos el vector de las condiciones con delay para resolver el siguiente paso de tiempo
        N_delay = np.append(N_delay, N[i])

        # Actualizamos la condicion inicial para el siguiente paso de tiempo
        N0 = N[i]

    # Devolvemos el vector de tiempo y la solucion de la ecuacion diferencial
    return t, N

# Verifiquemos los resultados analiticos del comportamiento de la solución según rTau de manera aproximada    
# Esta solución aproximada vale cuando Tau es mayor al tiempo crítico Tau_c = pi/(2*r), veamos que las oscilaciones son independientes de r y tienene periodo aproximadamente de 4*Tau
    
# Dejamos fijos los parámetros c = N(0) (creo) y K = 10.0.
def sol_aproximada(t, epsilon, r, c=-1, K=10.0):
    exp1 = (t*epsilon*r)/(1 + np.pi**2/4)
    exp2 = 1j * t * r * (1 - (epsilon*np.pi)/(2*(1 + np.pi**2/4)))
    return K * (1 + c * np.exp(exp1) * np.exp(exp2))

# Veriﬁcar que tanto la amplitud de las oscilaciones es independiente de la condicion inicial, 
# como que su perıodo es independiente de r y aproximadamente 4T 

# Para hacer esto tomemosdos soluciones de la logistica con delay para r = 2.0 y 4.0

def veficar_amplitud(N0s):
    K = 10
    tau = 1
    t0 = 0
    tf = 50
    r = 2.0
    niter = 1000
    # Primero que nada grafiquemos las dos soluciones para ver que es lo que tenemos
    t1, sol1 = logistica_delay(r, K, N0s[0], tau, t0, tf, niter)
    t2, sol2 = logistica_delay(r, K, N0s[1], tau, t0, tf, niter)
    t3, sol3 = logistica_delay(r, K, N0s[2], tau, t0, tf, niter)

    print(max(sol1), max(sol2), max(sol3))

    idx = len(t1)//2
    plt.figure()
    plt.plot(t1[idx:], sol1[idx:], label="$N_0$ = " + str(N0s[0]))
    plt.plot(t2[idx:], sol2[idx:], label="$N_0$ = " + str(N0s[1]))
    plt.plot(t3[idx:], sol3[idx:], label="$N_0$ = " + str(N0s[2])) 
    plt.xlabel('$t$', fontsize=12)
    plt.ylabel('Población $N(t)$', fontsize = 12)
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

def verifica_periodo(rs):
    K = 10
    tau = 1
    t0 = 0
    tf = 50
    N0 = 2
    niter = 1000

    t1, sol1 = logistica_delay(rs[0], K, N0, tau, t0, tf, niter)
    t2, sol2 = logistica_delay(rs[1], K, N0, tau, t0, tf, niter)
    t3, sol3 = logistica_delay(rs[2], K, N0, tau, t0, tf, niter)

    # Vamos a tomar desde t = 4 porque tarda un poco en estabilizarse las soluciones
    # Busco cual es ese indice buscando el mínimo del valor absoluto de la diferencia entre el valor de la solución y 4
    target_value = 4
    difference_array = np.abs(t1 - target_value)
    nearest_index = np.argmin(difference_array)

    # Me quedo con las soluciones a partir de ese índice
    sol1 = sol1[nearest_index:]
    sol2 = sol2[nearest_index:]
    sol3 = sol3[nearest_index:]

    # Ahora busco el periodo de las soluciones buscando la diferencia de los tiempos del primer y segundo pico
    peaks1, _ = find_peaks(sol1)
    peaks2, _ = find_peaks(sol2)
    peaks3, _ = find_peaks(sol3)

    # Calculo el periodo de las soluciones
    T1 = t1[peaks1[1]] - t1[peaks1[0]]
    T2 = t2[peaks2[1]] - t2[peaks2[0]]
    T3 = t3[peaks3[1]] - t3[peaks3[0]]

    print(T1, T2, T3)

    # Pimero grafiquemos a ver que sucede
    plt.figure()
    plt.plot(t1[nearest_index:], sol1, label="r = " + str(rs[0]))
    plt.plot(t2[nearest_index:], sol2, label="r = " + str(rs[1]))
    plt.plot(t3[nearest_index:], sol3, label="r = " + str(rs[2]))
    plt.xlabel('$t$', fontsize=12)
    plt.ylabel('Población $N(t)$', fontsize = 12)
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
    file_name = os.path.join(save_path, "Verificacion_periodo.pdf")
    plt.savefig(file_name, format='pdf')
    plt.show()


# Función main
if __name__ == "__main__":
    rs = [0.3, 1.2, 2.0]
    K = 10
    N0 = 2
    tau = 1
    t0 = 0
    tf = 50
    niter = 1000

    plot_actual = plt.figure()
    plt.title('K = ' + str(K) + ', $\\tau$ = ' + str(tau))

    for r in rs:
        t, N = logistica_delay(r, K, N0, tau, t0, tf, niter)
        plt.plot(t, N, label='r = ' + str(r))
        plt.xlabel('$t$', fontsize=12)
        plt.ylabel('Población $N(t)$', fontsize = 12)
        plt.legend()
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
    file_name = os.path.join(save_path, "Logistica_delay1.pdf")
    plot_actual.savefig(file_name)

    # Parte 2 del ejercicio

    # Graficamos la solución aproximada para distintos valores de r

    # epsilon = 1e-3
    # t = np.linspace(0, 50, 1000)

    # plot_aproximada = plt.figure()
    # for r in rs:
    #     plt.plot(t, sol_aproximada(t, epsilon, r), label = "r = " + str(r))
    #     plt.xlabel('$t$', fontsize=12)
    #     plt.ylabel('Población $N(t)$', fontsize = 12)
    #     plt.gca().xaxis.set_major_locator(plt.AutoLocator())
    #     plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    #     plt.gca().yaxis.set_major_locator(plt.AutoLocator())
    #     plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    #     plt.gca().yaxis.set_ticks_position('both')
    #     plt.gca().xaxis.set_ticks_position('both')
    #     plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
    #     plt.legend(fontsize=10, loc = "best")
    #     plt.grid(linestyle='--', linewidth=0.5)
    #     plt.tight_layout()
    # file_name = os.path.join(save_path, "Aproximacion_r" + str(r) + ".pdf")
    # plt.savefig(file_name, format='pdf')
    # plt.show()


    # Verificamos que la amplitud de las oscilaciones es independiente de la condicion inicial
    # N0s = [5, 8 ,12]
    # veficar_amplitud(N0s)

    # Da 24.626984177886072 la amplitud de todos

    # Verificamos que el periodo de las oscilaciones es independiente de r y aproximadamente 4*Tau

    rs = [2.0, 3.0, 4.0]
    verifica_periodo(rs)

