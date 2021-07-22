# Importar Biblioteclas
import numpy as np
import matplotlib.pyplot as pp
# Importar Ferramentas
from Ferramentas.f import f

def GerarGráfico(p,sf):
	px = []
	py = []
	for i in range(len(p)):
		px.append(p[i][0])
		py.append(p[i][1])
	minX = px[0]
	maxX = py[0]
	for i in range(1,len(px)):
		if px[i] < minX:
			minX = px[i]
		if px[i] > maxX:
			maxX = px[i]
	pp.style.use("ggplot")
	pp.xlabel("x")
	delt = (maxX-minX)*0.05
	x = np.linspace(minX-delt,maxX+delt,10000)
	y = np.vectorize(f)
	pp.plot(px,py,"or")
	pp.plot(x,y(x,sf),"-b", linewidth=2)
	pp.ylabel("f(x)")
	pp.title ("Função")
	pp.show()