# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:15:48 2020

@author: Nik
"""

from scipy.integrate import quad
from scipy import constants as const
import numpy as np
import matplotlib.pyplot as plt


def integrand(x):
    return (1/(4*const.pi*const.epsilon_0))*np.sin(x)

r = np.linspace(0.01, .02, num=1000)
t = np.linspace(0, 10, num=1000)

v=.8*const.c
a=.5*const.c

q = 2 * const.e * np.cos(r*t)
#print("The Charges Are")
#print(q)
q_dot = 2 * const.e * -1*np.sin(r*t) * r
#print("The derivatives of the charges Are")
#print(q_dot)

E = (1.0/(4*const.pi*const.epsilon_0)) * q / r**2.0
print(E[999])
F =  E + (1.0/(4*const.pi*const.epsilon_0)) * q_dot / (r*const.c)
print(F[999])
G =  F - (1.0/(4*const.pi*const.epsilon_0)) * (q_dot*v+q*a) / (r*const.c**2)
print(G[999])

plt.plot(r,E)
plt.plot(r,F)
plt.plot(r,G)


plt.show()