# Importar Bibliotecas
from Ferramentas.f import f
from Ferramentas.erro import erro
from time import time

def Bissecção(d, k=1):
	ti = time()
	fa = f(d["a"],d["sf"])
	fb = f(d["b"],d["sf"])
	x = (d["a"]+d["b"])/2
	fx = f(x,d["sf"])
	er = erro(d["a"],d["b"],fx)
	resultados = [[d["a"],x,d["b"],er,fa,fx,fb]]
	while (er > d["e"] and k < d["km"]):
		k+=1
		if fa*fx < 0:
			d["b"] = x
			fb = fx
		else:
			d["a"] = x
			fa = fx
		x = (d["a"]+d["b"])/2
		fx = f(x,d["sf"])
		er = erro(d["a"],d["b"],fx)
		resultados.append([d["a"],x,d["b"],er,fa,fx,fb])
	print(f"{time()-ti}s")
	return k, x, fx, er, resultados
