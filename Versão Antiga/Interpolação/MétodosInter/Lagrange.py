# Importar Bibliotecas
import mpmath as mm
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
#Importar Ferramentas
from Ferramentas.título import título

def Lagrange(pts, prec):
	título("Lagrange", "=")
	# Definir Precisão
	mm.mp.dps = prec
	nv = len(pts[0])
	matX = pts[0]
	matY = pts[1]
	matP = mm.matrix(list(reversed(Polynomial(lagrange(matX,matY)).coef)))
	
	# Transformar Resposta em String Polinômio
	sPol = pol2str(matP)
	print("Polinômio: ",sPol)

	return sPol

def pol2str(pol):
	s = ""
	for i in range(len(pol)):
		if pol[i] > 0:
			s = s + " +" + str(pol[i]) + "*(x^" + str(i) + ")"
		else:
			s = s + " " + str(pol[i]) + "*(x^" + str(i) + ")"
	return s