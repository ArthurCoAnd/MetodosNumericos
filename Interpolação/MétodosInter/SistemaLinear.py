# Importar Bibliotecas
import mpmath as mm
#Importar Ferramentas
from Ferramentas.título import título

def SL(pts, prec):
	título("Sistema Linear", "=")
	# Definir Precisão
	mm.mp.dps = prec
	nv = len(pts[0])
	pol = []

	# Criar Matriz Polinômio
	matA = []
	matY = []
	for i in range(len(pts[0])):
		matA.append([])
		for g in range(nv):
			matA[i].append(pts[0][i]**g)
		matY.append(pts[1][i])

	# Resolver Matriz
	matA = mm.matrix(matA)
	print("Matriz A")
	print(str(matA))
	matY = mm.matrix(matY)
	print("\nMatriz Y")
	print(str(matY))
	matInvA = matA**-1
	print("\nMatriz Inversa A")
	print(str(matInvA))
	matX = matInvA * matY
	print("\nMatriz X")
	print(str(matX))

	# Transformar Resposta em String Polinômio
	sPol = pol2str(matX)
	print("\nPolinômio: ",sPol)

	return sPol

def pol2str(pol):
	s = ""
	for i in range(len(pol)):
		s = s + "+("+ str(pol[i]) + "x^" + str(i) + ")"
	return s