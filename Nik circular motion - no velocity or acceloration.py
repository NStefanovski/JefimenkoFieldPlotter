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

def CalculateField(t,distance,radius,v,angularV):
    x1 = radius * np.cos(angularV * t)
    vx1 = angularV * radius * -np.sin(angularV * t)
    
    y1 = radius * np.sin(angularV * t)
    vy1 = angularV * radius * np.cos(angularV * t)
    
    
    x2 = distance
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
    print(vTrx1)
    vTry1 = angularV * radius * np.cos(angularV * Tr)
    
    speed = np.sqrt(vTrx1**2 + vTry1**2)
    
    
    #Retarded Acceleration
    aTrx1 = angularV**2 * radius * -np.cos(angularV * Tr)
    aTry1 = angularV**2 * radius * -np.sin(angularV * Tr)
    
    RdotU = (Rx*(const.speed_of_light * Rx - vTrx1 * R) + Ry*(const.speed_of_light * Ry - vTry1 * R))/ R
        
    UcrossA = (aTry1*((const.speed_of_light * Rx - vTrx1*R)/R) - (aTrx1*((const.speed_of_light * Ry - vTry1*R)/R)))
    
    RcrossUcrossAx = Rx * UcrossA
    RcrossUcrossAy = Ry * UcrossA
    
    CVUx = ((const.speed_of_light**2 - speed**2)*(const.speed_of_light*Rx - vTrx1*R))/R
    CVUy = ((const.speed_of_light**2 - speed**2)*(const.speed_of_light*Ry - vTry1*R))/R
    
    q = const.elementary_charge
    
    Ex = (q /(4 * const.pi * const.epsilon_0)) * (R / (RdotU)**3) * (CVUx + RcrossUcrossAx)
    Ey = (q /(4 * const.pi * const.epsilon_0)) * (R / (RdotU)**3) * (CVUy + RcrossUcrossAy)
    
    return Ex
   
    
Nt = 2001
t = np.linspace(0.0, 100e-16, Nt)
distance = 50#np.linspace(5E-7, 4E-8, Nt)

#Initial x,y positions of the moving charge
initialX = 5E-10   
initialY = 0
     
radius = 0#np.sqrt((initialX)**2.0 + (initialY)**2.0) #Radius of the Spin

v = 0 #the speed at which this thing spins

angularV = 0#v/radius    #angular velocity

E_stationary = CalculateField(t,distance,radius,v,angularV)

radius = np.sqrt((initialX)**2.0 + (initialY)**2.0) #Radius of the Spin

v = 5E5#.8*const.speed_of_light #the speed at which this thing spins

angularV = v/radius    #angular velocity

E_moving = CalculateField(t,distance,radius,v,angularV)

#Coulomb's law
E = const.elementary_charge/(4*np.pi*const.epsilon_0*distance**2)
print(E)
plt.figure(figsize=(1800/96, 1000/96))
plt.plot(t,E_stationary)
plt.plot(t,E_moving)

plt.legend(bbox_to_anchor=(.8, 1), loc='upper', borderaxespad=0.,fontsize=46)
plt.ylabel('Electric Field (N/C)',fontsize=46)
plt.xlabel('Time (t)',fontsize=46)
plt.xticks(fontsize= 46)
plt.yticks(fontsize= 46)
plt.tick_params(axis='x', labelsize=46)
plt.ticklabel_format(axis="y", style="sci",scilimits=(0,0))
plt.locator_params(axis='x', nbins=3)
ax = plt.gca()
ax.yaxis.offsetText.set_fontsize(30)
ax.xaxis.offsetText.set_fontsize(30)
mplcyberpunk.add_glow_effects()
plt.show()