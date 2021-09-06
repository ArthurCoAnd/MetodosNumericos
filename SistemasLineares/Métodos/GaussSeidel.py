# Importar Bibliotecas
import os
from time import time
# Importar Ferramentas
from Ferramentas.título import título as ttl

def GaussSeidel(mat, vet, e):
	os.system('cls' if os.name == 'nt' else 'clear')
	ttl("Gauss-Seidel","=")
	ti = time()
	pap = ""
	matX = vet
	k = 0
	while(True):
		nmatX = CalcularMatX(mat, matX)
		eMat = abs(MaiorModMat(nmatX, matX))
		matX = nmatX
		k += 1
		if eMat<e or k>999:
			break
	pap += f"Iterações (k): {k}\n"
	pap += f"Erro: {eMat}\n"
	pap += f"Tempo de execução: {time()-ti}s"
	print(pap)
	return matX

def CalcularMatX(mat, matX):
	nv = len(mat)
	mx = []
	for l in range(nv):
		x = mat[l][nv]
		for c in range(nv):
			# Utilizar Valores de Xk
			if(l < c):
				x = x - (mat[l][c]*matX[c])
			# Utilizar Valores de Xk+1 já encontrados
			if(l > c):
				x = x - (mat[l][c]*mx[c])
		x = x/mat[l][l]
		mx.append(x)
	return mx

def MaiorModMat(mat, matM):
	nv = len(mat)
	maior = abs(mat[0]-matM[0])
	for i in range(1,nv):
		if(abs(mat[i]-matM[i])>maior):
			maior = abs(mat[i]-matM[i])
	return maior