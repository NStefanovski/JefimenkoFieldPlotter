# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:00:29 2020

@author: Nik
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
plt.close('all')

Nt = 2001
t = np.linspace(0.0, 2, Nt)
dt = t[1]-t[0]


#Initial x,y positions of the moving charge
initialX = 5E-10   
initialY = 0  
     
radius = np.sqrt((initialX)**2.0 + (initialY)**2.0) #Radius of the Spin

v = 5E5 #the velocity at which this thing spins

angularV = v/radius    #angular velocity

x1 = radius * np.cos(angularV * t)
y1 = radius * np.sin(angularV * t)
plt.figure()
plt.plot(x1,y1)
plt.show()

x2 = 5E-8
y2 = 0


plt.figure()
plt.plot(t,np.sqrt((x2-x1)**2.0 + (y2-y1)**2.0))
plt.xlabel('Time ')
plt.ylabel('Separation')
plt.show()
