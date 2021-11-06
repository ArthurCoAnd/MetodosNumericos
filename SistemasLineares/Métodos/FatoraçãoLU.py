# Importar Bibliotecas
from numpy import matrix, zeros
# Importar Ferramentas
from SistemasLineares.Ferramentas.DecomposiçãoLU import DecomposiçãoLU

def FatoraçãoLU(mat, piv=0, pivT=0):
	nv = len(mat)
	pap = "Fatoração LU\n\n"
	matA = []
	for l in range(nv):
		matA.append([])
		for c in range(nv):
			matA[l].append(mat[l][c])
	pap += f"Matriz A:\n{str(matrix(matA))}"
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	pap += f"\n\nMatriz A:\n{str(matrix(matB))}"
	matL, matU = DecomposiçãoLU(matA)
	pap += f"\n\nMatriz L:\n{str(matrix(matL))}"
	pap += f"\n\nMatriz U:\n{str(matrix(matU))}"
	matY = zeros(nv)
	for d in range(nv):
		sub = 0
		for c in range(d):
			sub = sub+(matL[d][c]*matY[c])
		matY[d] = (matB[d]-sub)/matL[d][d]
	pap += f"\n\nMatriz Y:\n{str(matrix(matY))}"
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub + matU[d][c]*matX[c]
		matX[d] = (matY[d]-sub)/matU[d][d]
	pap += f"\n\nMatriz X:\n{str(matrix(matX))}"
	print(pap)
	return matX, pap