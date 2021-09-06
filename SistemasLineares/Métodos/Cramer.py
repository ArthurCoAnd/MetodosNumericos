# Importar Bibliotecas
import os
from time import time
from numpy import matrix
# Importar Ferramentas
from Ferramentas.título import título as ttl
from SistemasLineares.Ferramentas.Determinante import determinant_recursive as det

def Cramer(mat):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Cramer","=")
	pap = ""
	ti = time()
	nv = len(mat)
	matA = []
	for l in range(nv):
		matA.append([])
		for c in range(nv):
			matA[l].append(mat[l][c])
	dA = det(matA)
	pap += f"Matriz A\n"
	pap += str(matrix(matA))
	pap += f"\nDeterminante de A: {dA}"
	matB = []
	for l in range(nv):
		matB.append(mat[l][nv])
	pap += f"\n\nMatriz B\n"
	pap += str(matrix(matB))
	deltaX = []
	dX = []
	for x in range(nv):
		deltaX.append([])
		for l in range(nv):
			deltaX[x].append([])
			for c in range(nv):
				if c == x:
					deltaX[x][l].append(matB[l])
				else:
					deltaX[x][l].append(matA[l][c])
		dX.append(det(deltaX[x]))
	matX = []
	for x in range(nv):
		matX.append(dX[x]/dA)
		pap += f"\n\nMatriz Delta {x}\n"
		pap += str(matrix(deltaX[x]))
		pap += f"\nDeterminante Delta {x}: {dX[x]}"
		pap += f"\nX{x} = {matX[x]}"
	pap += f"\n\nMatriz X\n"
	pap += str(matrix(matX))
	pap += f"\n\nTempo de execução: {time()-ti}s"
	print(pap)
	return matX