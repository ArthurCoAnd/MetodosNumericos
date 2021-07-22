# Importar Bibliotecas
import mpmath as mm

	# ===== FATORAÇÃO DE MATRIZ USANDO BIBLIOTECA MPMATH =====
def FatorarMatriz(mat, prec, piv=0, pivT=0):
	mm.mp.dps = prec
	index = [] 
	for i in range(mat.rows):
		index.append(i+1)
	matFat = mat.copy()
	for d in range (matFat.rows):
		# Executa Pivotamento (Parcial ou Total)
		if(piv==1 or pivT==1):
			matFat = pivotar(matFat, d, prec, pivT, index)
		for l in range (d+1, matFat.rows):
			div = mm.mpf(matFat[l,d]/matFat[d,d])
			for c in range (matFat.cols):
				matFat[l,c] = mm.mpf(matFat[l,c]-(div*matFat[d,c]))
	
	return matFat, index

def pivotar(mat, d, prec, tot, index):
	mm.mp.dps = prec
	# Elemento de Maior Módulo
	maior = abs(mat[d,d])
	lmaior = d
	cmaior = d
	# Verificar Se é Pivotamento Total
	cf = d+1
	if(tot==1):
		cf = mat.rows
	# Procurar Posição do Elemento de Maior Módulo
	for l in range(d,mat.rows):
		for c in range(d,cf):
			if(maior<abs(mat[l,c])):
				lmaior = l
				cmaior = c
				maior = abs(mat[l,c])

	if(lmaior != d):
		if(cmaior != d):
			# Trocar Linha D pela Linha do Elemento de Maior Módulo
			for c in range(d,mat.cols):
				mat[d,c], mat[lmaior,c] = mat[lmaior,c], mat[d,c]
			# Trocar Coluna D pela Coluna do Elemento de Maior Módulo
			for l in range(0,mat.rows):
				mat[l,d], mat[l,cmaior] = mat[l,cmaior], mat[l,d]
			index[cmaior], index[d] = index[d], index[cmaior]
		else:
			for c in range(d,mat.cols):
				mat[d,c], mat[lmaior,c] = mat[lmaior,c], mat[d,c]

	return mat