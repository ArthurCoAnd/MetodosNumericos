# Importar Bibliotecas
import os
from time import time
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro
from Ferramentas.título import título as ttl

def PosiçãoFalsa(d, k=1):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Posição Falsa","=")
	pap = f"Função - f(x)\t\t{d['sf']}\n"
	pap += f"Limite inferior - a\t{d['a']}\n"
	pap += f"Limite superior - b\t{d['b']}\n"
	ti = time()
	fa = f(d["a"],d["sf"])
	fb = f(d["b"],d["sf"])
	x = (d["a"]*abs(fb) + d["b"]*abs(fa)) / (abs(fa) + abs(fb))
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
		x = (d["a"]*abs(fb) + d["b"]*abs(fa)) / (abs(fa) + abs(fb))
		fx = f(x,d["sf"])
		er = erro(d["a"],d["b"],fx)
		resultados.append([d["a"],x,d["b"],er,fa,fx,fb])
	pap += f"Iterações - k\t\t{k}\n"
	pap += f"Raiz - xk\t\t{x}\n"
	pap += f"Valor de f(xk)\t\t{fx}\n"
	pap += f"Erro\t\t\t{er}\n"
	pap += f"Tempo de execução\t{time()-ti}s\n"
	print(pap)
	return k, x, fx, er, resultados