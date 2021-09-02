# Importar Bibliotecas
import os
from time import time
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
# Importar Ferramentas
from Ferramentas.título import título as ttl
from Interpolação.Ferramentas.pol2str import pol2str

def Lagrange(p):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Lagrange","=")
	ti = time()
	pap = ""
	np = len(p)
	matX = []
	matY = []
	for i in range(np):
		matX.append(p[i][0])
		matY.append(p[i][1])
	poly = lagrange(matX, matY)
	poly = Polynomial(poly).coef
	poly = poly[::-1]
	strPol = pol2str(poly)
	pap += f"Função = {strPol}\n"
	pap += f"\nTempo de execução = {time()-ti}"
	print(pap)
	return strPol
