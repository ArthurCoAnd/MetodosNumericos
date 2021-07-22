# Importar Biblioteclas
import numpy as np
import matplotlib.pyplot as pp
# Importar Ferramentas
from Ferramentas.f import f

def GerarGráfico(d):
	pp.style.use("ggplot")
	pp.xlabel("x")
	h = (d["b"]-d["a"])/d["m"]
	xm = np.arange(d["a"],d["b"]+h,h)
	x = np.linspace(d["a"],d["b"],10000)
	y = np.vectorize(f)
	pp.plot((d["a"],d["b"]),(0,0),"-k", linewidth=1)
	pp.plot(xm,y(xm,d["sf"]),"-r", linewidth=1)
	pp.stem(xm,y(xm,d["sf"]),"-r")
	pp.plot(x,y(x,d["sf"]),"-b", linewidth=2)
	pp.show()