# Importar Bibliotecas
import os
from time import time
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro
from Ferramentas.título import título as ttl

def Secante(d, k=1):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Secante","=")
	pap = f"Função - f(x)\t\t{d['sf']}\n"
	pap += f"Ponto inicial - x0\t{d['x0']}\n"
	pap += f"Ponto inicial - x1\t{d['x1']}\n"
	ti = time()
	xa = d["x0"]
	fxa = f(xa,d["sf"])
	x = d["x1"]
	fx = f(x,d["sf"])
	xm = (xa*fx-x*fxa)/(fx-fxa)
	er = erro(xa,x,fxa)
	resultados = [xa, x, er, fxa]
	while (er > d["e"] and k < d["km"]):
		k+=1
		xa = x
		fxa = fx
		x = xm
		fx = f(x,d["sf"])
		xm = (xa*fx-x*fxa)/(fx-fxa)
		er = erro(xa,x,fxa)
		resultados.append([x, xm, er, fx])
	pap += f"Iterações - k\t\t{k}\n"
	pap += f"Raiz - xk\t\t{x}\n"
	pap += f"Valor de f(xk)\t\t{fx}\n"
	pap += f"Erro\t\t\t{er}\n"
	pap += f"Tempo de execução\t{time()-ti}s\n"
	print(pap)
	return k, x, fx, er, resultados