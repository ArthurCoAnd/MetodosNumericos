# Importar Bibliotecas
import mpmath as mm
#Importar Ferramentas
from Ferramentas.título import título

def Lagrange(pts, grau, prec):
	título("Lagrange", "=")
	# Definir Precisão
	mm.mp.dps = prec
	
	pol = []

	# Criar Matriz Polinômio
	matA = []
	matY = []
	for i in range(len(pts[0])):
		matA.append([])
		for g in range(grau+1):
			matA[i].append(pts[0][i]**g)
		matY.append(pts[1][i])

	# Calcular L's
	matL = []
	Li = mm.matrix([])
	for i in range(len(pts[0])):
		# matL.append([])
		div = 1
		Li.append([1])
		for g in range(grau+1):
			Liaux = Li.copy()
			if(g!=i):
				div = div * (pts[0][i]-pts[0][g])
				Li.insert(0,1)
				Liaux*(-pts[0][g])
				Li=[i] = Li[i] + Liaux
		matL.append(Li)

	# Transformar Resposta em String Polinômio
	sPol = pol2str(matL)
	print("Polinômio: ",sPol)

	return sPol

def pol2str(pol):
	s = ""
	for i in range(len(pol)):
		s = s + "+("+ str(pol[i]) + "x^" + str(i) + ")"
	return s