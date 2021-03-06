# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 18:18:50 2017

@author: Leonardo Venancio - Monografia
"""
#from math import sqrt
import numpy as np
import sys
from math import sqrt

print "Teste Satélite 3D\n"

#dados

c = 299792458 #velocidade da Luz (m/s)
v = 3900 # velocidade orbital dos satélites (m/s)
V = 465 # velocidade de rotação da Terra (m/s)
M = 5972e24 # Massa da Terra (kg)
R = 6371000 # Raio da Terra (m)
G = 6.67408e-11 # Constante Gravitacional Universal (m^3 kg^-1 s^-2)
g = 9.80665 #m/s^2

#tempos - tais tempos não são únicos, são apenas exemplos
#para facilitar...
tr1 = 0.00505783 #tempo de recepção
tr2 = 0.00923206
tr3 = 0.00836090
tr4 = 0.00712225

Te1 = 0.00390733 #tempo de emissão satélites
Te2 = 0.00813098
Te3 = 0.00574326
Te4 = 0.00416411

#Satélites
print "Tais valores NÃO podem ser COLINEARRES ou COPLANARES\n"

print "Sabendo que os satélites não estão no mesmo lugar, digite suas posicoes. \n"
#1
#####################################################################
X1 = float(raw_input('Digite a posicao X do primeiro satelite: '))
Y1 = float(raw_input('Digite a posicao Y do primeiro satelite: '))
Z1 = float(raw_input('Digite a posicao Z do primeiro satelite: '))
#2
#####################################################################
X2 = float(raw_input('Digite a posicao X do segundo satelite: '))
Y2 = float(raw_input('Digite a posicao Y do segundo satelite: '))
Z2 = float(raw_input('Digite a posicao Z do segundo satelite: '))
#3
#####################################################################
X3 = float(raw_input('Digite a posicao X do terceiro satelite: '))
Y3 = float(raw_input('Digite a posicao Y do terceiro satelite: '))
Z3 = float(raw_input('Digite a posicao Z do terceiro satelite: '))
#4
#####################################################################
X4 = float(raw_input('Digite a posicao X do quarto satelite: '))
Y4 = float(raw_input('Digite a posicao Y do quarto satelite: '))
Z4 = float(raw_input('Digite a posicao Z do quarto satelite: '))
#####################################################################

V2x = X1 - X2
V3x = X1 - X3
V4x = X1 - X4
V2y = Y1 - Y2
V3y = Y1 - Y3
V4y = Y1 - Y4
V2z = Z1 - Z2
V3z = Z1 - Z3
V4z = Z1 - Z4

#tais vetores não podem ser coplanares ou colineares

V2 = [V2x, V2y, V2z]
V3 = [V3x, V3y, V3z]
V4 = [V4x, V4y, V4z]

Ve = np.dot(V2,(np.cross(V3,V4)))

if(Ve==0):     
    V2x = X2 - X1
    V3x = X2 - X3
    V4x = X2 - X4
    V2y = Y2 - Y1
    V3y = Y2 - Y3
    V4y = Y2 - Y4
    V2z = Z2 - Z1
    V3z = Z2 - Z3
    V4z = Z2 - Z4
    
    V2 = [V2x, V2y, V2z]
    V3 = [V3x, V3y, V3z]
    V4 = [V4x, V4y, V4z]
    
    Ve = np.dot(V2,(np.cross(V3,V4)))
    
if(Ve==0):     
    V2x = X3 - X1
    V3x = X3 - X2
    V4x = X3 - X4
    V2y = Y3 - Y1
    V3y = Y3 - Y2
    V4y = Y3 - Y4
    V2z = Z3 - Z1
    V3z = Z3 - Z2
    V4z = Z3 - Z4
    
    V2 = [V2x, V2y, V2z]
    V3 = [V3x, V3y, V3z]
    V4 = [V4x, V4y, V4z]
    
    Ve = np.dot(V2,(np.cross(V3,V4)))
    
if(Ve==0):     
    V2x = X4 - X1
    V3x = X4 - X3
    V4x = X4 - X2
    V2y = Y4 - Y1
    V3y = Y4 - Y3
    V4y = Y4 - Y2
    V2z = Z4 - Z1
    V3z = Z4 - Z3
    V4z = Z4 - Z2
    
    V2 = [V2x, V2y, V2z]
    V3 = [V3x, V3y, V3z]
    V4 = [V4x, V4y, V4z]
    
    Ve = np.dot(V2,(np.cross(V3,V4)))

if(Ve==0):
    print "\nValores inválidos\nTente Novamente!\n"
    sys.exit()

#Distancia sem correção

D1 = c*(tr1-Te1)
D2 = c*(tr2-Te2)
D3 = c*(tr3-Te3)
D4 = c*(tr4-Te4)

X = (-0.5*(D1**2*V2y*V3z-D1**2*V2y*V4z-D1**2*V2z*V3y+D1**2*V2z*V4y
           +D1**2*V3y*V4z-D1**2*V3z*V4y-D2**2*V3y*V4z+D2**2*V3z*V4y
           +D3**2*V2y*V4z-D3**2*V2z*V4y-D4**2*V2y*V3z+D4**2*V2z*V3y
           -V2y*V3z*X1**2+V2y*V3z*X4**2-V2y*V3z*Y1**2+V2y*V3z*Y4**2
           -V2y*V3z*Z1**2+V2y*V3z*Z4**2+V2y*V4z*X1**2-V2y*V4z*X3**2
           +V2y*V4z*Y1**2-V2y*V4z*Y3**2+V2y*V4z*Z1**2-V2y*V4z*Z3**2
           +V2z*V3y*X1**2-V2z*V3y*X4**2+V2z*V3y*Y1**2-V2z*V3y*Y4**2
           +V2z*V3y*Z1**2-V2z*V3y*Z4**2-V2z*V4y*X1**2+V2z*V4y*X3**2
           -V2z*V4y*Y1**2+V2z*V4y*Y3**2-V2z*V4y*Z1**2+V2z*V4y*Z3**2
           -V3y*V4z*X1**2+V3y*V4z*X2**2-V3y*V4z*Y1**2+V3y*V4z*Y2**2
           -V3y*V4z*Z1**2+V3y*V4z*Z2**2+V3z*V4y*X1**2-V3z*V4y*X2**2
           +V3z*V4y*Y1**2-V3z*V4y*Y2**2+V3z*V4y*Z1**2-V3z*V4y*Z2**2)/
           float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

Y = (0.5*(D1**2*V2x*V3z-D1**2*V2x*V4z-D1**2*V2z*V3x+D1**2*V2z*V4x
          +D1**2*V3x*V4z-D1**2*V3z*V4x-D2**2*V3x*V4z+D2**2*V3z*V4x
          +D3**2*V2x*V4z-D3**2*V2z*V4x-D4**2*V2x*V3z+D4**2*V2z*V3x
          -V2x*V3z*X1**2+V2x*V3z*X4**2-V2x*V3z*Y1**2+V2x*V3z*Y4**2
          -V2x*V3z*Z1**2+V2x*V3z*Z4**2+V2x*V4z*X1**2-V2x*V4z*X3**2
          +V2x*V4z*Y1**2-V2x*V4z*Y3**2+V2x*V4z*Z1**2-V2x*V4z*Z3**2
          +V2z*V3x*X1**2-V2z*V3x*X4**2+V2z*V3x*Y1**2-V2z*V3x*Y4**2
          +V2z*V3x*Z1**2-V2z*V3x*Z4**2-V2z*V4x*X1**2+V2z*V4x*X3**2
          -V2z*V4x*Y1**2+V2z*V4x*Y3**2-V2z*V4x*Z1**2+V2z*V4x*Z3**2
          -V3x*V4z*X1**2+V3x*V4z*X2**2-V3x*V4z*Y1**2+V3x*V4z*Y2**2
          -V3x*V4z*Z1**2+V3x*V4z*Z2**2+V3z*V4x*X1**2-V3z*V4x*X2**2
          +V3z*V4x*Y1**2-V3z*V4x*Y2**2+V3z*V4x*Z1**2-V3z*V4x*Z2**2)/
          float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

Z = (-0.5*(D1**2*V2x*V3y-D1**2*V2x*V4y-D1**2*V2y*V3x+D1**2*V2y*V4x
           +D1**2*V3x*V4y-D1**2*V3y*V4x-D2**2*V3x*V4y+D2**2*V3y*V4x
           +D3**2*V2x*V4y-D3**2*V2y*V4x-D4**2*V2x*V3y+D4**2*V2y*V3x
           -V2x*V3y*X1**2+V2x*V3y*X4**2-V2x*V3y*Y1**2+V2x*V3y*Y4**2
           -V2x*V3y*Z1**2+V2x*V3y*Z4**2+V2x*V4y*X1**2-V2x*V4y*X3**2
           +V2x*V4y*Y1**2-V2x*V4y*Y3**2+V2x*V4y*Z1**2-V2x*V4y*Z3**2
           +V2y*V3x*X1**2-V2y*V3x*X4**2+V2y*V3x*Y1**2-V2y*V3x*Y4**2
           +V2y*V3x*Z1**2-V2y*V3x*Z4**2-V2y*V4x*X1**2+V2y*V4x*X3**2
           -V2y*V4x*Y1**2+V2y*V4x*Y3**2-V2y*V4x*Z1**2+V2y*V4x*Z3**2
           -V3x*V4y*X1**2+V3x*V4y*X2**2-V3x*V4y*Y1**2+V3x*V4y*Y2**2
           -V3x*V4y*Z1**2+V3x*V4y*Z2**2+V3y*V4x*X1**2-V3y*V4x*X2**2
           +V3y*V4x*Y1**2-V3y*V4x*Y2**2+V3y*V4x*Z1**2-V3y*V4x*Z2**2)/
           float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

print "\n\nValores sem correção\n"

print "X = ",X
print "Y = ",Y
print "Z = ",Z

A = X
B = Y
C = Z

###########################################################################################################
#Correção

e = ((3*v**2)/float((2*c**2)) - V**2/float((2*c**2)) - (G*M)/float((R*c**2)))

#Distancia com correção

D1 = c*(tr1-Te1/(1-e))
D2 = c*(tr2-Te2/(1-e))
D3 = c*(tr3-Te3/(1-e))
D4 = c*(tr4-Te4/(1-e))

X = (-0.5*(D1**2*V2y*V3z-D1**2*V2y*V4z-D1**2*V2z*V3y+D1**2*V2z*V4y
           +D1**2*V3y*V4z-D1**2*V3z*V4y-D2**2*V3y*V4z+D2**2*V3z*V4y
           +D3**2*V2y*V4z-D3**2*V2z*V4y-D4**2*V2y*V3z+D4**2*V2z*V3y
           -V2y*V3z*X1**2+V2y*V3z*X4**2-V2y*V3z*Y1**2+V2y*V3z*Y4**2
           -V2y*V3z*Z1**2+V2y*V3z*Z4**2+V2y*V4z*X1**2-V2y*V4z*X3**2
           +V2y*V4z*Y1**2-V2y*V4z*Y3**2+V2y*V4z*Z1**2-V2y*V4z*Z3**2
           +V2z*V3y*X1**2-V2z*V3y*X4**2+V2z*V3y*Y1**2-V2z*V3y*Y4**2
           +V2z*V3y*Z1**2-V2z*V3y*Z4**2-V2z*V4y*X1**2+V2z*V4y*X3**2
           -V2z*V4y*Y1**2+V2z*V4y*Y3**2-V2z*V4y*Z1**2+V2z*V4y*Z3**2
           -V3y*V4z*X1**2+V3y*V4z*X2**2-V3y*V4z*Y1**2+V3y*V4z*Y2**2
           -V3y*V4z*Z1**2+V3y*V4z*Z2**2+V3z*V4y*X1**2-V3z*V4y*X2**2
           +V3z*V4y*Y1**2-V3z*V4y*Y2**2+V3z*V4y*Z1**2-V3z*V4y*Z2**2)/
           float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

Y = (0.5*(D1**2*V2x*V3z-D1**2*V2x*V4z-D1**2*V2z*V3x+D1**2*V2z*V4x
          +D1**2*V3x*V4z-D1**2*V3z*V4x-D2**2*V3x*V4z+D2**2*V3z*V4x
          +D3**2*V2x*V4z-D3**2*V2z*V4x-D4**2*V2x*V3z+D4**2*V2z*V3x
          -V2x*V3z*X1**2+V2x*V3z*X4**2-V2x*V3z*Y1**2+V2x*V3z*Y4**2
          -V2x*V3z*Z1**2+V2x*V3z*Z4**2+V2x*V4z*X1**2-V2x*V4z*X3**2
          +V2x*V4z*Y1**2-V2x*V4z*Y3**2+V2x*V4z*Z1**2-V2x*V4z*Z3**2
          +V2z*V3x*X1**2-V2z*V3x*X4**2+V2z*V3x*Y1**2-V2z*V3x*Y4**2
          +V2z*V3x*Z1**2-V2z*V3x*Z4**2-V2z*V4x*X1**2+V2z*V4x*X3**2
          -V2z*V4x*Y1**2+V2z*V4x*Y3**2-V2z*V4x*Z1**2+V2z*V4x*Z3**2
          -V3x*V4z*X1**2+V3x*V4z*X2**2-V3x*V4z*Y1**2+V3x*V4z*Y2**2
          -V3x*V4z*Z1**2+V3x*V4z*Z2**2+V3z*V4x*X1**2-V3z*V4x*X2**2
          +V3z*V4x*Y1**2-V3z*V4x*Y2**2+V3z*V4x*Z1**2-V3z*V4x*Z2**2)/
          float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

Z = (-0.5*(D1**2*V2x*V3y-D1**2*V2x*V4y-D1**2*V2y*V3x+D1**2*V2y*V4x
           +D1**2*V3x*V4y-D1**2*V3y*V4x-D2**2*V3x*V4y+D2**2*V3y*V4x
           +D3**2*V2x*V4y-D3**2*V2y*V4x-D4**2*V2x*V3y+D4**2*V2y*V3x
           -V2x*V3y*X1**2+V2x*V3y*X4**2-V2x*V3y*Y1**2+V2x*V3y*Y4**2
           -V2x*V3y*Z1**2+V2x*V3y*Z4**2+V2x*V4y*X1**2-V2x*V4y*X3**2
           +V2x*V4y*Y1**2-V2x*V4y*Y3**2+V2x*V4y*Z1**2-V2x*V4y*Z3**2
           +V2y*V3x*X1**2-V2y*V3x*X4**2+V2y*V3x*Y1**2-V2y*V3x*Y4**2
           +V2y*V3x*Z1**2-V2y*V3x*Z4**2-V2y*V4x*X1**2+V2y*V4x*X3**2
           -V2y*V4x*Y1**2+V2y*V4x*Y3**2-V2y*V4x*Z1**2+V2y*V4x*Z3**2
           -V3x*V4y*X1**2+V3x*V4y*X2**2-V3x*V4y*Y1**2+V3x*V4y*Y2**2
           -V3x*V4y*Z1**2+V3x*V4y*Z2**2+V3y*V4x*X1**2-V3y*V4x*X2**2
           +V3y*V4x*Y1**2-V3y*V4x*Y2**2+V3y*V4x*Z1**2-V3y*V4x*Z2**2)/
           float(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

print "\nValores com correção\n"

print "X = ",X
print "Y = ",Y
print "Z = ",Z

diferenca = sqrt((A - X)**2 + (B-Y)**2 + (C-Z)**2)

print "\nA diferença de pontos sem e com a correção é = ", diferenca," metros"

"""
Teste Satélite 3D

Tais valores NÃO podem ser COLINEARRES ou COPLANARES

Sabendo que os satélites não estão no mesmo lugar, digite suas posicoes. 


Digite a posicao X do primeiro satelite: 10000

Digite a posicao Y do primeiro satelite: 15000

Digite a posicao Z do primeiro satelite: 20200000

Digite a posicao X do segundo satelite: 11045

Digite a posicao Y do segundo satelite: 17050

Digite a posicao Z do segundo satelite: 20350000

Digite a posicao X do terceiro satelite: 12540

Digite a posicao Y do terceiro satelite: 14561

Digite a posicao Z do terceiro satelite: 21033000

Digite a posicao X do quarto satelite: 11011

Digite a posicao Y do quarto satelite: 13030

Digite a posicao Z do quarto satelite: 22023000


Valores sem correção

X =  -260372007.47
Y =  71182004.4791
Z =  21149732.326

Valores com correção

X =  -260372212.948
Y =  71181985.9993
Z =  21149732.1516

A diferença de pontos sem e com a correção é =  206.307343193 metros

"""

