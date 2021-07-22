# Importar Biblioteclas
import numpy as np
import matplotlib.pyplot as pp
# Importar Ferramentas
from Ferramentas.f import f

def GerarGráfico(d):
	pp.style.use("ggplot")
	pp.xlabel("x")
	x = np.linspace(d["a"],d["b"],10000)
	y = np.vectorize(f)
	dy = np.vectorize(f)
	pp.plot((d["a"],d["b"]),(0,0),"-k")
	pp.plot(x,y(x,d["sf"]),"-b")
	try:
		pp.plot(x,dy(x,d["sdf"]),"-r")
		pp.ylabel("f(x) e f'(x)")
		pp.title ("Função e Derivada")
	except:
		pass
		pp.ylabel("f(x)")
		pp.title ("Função")
	pp.show()