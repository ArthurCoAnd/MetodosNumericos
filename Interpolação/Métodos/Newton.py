# Importar Bibliotecas
import os
from time import time
from traceback import print_tb
from numpy.polynomial.polynomial import Polynomial, polyadd, polymul
from numpy import zeros
from numpy import shape
# Importar Ferramentas
from Ferramentas.título import título as ttl
from Interpolação.Ferramentas.pol2str import pol2str


def Newton(p):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Newton","=")
	ti = time()
	pap = ""
	np = len(p)

	# Direta
	pap += "Diretaz\n"
	pol = p.copy()
	matX = []
	matY = []
	for i in range(np):
		matX.append(pol[i][0])
		matY.append(pol[i][1])
	coeff_vector = getNDDCoeffs(matX,matY)
	pap += f"Coeficientes de Newton = {coeff_vector}\n"
	final_pol = Polynomial([0.])
	n = coeff_vector.shape[0]
	for i in range(n):
		pol = Polynomial([1.])
		for j in range(i):
			p_temp = Polynomial([-matX[j],1.])
			pol = polymul(pol,p_temp)
		pol *= coeff_vector[i]
		final_pol = polyadd(final_pol,pol)
	pol = final_pol[0].coef
	direta = pol2str(pol)
	pap += f"Função Direta = {direta}\n"

	# Inversa
	pap += "\nInvera\n"
	pol = p.copy()
	matX = []
	matY = []
	for i in range(np):
		matX.append(pol[i][1])
		matY.append(pol[i][0])
	coeff_vector = getNDDCoeffs(matX,matY)
	pap += f"Coeficientes de Newton = {coeff_vector}\n"
	final_pol = Polynomial([0.])
	n = coeff_vector.shape[0]
	for i in range(n):
		pol = Polynomial([1.])
		for j in range(i):
			p_temp = Polynomial([-matX[j],1.])
			pol = polymul(pol,p_temp)
		pol *= coeff_vector[i]
		final_pol = polyadd(final_pol,pol)
	pol = final_pol[0].coef
	inversa = pol2str(pol)
	pap += f"Função Inversa = {inversa}\n"

	pap += f"\nTempo de execução = {time()-ti}"
	print(pap)
	return direta, inversa

def getNDDCoeffs(x, y):
	n = shape(y)[0]
	pyramid = zeros([n,n])
	pyramid[::,0] = y
	for j in range(1,n):
		for i in range(n-j):
			pyramid[i][j] = (pyramid[i+1][j-1]-pyramid[i][j-1])/(x[i+j]-x[i])
	return pyramid[0]