# Improtar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.Matriz.MatrizIdentidade import MatrizIdentidade as MId

def MatrizInversa(mat, prec):
	# Precisão Dígitos
	mm.mp.dps = prec

	# Número de Variáveis
	nV = len(mat)

	# Matriz Inversa iniciando como Matriz Identidade
	matInv = MId(nV, prec)

	for d in range (nV):
		div = mm.mpf(mat[d][d])
		# Dividir Linha da Diagonal pelo Termo da Diagonal
		for c in range (d,nV):
			mat[d][c] = mm.mpf(mat[d][c]/div)
			matInv[d][c] = mm.mpf(matInv[d][c]/div)
		# Subitrair Linhas ABAIXO da Diagonal
		for l in range (d+1,nV):
			div = mm.mpf(mat[l][d])
			for c in range (d,nV):
				mat[l][c] = mm.mpf(mat[l][c] - (mat[d][c]*div))
				matInv[l][c] = mm.mpf(matInv[l][c] - (matInv[d][c]*div))

	# print("Matriz Descida")
	# print(str(mm.matrix(mat)))
	# print("Matriz Inversa Descida")
	# print(str(mm.matrix(matInv)))

	for d in range (nV-2,-1,-1):
		div = mm.mpf(mat[d][d])
		# Dividir Linha da Diagonal pelo Termo da Diagonal
		for c in range (d):
			mat[d][c] = mm.mpf(mat[d][c]/div)
			matInv[d][c] = mm.mpf(matInv[d][c]/div)
		# Subitrair Linhas ACIMA da Diagonal
		for l in range (d):
			div = mm.mpf(mat[l][d])
			for c in range (d):
				mat[l][c] = mm.mpf(mat[l][c] - (mat[d][c]*div))
				matInv[l][c] = mm.mpf(matInv[l][c] - (matInv[d][c]*div))
	
	# print("Matriz Subida")
	# print(str(mm.matrix(mat)))

	# ===== COM PROBLEMAS =====
	
	return matInv