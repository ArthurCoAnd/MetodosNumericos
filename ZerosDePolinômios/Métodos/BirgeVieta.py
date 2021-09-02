# Importar Bibliotecas
import os
from time import time
from numpy import zeros
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro
from Ferramentas.título import título as ttl

def BirgeVieta(p,d,k=1):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("BirgeVieta","=")
	pap = f"Função - f(x)\t\t{d['sf']}\n"
	ti = time()
	gp = len(p)
	x = d["x0"]
	fx = f(x,d["sf"])
	er = fx
	resultados = [[k,x,fx,er]]
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
		if er < d["e"] or k > d["km"]:
			break
	pap += f"Iterações - k\t\t{k-1}\n"
	pap += f"Raiz - xk\t\t{x}\n"
	pap += f"Valor de f(xk)\t\t{fx}\n"
	pap += f"Erro\t\t\t{er}\n"
	pap += f"Tempo de execução\t{time()-ti}s\n"
	print(pap)
	return k-1, x, fx, er, resultados