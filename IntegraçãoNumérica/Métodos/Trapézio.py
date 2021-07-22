# Importar Ferramentas
from Ferramentas.f import f

def Trapézio(d):
	sf = d["sf"]
	if d["sdsf"] == "":
		sdsf = 0
	else:
		sdsf = d["sdsf"]
	a = d["a"]
	b = d["b"]
	m = d["m"]
	if(d["ac"] == 1):
		c = d["c"]
	else:
		c = (b+a)/2
	h = (b-a)/m
	
	# Cálculo da Integral
	I = 0
	for i in range(m+1):
		xi = a+(i*h)
		if(i==0 or i==m):
			I += f(xi,sf)
		else:
			I += 2*f(xi,sf)
	I = (h/2)*I
	
	# Calculo do Erro
	E = (m*(h**3)/12)*f(c,sdsf)

	return I, E