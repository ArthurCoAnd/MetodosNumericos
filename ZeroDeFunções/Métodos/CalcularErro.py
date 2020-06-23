from ZeroDeFunções.Funções.f import f
# Retornar o Maior Erro
def calcularErro(sf,a,b,xk):
	erro=0
	if(abs(a-b)<abs(f(xk,sf))):
		erro = abs(a-b)
	else:
		erro = abs(f(xk,sf))
	return erro