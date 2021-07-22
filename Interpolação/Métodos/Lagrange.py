# Importar Bibliotecas
from Interpolação.Ferramentas.pol2str import pol2str

from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

def Lagrange(p):
	np = len(p)
	matX = []
	matY = []
	for i in range(np):
		matX.append(p[i][0])
		matY.append(p[i][1])
	poly = lagrange(matX, matY)
	poly = Polynomial(poly).coef
	poly = poly[::-1]
	return pol2str(poly)
