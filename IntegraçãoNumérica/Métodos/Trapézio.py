# Importar Bibliotecas
import os
from time import time
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título as ttl
from IntegraçãoNumérica.Ferramentas.c4análise import c4análise as c4a

def Trapézio(d):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Trapézio","=")
	ti = time()
	pap = ""

	sf = d["sf"]
	if d["sdsf"] == "":
		sdsf = "0"
	else:
		sdsf = d["sdsf"]
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
		else:
			I += 2*f(xi,sf)
	I = (h/2)*I
	
	# Calculo do Erro
	E = (m*(h**3)/12)*c4a(a,b,sdsf)
	if E == 0: E = "-"

	pap += f"Integral\t\t{I}\n"
	pap += f"Erro\t\t\t{E}\n"
	pap += f"Tempo de execução\t{time()-ti}s"
	print(pap)

	return I, E