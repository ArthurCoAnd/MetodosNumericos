# Importar Bibliotecas
import mpmath as mm

def fatorarMatriz(mat, prec):
	mm.mp.dps = prec
	for d in range (len(mat)):
		for l in range (d+1, len(mat)):
			div = mm.mpf(mat[l][d]/mat[d][d])
			for c in range (len(mat[0])):
				mat[l][c]=mm.mpf(mat[l][c]-(div*mat[d][c]))
	
	return mat