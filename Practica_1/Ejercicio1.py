# Ejercicio 1: Mapeo de Beverton-Holt

import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator

save_path = "C:/Users/Propietario/Desktop/ib/5-Maestría/Matematica de los sistemas biológicos/Practica_1/Informe/Figuras/Ej_01"

if not os.path.exists(save_path):
    os.makedirs(save_path)

# Funcion del mapeo de Beverton-Holt
def Beverton_Holt(n_t, r, K):
    return r * n_t / (1 + (r - 1) * n_t / K)

# Realizamos el caclulo realizando un numero de iteraciones sobre el mapeo para ciertos parámetros r y K con condición inicial n0
def Calculo_Poblacion(r, K, n0, num_iteraciones):
    # Inicializamos el vector de poblacion con el numero de iteraciones que vamos a realizar
    n_t = np.zeros(num_iteraciones)
    # Inicializamos las condiciones iniciales
    n_t[0] = n0
    # Realizamos el calculo de la poblacion para cada iteracion
    for i in range(1, num_iteraciones):
        n_t[i] = Beverton_Holt(n_t[i-1], r, K)
    return n_t


# Main del programa
if __name__ == "__main__":
    # Inicializamos una lista con distintos r, recordemos que esto afecta la estabilidad de los puntos fijos
    rs = [0.5, 1, 2]
    # Seteamos el valor de K
    K = 40
    # Inicializamos una lista con distintos valores de condiciones de población inicial
    n0s = [2, 6, 12]

    # Elegimos el numero de iteraciones que vamos a realizar
    num_iteraciones = 50

    # Loop que realiza el calculo de la poblacion para cada r y n0
    for r in rs:
        # Inicializamos la figura que va a contener todas las curvas para las distintas condiciones iniciales
        plot_actual = plt.figure()
        # Identifico cual es el r y K que estoy graficando
        plt.title('r = ' + str(r) + ', K = ' + str(K))
        # Loop que realiza el calculo de la poblacion para cada condicion inicial n0
        for n0 in n0s:
            poblacion = Calculo_Poblacion(r, K, n0, num_iteraciones)
            plt.plot(range(0,len(poblacion)), poblacion, label='Condicion inicial $n_0$ = ' + str(n0), marker='o', linestyle='-')

        # Seteo los ejes y las etiquetas
        plt.xlabel('$t$', fontsize=12)
        plt.ylabel('Poblacion $n_t$', fontsize = 12)
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

        # Guardo la figura
        file_name = os.path.join(save_path, "Beverton_Holt_r_" + str(r) + ".pdf")
        plot_actual.savefig(file_name)
    # Muestro la figura
    plt.show()

