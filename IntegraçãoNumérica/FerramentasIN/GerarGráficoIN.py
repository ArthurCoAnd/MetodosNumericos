import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Importar Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN

def gerarGráficoIN(d,rep,divs):
	título("Gráfico da Função", '=')
	pp.title("Gráfico Função e Integração Numérica")
	pp.xlabel("X")
	pp.ylabel("f(X)")
	# Definir Dados
	sf = tSf(d.sf)
	delta = 1e-3
	x = np.arange(float(d.a),float(d.b),delta)
	y = np.vectorize(f)
	# Gerar Gráfico da Função
	pp.plot(x,x-x,'k',linewidth=3)
	pp.plot(x,y(x,sf),'k',linewidth=2)
	# Gerar Inegração Numérica
	if(rep):
		n = (int(d.m)+1)*(divs)
		x = np.linspace(float(d.a),float(d.b),n)
		pp.plot(x,y(x,sf),'r',x,y(x,sf),'o')

	else:
		n = divs+1
		x = np.linspace(float(d.a),float(d.b),n)
		pp.plot(x,y(x,sf),'r',x,y(x,sf),'o')

	pp.show()