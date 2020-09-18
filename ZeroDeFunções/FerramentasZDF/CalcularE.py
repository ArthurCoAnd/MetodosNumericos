from Ferramentas.f import f
# Retorna o Menor Verificador de Parada
def calcularE(sf,a,b,xk):
	erro=0
	if(abs(a-b)<abs(f(xk,sf))):
		erro = abs(a-b)
	else:
		erro = abs(f(xk,sf))
	return erro