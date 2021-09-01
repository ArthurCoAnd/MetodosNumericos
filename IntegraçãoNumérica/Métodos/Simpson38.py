# Importar Ferramentas
from Ferramentas.f import f
from IntegraçãoNumérica.Ferramentas.c4análise import c4análise as c4a

def Simpson38(d):
	sf = d["sf"]
	if d["sdqf"] == "":
		sdqf = "0"
	else:
		sdqf = d["sdqf"]
	a = d["a"]
	b = d["b"]
	m = d["m"]
	h = (b-a)/m
	
	# Cálculo da Integral
	I = 0
	for i in range(m+1):
		xi = a+(i*h)
		if(i==0 or i==m):
			I += f(xi,sf)
		elif(i%3==1 or i%3==2):
			I += 3*f(xi,sf)
		else:
			I += 2*f(xi,sf)
	I = (3*h/8)*I
	
	# Calculo do Erro
	E = (m*(h**5)/80)*c4a(a,b,sdqf)
	if E == 0: E = "-"

	return I, E