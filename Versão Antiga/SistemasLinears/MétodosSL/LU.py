# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.título import título

def LU(mat, prec):
	título("Fatoração LU", "=")
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
	print("Matriz A")
	print(str(matA))

	# Matriz B
	matB = []
	c = nV
	for l in range (nV):
		matB.append(mat[l][c])
	matB = mm.matrix(matB)
	print("Matriz B")
	print(str(matB))

	# Matriz P L U
	matP, matL, matU = mm.lu(matA)
	print("Matriz P")
	print(str(matP))

	print("Matriz L")
	print(str(matL))

	print("Matriz U")
	print(str(matU))

	# Matriz X
	matX = mm.lu_solve(matA, matB)
	print("Matriz X")
	print(str(matX))

	# Erro
	matE = mm.residual(matA, matX, matB)
	print("Matriz Erro Residual")
	print(str(matE))

	# Resposta e Resíduo
	resp = "Fatoração LU:"
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(matX[l])
	ress = "Resíduo:"
	for l in range (nV):
		ress += "\nx("+str(l+1)+") = "+str(matE[l])

	return resp, ress