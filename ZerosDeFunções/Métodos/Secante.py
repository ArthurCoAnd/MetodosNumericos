# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.erro import erro

def Secante(d, k=1):
	pap = "Secante\n\n"
	pap += f"Função - f(x)\t\t{d['sf']}\n"
	pap += f"Ponto inicial - x0\t{d['x0']}\n"
	pap += f"Ponto inicial - x1\t{d['x1']}\n"
	xa = d["x0"]
	fxa = f(xa,d["sf"])
	x = d["x1"]
	fx = f(x,d["sf"])
	xm = (xa*fx-x*fxa)/(fx-fxa)
	er = erro(xa,x,fxa)
	resultados = [xa, x, er, fxa]
	while (er > d["e"] and k < d["km"]):
		pap += f"\nIteração - {k}\n"
		pap += f"x(n-1) = {xa} -> f(x(n-1)) = {fxa}\n"
		pap += f"x = {x} -> f(x) = {fx}\n"
		xa = x
		fxa = fx
		x = xm
		fx = f(x,d["sf"])
		xm = (xa*fx-x*fxa)/(fx-fxa)
		er = erro(xa,x,fxa)
		resultados.append([x, xm, er, fx])
		k+=1
		pap += f"x(n+1) = {xm} -> f(x(n+1)) = {fx}\n"
		pap += f"Erro: {er}\n"
	pap += f"\nIterações (k): {k}\n"
	pap += f"Raiz (xk): {x}\n"
	pap += f"Valor de f(xk): {fx}\n"
	pap += f"Erro: {er}"
	print(pap)
	return k, x, fx, er, resultados, pap