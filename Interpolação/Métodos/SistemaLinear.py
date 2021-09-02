# Importar Bibliotecas
import os
from time import time
from numpy import zeros
# Importar Ferramentas
from Ferramentas.título import título as ttl
from Ferramentas.FatorarMatriz import FatorarMatriz as FM
from Interpolação.Ferramentas.pol2str import pol2str

def SistemaLinear(p):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Sistema Linear","=")
	ti = time()
	pap = ""
	nv = len(p)
	matA = []
	matY = []
	for i in range(nv):
		matA.append([])
		for g in range(nv):
			matA[i].append(p[i][0]**g)
		matY.append(p[i][1])
	mat = zeros((nv,nv+1))
	for l in range(nv):
		for c in range(nv):
			mat[l][c] = matA[l][c]
		mat[l][nv] = matY[l]
	matFat, index = FM(mat)
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub+(matFat[d][c]*matX[c])
		matX[d] = (matFat[d][nv]-sub)/matFat[d][d]
	strPol = pol2str(matX)
	pap += f"Função = {strPol}\n"
	pap += f"\nTempo de execução = {time()-ti}"
	print(pap)
	return strPol