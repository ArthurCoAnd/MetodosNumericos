# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.título import título
from Ferramentas.Matriz.FatorarMatriz import FatorarMatriz as fM

def Gauss(mat, prec, piv, pivT):
	título("Eliminação de Gauss", "=")
	# Precisão de Dígitos
	mm.mp.dps = prec
	
	# Número de Variáveis
	nV = len(mat)

	# Matriz A
	matA = []
	for l in range (nV):
		matA.append([])
		for c in range (nV):
			matA[l].append(mat[l][c])
	matA = mm.matrix(matA)
	# print("Matriz A")
	# print(str(matA))

	# Matriz B
	matB = []
	c = nV
	for l in range (nV):
		matB.append(mat[l][c])
	matB = mm.matrix(matB)
	# print("Matriz B")
	# print(str(matB))

	# Matriz
	mat = mm.matrix(mat)
	print("Matriz")
	print(str(mat))

	# Matriz Fatorada
	matFat = fM(mat, prec, piv, pivT)
	print("Matriz Fatorada")
	print(str(matFat))

	# Matriz X
	matX = mm.zeros(nV,1)
	for d in range (nV-1,-1,-1):
		sub = mm.mpf('0.0')
		for c in range (d+1,nV):
			sub = mm.mpf(sub+(matFat[d,c]*matX[c]))
		matX[d] = mm.mpf((matFat[d,nV]-sub)/matFat[d,d])
	print("Matriz X")
	print(str(matX))

	# Erro
	matE = mm.residual(matA, matX, matB)
	print("Matriz Erro Residual")
	print(str(matE))

	# Resposta e Resíduo
	resp = "Eliminação de Gauss:"
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(matX[l])
	ress = "Resíduo:"
	for l in range (nV):
		ress += "\nx("+str(l+1)+") = "+str(matE[l])

	return resp, ress