# Importar Bibliotecas
from numpy import zeros
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro

def BirgeVieta(p,d,k=1):
	pap = "Birge-Vieta\n\n"
	pap += f"Função - f(x): {d['sf']}\n"
	gp = len(p)
	x = d["x0"]
	fx = f(x,d["sf"])
	er = fx
	resultados = [[k,x,fx,er]]
	pap += f"\nIteração - {k}\n"
	pap += f"x = {x} -> f(x) = {fx}\n"
	pap += f"Erro: {er}\n"
	while(True):
		k += 1
		b = zeros(gp)
		for i in range(gp-1,-1,-1):
			if i == gp-1:
				b[i] = p[i]
			else:
				b[i] = p[i] + b[i+1]*x
		c = zeros(gp)
		for i in range(gp-1,0,-1):
			if i == gp-1:
				c[i] = b[i]
			else:
				c[i] = b[i] + c[i+1]*x
		xm = x - (b[0]/c[1])
		fx = f(xm,d["sf"])
		er = erro(x,xm,fx)
		x = xm
		resultados.append([k,xm,fx,er])
		pap += f"\nIteração - {k}\n"
		pap += f"b = {b}\n"
		pap += f"c = {c}\n"
		pap += f"x = {xm} -> f(x) = {fx}\n"
		pap += f"Erro: {er}\n"
		if er < d["e"] or k > d["km"]:
			break
	pap += f"\nIterações (k): {k}\n"
	pap += f"Raiz (xk): {x}\n"
	pap += f"Valor de f(xk): {fx}\n"
	pap += f"Erro: {er}"
	print(pap)
	return k-1, x, fx, er, resultados, pap