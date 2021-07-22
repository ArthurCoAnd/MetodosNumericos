# Importar Bibliotecas
from numpy import zeros
from math import sqrt

def DecomposiçãoCholesky(L,U):
	nv = len(L)
	Lt = U.copy()
	D = zeros((nv,nv))
	for l in range(nv):
		D[l][l] = U[l][l]
		for c in range(l,nv):
			Lt[l][c] = Lt[l][c]/D[l][l]
	Dl = D.copy()
	for d in range(nv):
		Dl[d][d] = sqrt(Dl[d][d])
	G = L.copy()
	for l in range(nv):
		for c in range(l+1):
			G[l][c] = G[l][c]*Dl[c][c]
	Gt = Lt.copy()
	for l in range(nv):
		for c in range(l,nv):
			Gt[l][c] = Gt[l][c]*Dl[l][l]
	return G, Gt