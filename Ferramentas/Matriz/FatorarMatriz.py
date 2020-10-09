# Importar Bibliotecas
import mpmath as mm

	# ===== FATORAÇÃO DE MATRIZ USANDO BIBLIOTECA MPMATH =====
def FatorarMatriz(mat, prec):
	mm.mp.dps = prec
	matFat = mat.copy()
	for d in range (matFat.rows):
		for l in range (d+1, matFat.rows):
			div = mm.mpf(matFat[l,d]/matFat[d,d])
			for c in range (matFat.cols):
				matFat[l,c] = mm.mpf(matFat[l,c]-(div*matFat[d,c]))
	
	return matFat

	# ===== FATORAÇÃO DE MATRIZ SEM USAR BIBLIOTECA MPMATH =====
# def FatorarMatriz(mat, prec):
# 	mm.mp.dps = prec
# 	for d in range (len(mat)):
# 		for l in range (d+1, len(mat)):
# 			div = mm.mpf(mat[l][d]/mat[d][d])
# 			for c in range (len(mat[0])):
# 				mat[l][c]=mm.mpf(mat[l][c]-(div*mat[d][c]))
	
# 	return mat