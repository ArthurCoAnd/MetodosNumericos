# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro

def PosiçãoFalsa(d, k=1):
	pap = "Posição Falsa\n\n"
	pap += f"Função - f(x)\t\t{d['sf']}\n"
	pap += f"Limite inferior - a\t{d['a']}\n"
	pap += f"Limite superior - b\t{d['b']}\n"
	fa = f(d["a"],d["sf"])
	fb = f(d["b"],d["sf"])
	x = (d["a"]*abs(fb) + d["b"]*abs(fa)) / (abs(fa) + abs(fb))
	fx = f(x,d["sf"])
	er = erro(d["a"],d["b"],fx)
	resultados = [[d["a"],x,d["b"],er,fa,fx,fb]]
	while (er > d["e"] and k < d["km"]):
		pap += f"\nIteração - {k}\n"
		pap += f"a = {d['a']} -> f(a) = {fa}\n"
		pap += f"x = {x} -> f(x) = {fx}\n"
		pap += f"b = {d['b']} -> f(b) = {fb}\n"
		if fa*fx < 0:
			pap += f"fa*fx < 0 -> b = x & fb = fx\n"
			d["b"] = x
			fb = fx
		else:
			pap += f"fa*fx > 0 -> a = x & fa = fx\n"
			d["a"] = x
			fa = fx
		x = (d["a"]*abs(fb) + d["b"]*abs(fa)) / (abs(fa) + abs(fb))
		fx = f(x,d["sf"])
		er = erro(d["a"],d["b"],fx)
		resultados.append([d["a"],x,d["b"],er,fa,fx,fb])
		k+=1
		pap += f"Erro: {er}\n"
	pap += f"\nIterações (k): {k}\n"
	pap += f"Raiz (xk): {x}\n"
	pap += f"Valor de f(xk): {fx}\n"
	pap += f"Erro: {er}"
	print(pap)
	return k, x, fx, er, resultados, pap