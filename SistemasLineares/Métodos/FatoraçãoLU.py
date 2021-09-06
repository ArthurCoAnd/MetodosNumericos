# Importar Bibliotecas
import os
from time import time
from numpy import zeros
# Importar Ferramentas
from Ferramentas.título import título as ttl
from SistemasLineares.Ferramentas.DecomposiçãoLU import DecomposiçãoLU

def FatoraçãoLU(mat, piv=0, pivT=0):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Fatoração LU","=")
	ti = time()
	pap = ""
	nv = len(mat)
	matA = []
	for l in range(nv):
		matA.append([])
		for c in range(nv):
			matA[l].append(mat[l][c])
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	matL, matU = DecomposiçãoLU(matA)
	matY = zeros(nv)
	for d in range(nv):
		sub = 0
		for c in range(d):
			sub = sub+(matL[d][c]*matY[c])
		matY[d] = (matB[d]-sub)/matL[d][d]
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub + matU[d][c]*matX[c]
		matX[d] = (matY[d]-sub)/matU[d][d]
	pap += f"Tempo de execução: {time()-ti}s"
	print(pap)
	return matX