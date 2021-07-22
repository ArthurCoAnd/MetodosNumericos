# Importar Bibliotecas
from numpy import zeros
from numpy import identity

def DecomposiçãoLU(mat, piv=0, pivT=0):
	nv = len(mat)
	for d in range(nv):
		for l in range(d+1,nv):
			mat[l][d] = mat[l][d]/mat[d][d]
			for c in range(d+1,nv):
				mat[l][c] = mat[l][c] - mat[d][c]*mat[l][d]
	L = identity(nv)
	for l in range(1,nv):
		for c in range(l):
			L[l][c] = mat[l][c]
	U = zeros((nv,nv))
	for l in range(nv):
		for c in range(l,nv):
			U[l][c] = mat[l][c]
	return L,U