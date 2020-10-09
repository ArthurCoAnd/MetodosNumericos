# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.Matriz.FatorarMatriz import FatorarMatriz as fM

def Gauss(mat, prec):
	título("Eliminação de Gauss", "=")
	# Precisão de Dígitos
	mm.mp.dps = prec
	
	# Número de Variáveis
	nV = len(mat)

	# Matriz
	mat = mm.matrix(mat)
	print("Matriz")
	print(str(mat))

	# Matriz Fatorada
	matFat = fM(mat, prec)
	print("Matriz Fatorada")
	print(str(matFat))

	# Matriz X
	matX = mm.zeros(nV,1)
	for d in range (nV-1,-1,-1):
		sub = mm.mpf('0.0')
		for c in range (d-1,-1,-1):
			sub = mm.mpf(sub+(matFat[d,c]*matX[c]))
		matX[d] = mm.mpf((matFat[d,d+1]-sub)/matFat[d,d])
	print("Matriz X")
	print(str(matX))

	resp = "Eliminação de Gauss:"
	for l in range (nV):
		resp += "\nx("+str(l+1)+") = "+str(matX[l])

	return resp
