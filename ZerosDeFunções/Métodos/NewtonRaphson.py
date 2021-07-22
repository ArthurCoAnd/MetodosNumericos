# Importar Bibliotecas
from Ferramentas.f import f
from Ferramentas.erro import erro

def NewtonRaphson(d, k=1):
	x = d["x0"]
	fx = f(x,d["sf"])
	dfx = f(x,d["sdf"])
	xm = x - fx/dfx
	er = erro(x,xm,fx)
	resultados = [x, xm, er, fx]
	while (er > d["e"] and k < d["km"]):
		k+=1
		x = xm
		fx = f(x,d["sf"])
		dfx = f(x,d["sdf"])
		xm = x - fx/dfx
		er = erro(x,xm,fx)
		resultados.append([x, xm, er, fx])
	return k, x, fx, er, resultados