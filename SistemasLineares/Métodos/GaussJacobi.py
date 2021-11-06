# Importar Bibliotecas
from numpy import matrix

def GaussJacobi(mat, vet, e):
	k = 0
	matX = vet
	pap = "Gauss-Jacobi\n\n"
	pap += f"Matriz Base:\n{str(matrix(mat))}\n"
	pap += f"x({k}): {str(matrix(matX))}\n"
	while(True):
		k += 1
		nmatX = CalcularMatX(mat, matX)
		eMat = abs(MaiorModMat(nmatX, matX))
		matX = nmatX
		pap += f"\nIteração {k}\n"
		pap += f"x({k}): {str(matrix(matX))}\n"
		pap += f"Erro: {eMat}\n"
		if eMat<e or k>999:
			break
	print(pap)
	return matX, pap

def CalcularMatX(mat, matx):
	nv = len(mat)
	mx = []
	for l in range(nv):
		x = mat[l][nv]
		for c in range(nv):
			if(l != c):
				x = x - (mat[l][c]*matx[c])
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