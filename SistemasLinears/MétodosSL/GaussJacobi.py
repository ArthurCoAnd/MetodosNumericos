# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.título import título

def GaussJacobi(mat, matx, prec, e):
	título("Gauss-Jacobi", "=")
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

	# Matriz X
	matx = mm.matrix(matx)
	# print("Matriz X")
	# print(str(matx))

	# Matriz
	mat = mm.matrix(mat)
	print("Matriz")
	print(str(mat))

	# Gerar Matrix X
	k = 0
	while(True):
		nmatx = mm.matrix(CalcularMatX(mm.matrix(mat), matx, prec))
		eMat = abs(MaiorModMat(nmatx, matx, prec))
		matx = mm.matrix(nmatx)
		k += 1
		if(eMat<e):
			break
	matx = mm.matrix(matx)
	print("Matriz X("+str(k)+")")
	print(str(matx))

	# Erro/Resíduo
	matE = mm.residual(matA, matx, matB)
	print("Matriz Erro Residual")
	print(str(matE))

	# Resposta e Resíduo
	resp = "Método Gauss-Jacobi:\nIterações - "+str(k)+"\nε - "+str(eMat)
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(matx[l])
	ress = "Resíduo:"
	for l in range (nV):
		ress += "\nx("+str(l+1)+") = "+str(matE[l])

	return resp, ress

def CalcularMatX(mat, matx, prec):
	# Precisão de Dígitos
	mm.mp.dps = prec

	# Número de Variáveis
	nV = len(mat)

	mx = []
	for l in range(nV):
		x = mm.mpf(mat[l,nV])
		for c in range(nV):
			if(l != c):
				x = mm.mpf(x - (mat[l,c]*matx[c]))
		x = mm.mpf(x/mat[l,l])
		mx.append(x)

	return mm.matrix(mx)

def MaiorModMat(mat, matm, prec):
	# Precisão de Dígitos
	mm.mp.dps = prec

	# Número de Variáveis
	nV = len(mat)

	maior = mm.mpf(abs(mat[0]-matm[0]))
	for i in range(1,nV):
		if(abs(mat[i]-matm[i])>maior):
			maior = mm.mpf(abs(mat[i]-matm[i]))
	
	return maior