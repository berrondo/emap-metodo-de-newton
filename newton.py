# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:49:56 2011
@author: Claudio Berrondo

Mestrado em Modelagem Matematica da Informacao - EMAp FGV
Para a disciplina de Analise Matematica para Aplicacoes do professor Branco

Implementacao do metodo iterativo de Newton para o calculo da raiz quadrada:
    
Xn+1 = 1/2(Xn + N/Xn), i.e.:

Xo = random.randint(0, N)
precisao = 2 # casas decimais
while round(Xo*Xo, precisao) != round(N, precisao):
    Xo = (Xo + N/Xo)/2.0
return Xo

"""

from random import sample, uniform
from numpy import mean, std
from math import sqrt


# para formatacao do RELATORIO:
largura_maior = 69
largura_menor = 46
def linha(largura, ponta='|'): return '%s%s%s\n' % (ponta, '-'*largura, ponta)
def borda(largura, ponta='+'): return linha(largura, ponta)
mascara = '|%4s%16s%16s%16s%6s%10s |\n'
mascara_final = '|%15s%10s%20s |\n'
RELATORIO = borda(largura_maior)
RELATORIO += mascara % ('N', 'rz_newton(N)', 'sqrt(N)', 'Xo', '#i', 'precisao')
##



## extracao da raiz quadrada pelo metodo iterativo de Newton:
precisoes = [0.01, 0.000001, 0.0000000001]
todas_as_iteracoes = [[], [], []]

def raiz_newton(N, chute=1.0, precisao=0.01, iteracoes=0):
    iteracoes += 1
    if abs(chute**2 - N) < precisao:
        return chute, iteracoes
    else:
        chute = (chute + N/chute) / 2.0
        return raiz_newton(N, chute, precisao, iteracoes)
  
for N in sample(xrange(1000), 100):
    chute = uniform(1, N)

    RELATORIO += linha(largura_maior)    
    for n, precisao in enumerate(precisoes):
        raiz, iteracoes = raiz_newton(N, chute, precisao)
        todas_as_iteracoes[n].append(iteracoes)
        
        RELATORIO += mascara % (N, raiz, sqrt(N), chute, iteracoes, precisao)
############################################################



# arquivo de RELATORIO:        
RELATORIO += (borda(largura_maior) + '\n')

RELATORIO += borda(largura_menor)
RELATORIO += mascara_final % ('para precisao:', 'a media:', 'com desvio padrao:')
RELATORIO += linha(largura_menor)

for n, precisao in enumerate(precisoes):
    RELATORIO += mascara_final % (precisao, 
                                  mean(todas_as_iteracoes[n]), 
                                  std(todas_as_iteracoes[n]))
    
RELATORIO += borda(largura_menor)

relato = open('RELATORIO.txt', 'w')
relato.write(RELATORIO)
relato.close()
##