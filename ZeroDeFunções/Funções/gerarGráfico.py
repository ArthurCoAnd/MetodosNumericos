import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.dadosZDF import dados
# Importando Funções
from ZeroDeFunções.Funções.f import f

def gerarGráfico(d):
	título("Gráfico da Função", '=')
	delta = 1e-3

	x=np.arange(d.a,d.b,delta)
	pp.title("Gráfico Função e Derivada")
	pp.xlabel("X")
	pp.ylabel("f (X)")
	pp.plot(x,x-x,'k',x,f(x,d.sf),'k',x,f(x,d.sdf),'r')
	pp.show()