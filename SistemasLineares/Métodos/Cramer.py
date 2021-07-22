# Importar Ferramentas
from SistemasLineares.Ferramentas.Determinante import determinant_recursive as det

def Cramer(mat):
	nv = len(mat)
	matA = []
	for l in range(nv):
		matA.append([])
		for c in range(nv):
			matA[l].append(mat[l][c])
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	deltaX = []
	for x in range(nv):
		deltaX.append([])
		for l in range(nv):
			deltaX[x].append([])
			for c in range(nv):
				if c == x:
					deltaX[x][l].append(matB[l])
				else:
					deltaX[x][l].append(matA[l][c])
	matX = []
	for x in range(nv):
		xx = det(deltaX[x])/det(matA)
		matX.append(xx)
	return matX