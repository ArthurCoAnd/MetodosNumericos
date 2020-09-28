import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Importar Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def gerarGráficoZDF(d):
	título("Gráfico da Função", '=')
	sf = tSf(dIN.sf)
	delta = 0.001
	x=np.arange(float(dIN.a),float(dIN.b),delta)
	y=np.vectorize(f)
	dy=np.vectorize(f)
	pp.title("Gráfico Função e Derivada")
	pp.xlabel("X")
	pp.ylabel("f(X) & f'(X)")
	pp.plot(x,x-x,'k',x,y(x,sf),'k',x,dy(x,sdf),'r')
	pp.show()