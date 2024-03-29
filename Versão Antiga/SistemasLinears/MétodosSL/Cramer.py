# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.título import título

def Cramer(mat, prec):
	título("Cramer", "=")
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

	# Determinante de A
	detA = mm.det(matA)
	print("Determinante de A = "+str(detA))

	# Matriz B
	matB = []
	c = nV
	for l in range (nV):
		matB.append(mat[l][c])
	matB = mm.matrix(matB)
	print("Matriz B")
	print(str(matB))

	# Matriz Inversa de A
	# matInvA = matA**-1
	# print("Matriz Inversa A")
	# print(str(matInvA))

	# Verificar Matriz Inversa A
	# matVer = matA*matInvA
	# print("matriz A * Matriz Inversa A")
	# print(str(matVer))

	# Matriz X
	# matX = matInvA * matB
	# print("Matriz X")
	# print(str(matX))

	# Matriz X
	matX = []
	for n in range(nV):
		# Matriz An
		matAn = []
		for l in range(nV):
			matAn.append([])
			for c in range(nV):
				if c == n:
					matAn[l].append(matB[l])
				else:
					matAn[l].append(matA[l,c])
		matAn = mm.matrix(matAn)
		print(f"Matriz A{n}")
		print(str(matAn))
		detAn = mm.det(matAn)
		print(f"Determinante de A{n} = "+str(detAn))
		xn = mm.mpf(detAn/detA)
		matX.append(xn)
	matX = mm.matrix(matX)
	print("Matriz X")
	print(str(matX))
		
	# Erro
	matE = mm.residual(matA, matX, matB)
	print("Matriz Erro Residual")
	print(str(matE))

	# Resposta e Resíduo
	resp = "Cramer:"
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(matX[l])
	ress = "Resíduo:"
	for l in range (nV):
		ress += "\nx("+str(l+1)+") = "+str(matE[l])

	return resp, ress