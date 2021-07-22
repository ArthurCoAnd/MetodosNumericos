# Importar Bibliotecas
from Ferramentas.f import f
from Ferramentas.erro import erro

def Secante(d, k=1):
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
	return k, x, fx, er, resultados