import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf

def gerarGráficoZDF(d):
	título("Gráfico da Função", '=')
	sf = tSf(d.sf)
	delta = 0.001
	x=np.arange(float(d.a),float(d.b),delta)
	y=np.vectorize(f)
	dy=np.vectorize(f)
	if d.sdf != "":
		sdf = tSf(d.sdf)
		pp.title("Gráfico da Função e Derivada")
		pp.xlabel("X")
		pp.ylabel("f(X) & f'(X)")
		pp.plot(x,x-x,'k',x,y(x,sf),'k',x,dy(x,sdf),'r')
	else:
		pp.title("Gráfico da Função")
		pp.xlabel("X")
		pp.ylabel("f(X)")
		pp.plot(x,x-x,'k',x,y(x,sf),'k')
	pp.show()