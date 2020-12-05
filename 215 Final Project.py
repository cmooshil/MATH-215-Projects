#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:06:23 2018

@author: christinamooshil

Creates visuals for complex mathematical functions with matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

#LOG FUNCTION
def reLog(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.log10(complex(x[a], y[b])).real
    return z

def imLog(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.log10(complex(x[a], y[b])).imag
    return z

def modLog(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a, b]=abs(np.log10(complex(x[a], y[b])))
    return z
#EXP FUNCTION
def reExp(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.exp(complex(x[a], y[b])).real 
    return z

def imExp(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.exp(complex(x[a], y[b])).imag
    return z

def modExp(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a, b]=abs(np.exp(complex(x[a], y[b])))
    return z

#MODULUS
def reMod(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.abs(complex(x[a], y[b])).real
    return z

def imMod(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.abs(complex(x[a], y[b])).imag
    return z

def modMod(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a, b]=abs(abs(complex(x[a], y[b])))
    return z
#Argument
def reArg(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.angle(complex(x[a], y[b])).real
    return z

def imArg(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a,b] = np.angle(complex(x[a], y[b])).imag
    return z

def modArg(N_max, xmin, xmax, ymin, ymax, nx, ny):
    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymax, ymin, ny)
    z = np.zeros([nx, ny])
    for a in range(nx):
        for b in range(ny):
            z[a, b]=abs(np.angle(complex(x[a], y[b])))
    return z
    
def main(): 
    print("Type m for the modulus of a complex number, e for complex exponential function, l for log function, a for the complex argument: ")
    response = input()
    if response.lower() == 'e':
        
        xmin = -5
        xmax = 5
        ymin = -5
        ymax = 5
        maxNumSteps = 64
        pts = 500
        
        real_exp = reExp(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        imag_exp = imExp(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        mod_exp = modExp(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        
        plt.figure(1)
        plt.imshow(real_exp.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Re[e^x+iy]')  
        
        plt.figure(2)
        plt.imshow(imag_exp.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Im[e^x+iy]')
        
        plt.figure(3)
        plt.imshow(mod_exp.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('|e^x+iy|')
        
    elif response.lower() == 'l':
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        maxNumSteps = 64
        pts = 500
        
        real_log = reLog(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        imag_log = imLog(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        mod_log = modLog(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        
        plt.figure(1)
        plt.imshow(real_log.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Re[log(x+iy)]')
        
        plt.figure(2)
        plt.imshow(imag_log.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Im[log(x+iy)]')
        
        plt.figure(3)
        plt.imshow(mod_log.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('|log(x+iy)|')
        
    elif response.lower() == 'm':
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        maxNumSteps = 64
        pts = 500
        
        real_mod = reMod(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        imag_mod = imMod(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        mod_mod = modMod(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        
        plt.figure(1)
        plt.imshow(real_mod.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Re[|x+iy|]')
        
        plt.figure(2)
        plt.imshow(imag_mod.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Im[|x+iy|]')
        
        plt.figure(3)
        plt.imshow(mod_mod.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('||x+iy)||')
    
    elif response.lower() == 'a':
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        maxNumSteps = 64
        pts = 500
        
        real_arg = reArg(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        imag_arg = imArg(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        mod_arg = modArg(maxNumSteps, xmin, xmax, ymin, ymax, pts, pts)
        
        plt.figure(1)
        plt.imshow(real_arg.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Re[arg(x+iy)]')

        plt.figure(2)
        plt.imshow(imag_arg.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('Im[arg(x+iy)]')
        
        plt.figure(3)
        plt.imshow(mod_arg.T, extent=[xmin, xmax, ymin,ymax], cmap = plt.cm.rainbow)
        plt.colorbar()
        plt.title('|arg(x+iy)|')
    
main()