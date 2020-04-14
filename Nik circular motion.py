# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:00:29 2020

@author: Nik
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import mplcyberpunk

plt.style.use("cyberpunk")

plt.close('all')

Nt = 2001
t = np.linspace(0.0, 100e-15, Nt)
distance = np.linspace(5E-6, 500, Nt)

#Initial x,y positions of the moving charge
initialX = 5E-10   
initialY = 0
     
radius = np.sqrt((initialX)**2.0 + (initialY)**2.0) #Radius of the Spin

v = 0 #the speed at which this thing spins

angularV = 0#v/radius    #angular velocity

x1 = 0#radius * np.cos(angularV * t)
vx1 = angularV * radius * -np.sin(angularV * t)

y1 = 0#radius * np.sin(angularV * t)
vy1 = angularV * radius * np.cos(angularV * t)


x2 = 5
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
#print(Ey)
#
#plt.figure()
#plt.plot(t,Ex,label='Ex')
#plt.plot(t,Ey,label='Ey')
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#axes = plt.gca()
#axes.set_ylim([-4E-1,4E-1])
#mplcyberpunk.add_glow_effects()
#
#plt.show()
#
#plt.figure()
#plt.plot(t,Ex,label='Ex')
#plt.plot(t,Ey,label='Ey')
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#axes = plt.gca()
#axes.set_xlim([490,500])
#axes.set_ylim([-4E-8,4E-8])
#mplcyberpunk.add_glow_effects()
#
#plt.show()
#
#plt.figure()
#plt.title('Observer ' + str(x2) + ' meters away')
#plt.plot(t,Ex,label='Ex')
#plt.plot(t,Ey,label='Ey')
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#mplcyberpunk.add_glow_effects()
#
#plt.show()

plt.figure(figsize=(1800/96, 1000/96))
plt.plot(t,Ex)
plt.legend(bbox_to_anchor=(.5, .99), loc='upper', borderaxespad=0.,fontsize=46)
plt.ylabel('Electric Field (N/C)',fontsize=46)
plt.xlabel('Time (s)',fontsize=46)
plt.xticks(fontsize= 46)
plt.yticks(fontsize= 46)
plt.tick_params(axis='x', labelsize=46)
plt.ticklabel_format(axis="y", style="sci",scilimits=(0,0))
plt.locator_params(axis='x', nbins=6)
axes = plt.gca()
mplcyberpunk.add_glow_effects()
plt.show()