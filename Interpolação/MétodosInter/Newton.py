# Importar Bibliotecas
import mpmath as mm
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
#Importar Ferramentas
from Ferramentas.título import título

def Newton(pts, prec):
	título("Newton", "=")
	# Definir Precisão
	mm.mp.dps = prec

	nv = len(pts[0])
	matX = pts[0]
	matY = [pts[1]]
	for i in range(1,nv):
		matY.append([])
		for j in range (nv-i):
			matY[i].append((matY[i-1][j+1]-matY[i-1][j])/(matX[j+i]-matX[j]))
	
	print("\nTabela\n\n",mm.matrix(matY))

	# matP = [matY[1][0]]
	# for i in range(nv-1):
	# 	mult = 1
	# 	for n in range(i):
	# 		mult *= -matX[n]
	# 	matP.append(mult)

	matX = pts[0]
	matY = pts[1]
	matP = mm.matrix(list(reversed(Polynomial(lagrange(matX,matY)).coef)))

	# Transformar Resposta em String Polinômio
	sPol = pol2str(matP)
	print("\nPolinômio: ",sPol)

	return sPol

def F(f0,f1,x0,x1):
	return (f1-f0)/(x1-x0)

def pol2str(pol):
	s = ""
	for i in range(len(pol)):
		s = s + "+("+ str(pol[i]) + "x^" + str(i) + ")"
	return s