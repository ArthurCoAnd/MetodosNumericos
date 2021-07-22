def FatorarMatriz(mat, piv=0, pivT=0):
	nl = len(mat)
	nc = len(mat[0])
	matFat = mat.copy()
	index = [] 
	for i in range(nl):
		index.append(i+1)
	for d in range (nl):
		# Executa Pivotamento (Parcial ou Total)
		if(piv==1 or pivT==1):
			matFat = Pivotar(matFat, d, pivT, index)
		for l in range (d+1, nl):
			div = matFat[l][d]/matFat[d][d]
			for c in range(nc):
				matFat[l][c] = matFat[l][c]-(div*matFat[d][c])
	return matFat, index

def Pivotar(mat, d, tot, index):
	nl = len(mat)
	nc = len(mat[0])
	# Elemento de Maior Módulo
	maior = abs(mat[d][d])
	lmaior = d
	cmaior = d
	# Verificar Se é Pivotamento Total
	cf = d+1
	if(tot==1):
		cf = nl
	# Procurar Posição do Elemento de Maior Módulo
	for l in range(d,nl):
		for c in range(d,cf):
			if(maior<abs(mat[l][c])):
				lmaior = l
				cmaior = c
				maior = abs(mat[l][c])
	if(lmaior != d):
		if(cmaior != d):
			# Trocar Linha D pela Linha do Elemento de Maior Módulo
			for c in range(d,nc):
				mat[d][c], mat[lmaior][c] = mat[lmaior][c], mat[d][c]
			# Trocar Coluna D pela Coluna do Elemento de Maior Módulo
			for l in range(0,nl):
				mat[l][d], mat[l][cmaior] = mat[l][cmaior], mat[l][d]
			index[cmaior], index[d] = index[d], index[cmaior]
		else:
			for c in range(d,nc):
				mat[d][c], mat[lmaior][c] = mat[lmaior][c], mat[d][c]
	return mat