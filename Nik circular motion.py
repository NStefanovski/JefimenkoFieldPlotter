# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:00:29 2020

@author: Nik
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.constants as const
import matplotlib.animation as animation
plt.close('all')

Nt = 2001
t = np.linspace(0.0, 100e-15, Nt)
distance = np.linspace(5E-6, 5E-5, Nt)

#Initial x,y positions of the moving charge
initialX = 5E-10   
initialY = 0
     
radius = np.sqrt((initialX)**2.0 + (initialY)**2.0) #Radius of the Spin

v = 5E5 #the speed at which this thing spins

angularV = v/radius    #angular velocity

x1 = radius * np.cos(angularV * t)
vx1 = angularV * radius * -np.sin(angularV * t)

y1 = radius * np.sin(angularV * t)
vy1 = angularV * radius * np.cos(angularV * t)


x2 = 5E-6
y2 = 0

#Retarded  Times
Tr = t - (np.absolute(np.sqrt((x2-x1)**2.0 + (y2-y1)**2.0)) / const.speed_of_light)

#Retarded Position
Trx1 = radius * np.cos(angularV * Tr)
Try1 = radius * np.sin(angularV * Tr)

Rx = np.absolute(x2 - Trx1)
Ry = np.absolute(y2 - Try1)

R = np.sqrt((x2-Trx1)**2.0 + (y2-Try1)**2.0)
#Retarded Velocities
vTrx1 = angularV * radius * -np.sin(angularV * Tr)
vTry1 = angularV * radius * np.cos(angularV * Tr)

speed = np.sqrt(vTrx1**2 + vTry1**2)


#Retarded Acceleration
aTrx1 = angularV**2 * radius * -np.cos(angularV * Tr)
aTry1 = angularV**2 * radius * -np.sin(angularV * Tr)

RdotU = (Rx*(const.speed_of_light * Rx - vTrx1 * R) + Ry*(const.speed_of_light * Ry - vTry1 * R))/ R

print(Ry[0],vTry1[0],R[0])

UcrossA = (aTry1*((const.speed_of_light * Rx - vTrx1*R)/R) - (aTrx1*((const.speed_of_light * Ry - vTry1*R)/R)))

RcrossUcrossAx = Rx * UcrossA
RcrossUcrossAy = Ry * UcrossA

CVUx = ((const.speed_of_light**2 - speed**2)*(const.speed_of_light*Rx - vTrx1*R))/R
CVUy = ((const.speed_of_light**2 - speed**2)*(const.speed_of_light*Ry - vTry1*R))/R

q = const.elementary_charge

Ex = (q /(4 * const.pi * const.epsilon_0)) * (R / (RdotU)**3) * (CVUx + RcrossUcrossAx)
Ey = (q /(4 * const.pi * const.epsilon_0)) * (R / (RdotU)**3) * (CVUy + RcrossUcrossAy)
print(Ey)

plt.figure()
plt.plot(t,Ex,label='Ex')
plt.plot(t,Ey,label='Ey')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

plt.figure()
plt.plot(t,Ex,label='Ex')
plt.plot(t,Ey,label='Ey')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
axes = plt.gca()
axes.set_ylim([-4E-13,4E-13])
plt.show()

plt.figure()
plt.plot(t,Ex,label='Ex')
plt.plot(t,Ey,label='Ey')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
axes = plt.gca()
axes.set_ylim([-4E-6,4E-6])
plt.show()

plt.figure()
plt.title('Observer ' + str(x2) + ' meters away')
plt.plot(t,Ex,label='Ex')
plt.plot(t,Ey,label='Ey')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

E = np.sqrt(Ex**2 + Ey**2)
plt.figure()
plt.title('Observer ' + str(x2) + ' meters away')
plt.plot(t,E,label='E')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
