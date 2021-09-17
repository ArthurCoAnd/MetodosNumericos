# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro

def NewtonRaphson(d, k=1):
	pap = "Newton-Raphson\n\n"
	pap += f"Função - f(x)\t\t{d['sf']}\n"
	pap += f"Ponto inicial - x0\t{d['x0']}\n"
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
	pap += f"Iterações - k\t\t{k}\n"
	pap += f"Raiz - xk\t\t{x}\n"
	pap += f"Valor de f(xk)\t\t{fx}\n"
	pap += f"Erro\t\t\t{er}"
	print(pap)
	return k, x, fx, er, resultados, pap