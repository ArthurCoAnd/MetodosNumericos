# Importar Ferramentas
from Ferramentas.f import f
from IntegraçãoNumérica.Ferramentas.c4análise import c4análise as c4a

def Simpson13(d):
	pap = "1/3 de Simpson\n\n"

	sf = d["sf"]
	if d["sdqf"] == "":
		sdqf = "0"
	else:
		sdqf = d["sdqf"]
	a = d["a"]
	b = d["b"]
	m = d["m"]
	h = (b-a)/m
	
	pap += f"Função - f(x)\t\t{sf}\n"
	pap += f"Limite inferior - a\t{a}\n"
	pap += f"Limite superior - b\t{b}\n"
	pap += f"Subdivisões - m\t\t{m}\n"
	pap += f"Tamanho subdivisões - h\t{h}\n"
	
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
	E = (m*(h**5)/180)*c4a(a,b,sdqf)
	if E == 0: E = "-"

	pap += f"Integral\t\t{I}\n"
	pap += f"Erro\t\t\t{E}"
	print(pap)

	return I, E, pap