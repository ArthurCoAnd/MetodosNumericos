import mpmath as mm
from Ferramentas.f import f
# Retorna o Menor Verificador de Parada
def calcularE(sf,a,b,xk,pDec=16):
	mm.mp.dps = pDec
	mm.mp.trap_complex = True
	a = mm.mpf(a)
	b = mm.mpf(b)
	xk = mm.mpf(xk)
	fxk = f(xk,sf,pDec)
	erro = mm.mpf('0.0')
	if(abs(a-b)<abs(fxk)):
		erro = mm.mpf(abs(a-b))
	else:
		erro = mm.mpf(abs(fxk))
	return erro