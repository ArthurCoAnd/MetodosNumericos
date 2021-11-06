# Importar Bibliotecas
from numpy import matrix, zeros
# Importar Ferramentas
from SistemasLineares.Ferramentas.FatorarMatriz import FatorarMatriz as FM

def EliminaçãoDeGauss(mat, piv=0, pivT=0):
	nv = len(mat)
	pap = "Eliminação de Gauss\n\n"
	pap += f"Matriz Base:\n{str(matrix(mat))}"
	matFat, index = FM(mat, piv, pivT)
	pap += f"\n\nMatriz Fatorada:\n{str(matrix(matFat))}"
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
	pap += f"\n\nMatriz X:\n{str(matrix(matG))}"
	print(pap)
	return matG, pap