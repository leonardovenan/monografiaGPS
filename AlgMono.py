# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 18:18:50 2017

@author: Leonardo Venancio - Monografia
"""
#from math import sqrt

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

c = 299792458 #velocidade da Luz

#tempos

t1 = 0.00505783
t2 = 0.00423206
t3 = 0.00836090
t4 = 0.00712225

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
V2x = X1 - X2
V3x = X1 - X3
V4x = X1 - X4
V2y = Y1 - Y2
V3y = Y1 - Y3
V4y = Y1 - Y4
V2z = Z1 - Z2
V3z = Z1 - Z3
V4z = Z1 - Z4

#Distancia
D1 = c*t1
D2 = c*t2
D3 = c*t3
D4 = c*t4

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
           (V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

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
          (V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

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
(V2x*V3y*V4z-V2x*V3z*V4y-V2y*V3x*V4z+V2y*V3z*V4x+V2z*V3x*V4y-V2z*V3y*V4x))

print X
print Y
print Z


















