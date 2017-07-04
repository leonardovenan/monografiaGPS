# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 18:18:50 2017

@author: Leonardo Venancio - Monografia
"""
from math import sqrt

"""
print "Para posições positivas\n"

R1 = float(raw_input('Posicao Satelite: '))
R2 = float(raw_input('Posicao Satelite: '))
v=3

Obs = float(raw_input('Posicao do Observador: '))

T1= abs((R1-Obs)/v)
T2= abs((R2-Obs)/v)

print
print 'T1 = '  +  str(T1)+' s'
print 'T2 = '  +  str(T2)+' s\n'

h1 = abs(R1 + T1*v)  
h2 = abs(R1 - T1*v)
h3 = abs(R2 + T2*v)
h4 = abs(R2 - T2*v)

print 'h1 = ' + str(h1)+' m'
print 'h2 = ' + str(h2)+' m'
print 'h3 = ' + str(h3)+' m'
print 'h4 = ' + str(h4)+' m'

print
# 3!
if h1==h2:
    print 'h = '+ str(h1)+' m'
elif h1==h3:
    print 'h = '+ str(h1)+' m'
elif h1==h4:
    print 'h = '+ str(h1)+' m'
elif h2==h3:
    print 'h = '+ str(h2)+' m'
elif h2==h4:
    print 'h = '+ str(h2)+' m'
elif h3==h4:
    print 'h = '+ str(h3)+' m'

"""
print "Teste Satélite 3D\n"
#Satélites
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
Z4 = float(raw_input('Digite a posicao Z do qaurto satelite: '))
#####################################################################

#Distancia
D1 = 1
D2 = 1
D3 = 1
D4 = 1

X =(-0.5*((D1**2)*Y2*Z3 - (D1**2)*Y2*Z4 - (D1**2)*Y3*Z2 + (D1**2)*Y3*Z4 + (D1**2)*Y4*Z2 - 
          (D1**2)*Y4*Z3 - (D2**2)*Y1*Z3 + (D2**2)*Y1*Z4 + (D2**2)*Y3*Z1 - (D2**2)*Y3*Z4 - 
          (D2**2)*Y4*Z1 + (D2**2)*Y4*Z3 + (D3**2)*Y1*Z2 - (D3**2)*Y1*Z4 - (D3**2)*Y2*Z1 +
          (D3**2)*Y2*Z4 + (D3**2)*Y4*Z1 - (D3**2)*Y4*Z2 - (D4**2)*Y1*Z2 + (D4**2)*Y1*Z3 +
          (D4**2)*Y2*Z1 - (D4**2)*Y2*Z3 - (D4**2)*Y3*Z1 + (D4**2)*Y3*Z2 - (X1**2)*Y2*Z3 +
          (X1**2)*Y2*Z4 + (X1**2)*Y3*Z2 - (X1**2)*Y3*Z4 - (X1**2)*Y4*Z2 + (X1**2)*Y4*Z3 +
          (X2**2)*Y1*Z3 - (X2**2)*Y1*Z4 - (X2**2)*Y3*Z1 + (X2**2)*Y3*Z4 + (X2**2)*Y4*Z1 -
          (X2**2)*Y4*Z3 - (X3**2)*Y1*Z2 + (X3**2)*Y1*Z4 + (X3**2)*Y2*Z1 - (X3**2)*Y2*Z4 -
          (X3**2)*Y4*Z1 + (X3**2)*Y4*Z2 + (X4**2)*Y1*Z2 - (X4**2)*Y1*Z3 - (X4**2)*Y2*Z1 +
          (X4**2)*Y2*Z3 + (X4**2)*Y3*Z1 - (X4**2)*Y3*Z2 - (Y1**2)*Y2*Z3 + (Y1**2)*Y2*Z4 +
          (Y1**2)*Y3*Z2 - (Y1**2)*Y3*Z4 - (Y1**2)*Y4*Z2 + (Y1**2)*Y4*Z3 + (Y2**2)*Y1*Z3 -
          (Y2**2)*Y1*Z4 - (Y3**2)*Y1*Z2 + (Y3**2)*Y1*Z4 + (Y4**2)*Y1*Z2 - (Y4**2)*Y1*Z3 +
          (Z2**2)*Y1*Z3 - (Z2**2)*Y1*Z4 - (Z3**2)*Z2*Y1 + (Z4**2)*Y1*Z2 + (Z3**2)*Y1*Z4 -
          (Z4**2)*Z3*Y1 - (Y2**2)*Y3*Z1 + (Y2**2)*Y3*Z4 + (Y2**2)*Y4*Z1 - (Y2**2)*Y4*Z3 +
          (Y3**2)*Y2*Z1 - (Y3**2)*Y2*Z4 - (Y4**2)*Y2*Z1 + (Y4**2)*Y2*Z3 - (Z1**2)*Y2*Z3 +
          (Z1**2)*Y2*Z4 + (Z3**2)*Z1*Y2 - (Z4**2)*Z1*Y2 - (Z3**2)*Z4*Y2 + (Z4**2)*Z3*Y2 -
          (Y3**2)*Y4*Z1 + (Y3**2)*Y4*Z2 + (Y4**2)*Y3*Z1 - (Y4**2)*Y3*Z2 + (Z1**2)*Z2*Y3 -
          (Z1**2)*Z4*Y3 - (Z2**2)*Z1*Y3 + (Z4**2)*Z1*Y3 + (Z2**2)*Z4*Y3 - (Z4**2)*Z2*Y3 -
          (Z1**2)*Z2*Y4 + (Z1**2)*Z3*Y4 + (Z2**2)*Z1*Y4 - (Z3**2)*Z1*Y4 - (Z2**2)*Z3*Y4 +
          (Z3**2)*Z2*Y4)/(X1*Y2*Z3 - X1*Y2*Z4 - X1*Y3*Z2 + X1*Y3*Z4 + X1*Y4*Z2 - 
          X1*Y4*Z3 - X2*Y1*Z3 + X2*Y1*Z4 + X2*Y3*Z1 - X2*Y3*Z4 - X2*Y4*Z1 + X2*Y4*Z3 + 
          X3*Y1*Z2 - X3*Y1*Z4 - X3*Y2*Z1 + X3*Y2*Z4 + X3*Y4*Z1 - X3*Y4*Z2 - X4*Y1*Z2 +
          X4*Y1*Z3 + X4*Y2*Z1 - X4*Y2*Z3 - X4*Y3*Z1 + X4*Y3*Z2))
Y= ()
Z= ()





















