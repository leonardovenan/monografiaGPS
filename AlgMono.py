# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 18:18:50 2017

@author: Leonardo Venancio - Monografia
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

    
