# Importar Bibliotecas
from numpy import zeros
# Importar Ferramentas
from SistemasLineares.Ferramentas.DecomposiçãoCholesky import DecomposiçãoCholesky
from SistemasLineares.Ferramentas.DecomposiçãoLU import DecomposiçãoLU

def FatoraçãoCholesky(mat):
	nv = len(mat)
	pap = "Fatoração Cholesky\n\n"
	matA = []
	for l in range(nv):
		matA.append([])
		for c in range(nv):
			matA[l].append(mat[l][c])
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	matL, matU = DecomposiçãoLU(matA)
	matG, matGt = DecomposiçãoCholesky(matL, matU)
	matY = zeros(nv)
	for d in range(nv):
		sub = 0
		for c in range(d):
			sub = sub+(matG[d][c]*matY[c])
		matY[d] = (matB[d]-sub)/matG[d][d]
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub + matGt[d][c]*matX[c]
		matX[d] = (matY[d]-sub)/matGt[d][d]
	print(pap)
	return matX, pap
