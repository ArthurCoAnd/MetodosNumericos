# Importar Bibliotecas
from Interpolação.Ferramentas.pol2str import pol2str
from numpy.polynomial.polynomial import Polynomial, polyadd, polymul
from numpy import zeros
from numpy import shape

def Newton(p):
	np = len(p)

	matX = []
	matY = []
	for i in range(np):
		matX.append(p[i][0])
		matY.append(p[i][1])

	coeff_vector = getNDDCoeffs(matX,matY)
	final_pol = Polynomial([0.])
	n = coeff_vector.shape[0]
	for i in range(n):
		p = Polynomial([1.])
		for j in range(i):
			p_temp = Polynomial([-matX[j],1.])
			p = polymul(p,p_temp)
		p *= coeff_vector[i]
		final_pol = polyadd(final_pol,p)
	p = final_pol[0].coef

	return pol2str(p)

def getNDDCoeffs(x, y):
	n = shape(y)[0]
	pyramid = zeros([n,n])
	pyramid[::,0] = y
	for j in range(1,n):
		for i in range(n-j):
			pyramid[i][j] = (pyramid[i+1][j-1]-pyramid[i][j-1])/(x[i+j]-x[i])
	return pyramid[0]