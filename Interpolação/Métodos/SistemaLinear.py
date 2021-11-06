# Importar Bibliotecas
from numpy import matrix, zeros
# Importar Ferramentas
from Ferramentas.FatorarMatriz import FatorarMatriz as FM
from Interpolação.Ferramentas.pol2str import pol2str

def SistemaLinear(p):
	pap = "Sistema Linear\n\n"
	nv = len(p)
	matA = []
	matY = []
	for i in range(nv):
		matA.append([])
		for g in range(nv):
			matA[i].append(p[i][0]**g)
		matY.append(p[i][1])
	mat = zeros((nv,nv+1))
	for l in range(nv):
		for c in range(nv):
			mat[l][c] = matA[l][c]
		mat[l][nv] = matY[l]
	pap += f"\n\nMatriz:\n{str(matrix(mat))}"
	matFat, index = FM(mat)
	pap += f"\n\nMatriz Fatorada:\n{str(matrix(mat))}"
	matX = zeros(nv)
	for d in range(nv-1,-1,-1):
		sub = 0
		for c in range(d+1,nv):
			sub = sub+(matFat[d][c]*matX[c])
		matX[d] = (matFat[d][nv]-sub)/matFat[d][d]
	pap += f"\n\nMatriz X:\n{str(matrix(matX))}"
	strPol = pol2str(matX)
	pap += f"\n\nFunção = {strPol}"
	print(pap)
	return strPol, pap