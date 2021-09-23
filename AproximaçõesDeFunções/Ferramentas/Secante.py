# Importar Bibliotecas
from Ferramentas.f import f
from Ferramentas.erro import erro

def Secante(p, sf, k=1):
	# Definir erro mínimo
	e = 1/(len(p)*100)
	# Definir máximo de iterações
	km = len(p)*10
	# Definir menor e maior valor de X
	min = p[0][0]
	max = p[0][0]
	for i in range(1,len(p)):
		if p[i][0] < min:
			min = p[i][0]
		if p[i][0] > max:
			max = p[i][0]
	xa = min
	fxa = f(xa,sf)
	x = max
	fx = f(x,sf)
	xm = (xa*fx-x*fxa)/(fx-fxa)
	er = erro(xa,x,fxa)
	resultados = [xa, x, er, fxa]
	while (er > e and k < km):
		k+=1
		xa = x
		fxa = fx
		x = xm
		fx = f(x,sf)
		xm = (xa*fx-x*fxa)/(fx-fxa)
		er = erro(xa,x,fxa)
		resultados.append([x, xm, er, fx])
	return x