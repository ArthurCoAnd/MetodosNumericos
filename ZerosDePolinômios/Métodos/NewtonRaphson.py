# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro

def NewtonRaphson(p,d,k=1):
	pap = "Newton Raphson\n\n"
	pap += f"Função - f(x)\t\t{d['sf']}\n"
	gp = len(p)
	x = d["x0"]
	fx = f(x,d["sf"])
	er = fx
	resultados = [[k,x,fx,er]]
	while(True):
		k += 1
		dfx = 0
		for i in range(1,gp):
			dfx += i*p[i]*x**(i-1)
		xm = x - (fx/dfx)
		fx = f(xm,d["sf"])
		er = erro(x,xm,fx)
		x = xm
		resultados.append([k,xm,fx,er])
		if er < d["e"] or k > d["km"]:
			break
	pap += f"Iterações - k\t\t{k-1}\n"
	pap += f"Raiz - xk\t\t{x}\n"
	pap += f"Valor de f(xk)\t\t{fx}\n"
	pap += f"Erro\t\t\t{er}"
	print(pap)
	return k-1, x, fx, er, resultados, pap