# Importar Ferramentas
from Ferramentas.f import f

def Simpson13(d):
	sf = d["sf"]
	if d["sdqf"] == "":
		sdqf = 0
	else:
		sdqf = d["sdqf"]
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
		elif(i%2==1):
			I += 4*f(xi,sf)
		else:
			I += 2*f(xi,sf)
	I = (h/3)*I
	
	# Calculo do Erro
	E = (m*(h**5)/180)*f(c,sdqf)

	return I, E