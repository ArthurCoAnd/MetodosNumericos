# Importar Bibliotecas
from numpy import matrix, zeros
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
	pap += f"Matriz A:\n{str(matrix(matA))}"
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	pap += f"\n\nMatriz B:\n{str(matrix(matB))}"
	matL, matU = DecomposiçãoLU(matA)
	pap += f"\n\nMatriz L:\n{str(matrix(matL))}"
	pap += f"\n\nMatriz U:\n{str(matrix(matU))}"
	matG, matGt = DecomposiçãoCholesky(matL, matU)
	pap += f"\n\nMatriz G:\n{str(matrix(matG))}"
	pap += f"\n\nMatriz Gt:\n{str(matrix(matGt))}"
	matY = zeros(nv)
	for d in range(nv):
		sub = 0
		for c in range(d):
			sub = sub+(matG[d][c]*matY[c])
		matY[d] = (matB[d]-sub)/matG[d][d]
	pap += f"\n\nMatriz Y:\n{str(matrix(matY))}"
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub + matGt[d][c]*matX[c]
		matX[d] = (matY[d]-sub)/matGt[d][d]
	pap += f"\n\nMatriz X:\n{str(matrix(matX))}"
	print(pap)
	return matX, pap
