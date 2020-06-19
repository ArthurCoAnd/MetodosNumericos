import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
# Importando Funções
from ZeroDeFunções.Funções.f import f

def gerarGráfico(sf,sdf):
	título("Gráfico da Função", '=')
	pos = pedirFloat(s="X INICIAL do Gráfico")
	posF = pedirFloatMaiorQue(pos, s="X FINAL do Gráfico")
	delta = pedirFloat(s="Tamanho Entre os Intervalos")

	x=np.arange(pos,posF,delta)
	pp.title("Gráfico Função e Derivada")
	pp.xlabel("X")
	pp.ylabel("f (X)")
	pp.plot(x,x-x,'k',x,f(x,sf),'k',x,f(x,sdf),'r')
	pp.show()