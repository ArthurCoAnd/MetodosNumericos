# Importar Bibliotecas
import os
from time import time
from numpy import zeros
# Importar Ferramentas
from Ferramentas.título import título as ttl
from SistemasLineares.Ferramentas.FatorarMatriz import FatorarMatriz as FM

def EliminaçãoDeGauss(mat, piv=0, pivT=0):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Eliminação de Gauss","=")
	ti = time()
	pap = ""
	nv = len(mat)
	matFat, index = FM(mat, piv, pivT)
	# Matriz X
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub+(matFat[d][c]*matX[c])
		matX[d] = (matFat[d][nv]-sub)/matFat[d][d]
	matG = zeros(nv)
	for x in range(nv):
		matG[index[x]-1] = matX[x]
	pap += f"Tempo de execução: {time()-ti}s"
	print(pap)
	return matG