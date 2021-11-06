# Importar Bibliotecas
from numpy import matrix
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
# Importar Ferramentas
from Interpolação.Ferramentas.pol2str import pol2str

def Lagrange(p):
	pap = "Lagrange\n\n"
	np = len(p)
	matX = []
	matY = []
	for i in range(np):
		matX.append(p[i][0])
		matY.append(p[i][1])
	poly = lagrange(matX, matY)
	poly = Polynomial(poly).coef
	poly = poly[::-1]
	strPol = pol2str(poly)
	pap += f"\n\nFunção = {strPol}"
	print(pap)
	return strPol, pap
