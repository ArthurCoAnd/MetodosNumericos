# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.Matriz.FatorarMatriz import FatorarMatriz as fM
from Ferramentas.Matriz.MatrizInversa import MatrizInversa as MInv

def Cramer(mat, prec):
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

	# Matriz Inversa de A
	matInvA = matA**-1
	print("Matriz Inversa A")
	print(str(matInvA))

	# Verificar Matriz Inversa A
	matVer = matA*matInvA
	print("matriz A * Matriz Inversa A")
	print(str(matVer))

	# Matriz X
	X = matInvA * matB
	print("Matriz X")
	print(str(X))

	resp = "Cramer:"
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(X[l])

	return resp