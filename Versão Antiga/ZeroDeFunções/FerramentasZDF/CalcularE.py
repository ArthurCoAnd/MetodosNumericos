import mpmath as mm
from Ferramentas.f import f
# Retorna o Menor Verificador de Parada
def calcularE(sf,a,b,xk,pDec=16,k=1):
	mm.mp.dps = pDec
	mm.mp.trap_complex = True
	
	erro = mm.mpf('0.0')
	fxk = mm.mpf(abs(f(xk,sf,pDec)))
	if(k!=0):
		difab = mm.mpf(abs(a-b))
		if(difab<fxk):
			erro = difab
		else:
			erro = fxk
	else:
		erro = fxk

	return erro