# Población con tasa de crecimiento possoniana

import numpy as np 
import scipy as sci
import os
from numpy import random
from scipy.stats import poisson
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator

#generate random values from Poisson distribution with mean=1.7
r = np.random.poisson(1.7, 1000000)
hist, bins = np.histogram(r)
plt.bar(bins[:-1], hist, linestyle = '--')
plt.xlabel('N', fontsize = 12)
plt.ylabel('Frecuencia', fontsize = 12)
plt.gca().xaxis.set_major_locator(plt.AutoLocator())
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_major_locator(plt.AutoLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_ticks_position('both')
plt.gca().xaxis.set_ticks_position('both')
plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
plt.grid(linestyle='--', linewidth=0.5)
plt.tight_layout()
save_path = r"C:\Users\Propietario\Desktop\ib\5-Maestría\Matematica de los sistemas biológicos\Practica_1\Informe\Figuras\Ej_04"
file_name = os.path.join(save_path, "DistribucionPoisson.pdf")
plt.savefig(file_name, format='pdf')
plt.show()

# Mas o menos sigue una distribución de poisson


# t_steps = 25

# N = np.zeros(t_steps)

# N[0] = 1

# for t in range(1,t_steps):
#     r = poisson.rvs(mu = 1.7)
#     N[t] = r*N[t-1]

# plt.plot(range(t_steps),N, marker = 'o', linestyle = '--')
# plt.xlabel('$t$', fontsize = 12)
# plt.ylabel('$N(t)$', fontsize = 12)
# plt.gca().xaxis.set_major_locator(plt.AutoLocator())
# plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
# plt.gca().yaxis.set_major_locator(plt.AutoLocator())
# plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
# plt.gca().yaxis.set_ticks_position('both')
# plt.gca().xaxis.set_ticks_position('both')
# plt.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)
# plt.grid(linestyle='--', linewidth=0.5)
# plt.tight_layout()
# save_path = r"C:\Users\Propietario\Desktop\ib\5-Maestría\Matematica de los sistemas biológicos\Practica_1\Informe\Figuras\Ej_04"
# file_name = os.path.join(save_path, "SimulacionPoisson.pdf")
# plt.savefig(file_name, format='pdf')
# plt.show()