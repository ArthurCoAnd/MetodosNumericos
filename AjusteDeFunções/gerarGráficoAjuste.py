import math
import matplotlib.pyplot as pp
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f

def gerarGráfico(pts,sf):
	delta = 1e-3

	x=np.arange(int(min(pts[0])-1),int(max(pts[0])+1),delta)
	y=np.vectorize(f)
	pp.title("Gráfico da Função e do Pontos")
	pp.xlabel("X")
	pp.ylabel("f(X) & Pontos")
	pp.plot(x,x-x,'k',x,y(x,sf),'k',pts[0],pts[1],'o')
	pp.show()