def GaussJacobi(mat, vet, e):
	matX = vet
	k = 0
	while(True):
		nmatX = CalcularMatX(mat, matX)
		eMat = abs(MaiorModMat(nmatX, matX))
		matX = nmatX
		k += 1
		if eMat<e or k>999:
			break
	return matX

def CalcularMatX(mat, matx):
	nv = len(mat)
	mx = []
	for l in range(nv):
		x = mat[l][nv]
		for c in range(nv):
			if(l != c):
				x = x - (mat[l][c]*matx[c])
		x = x/mat[l][l]
		mx.append(x)
	return mx

def MaiorModMat(mat, matM):
	nv = len(mat)
	maior = abs(mat[0]-matM[0])
	for i in range(1,nv):
		if(abs(mat[i]-matM[i])>maior):
			maior = abs(mat[i]-matM[i])
	return maior