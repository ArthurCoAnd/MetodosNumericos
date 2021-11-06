# Importar Bibliotecas
from numpy import matrix

def GaussSeidel(mat, vet, e):
	k = 0
	matX = vet
	pap = "Gauss-Seidel\n\n"
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