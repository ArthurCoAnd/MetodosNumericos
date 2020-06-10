import math
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f

def bissecção(a,b,e,kmax,sf):
	título("Bissecçâo", '=')
	k = 1
	# xk = metade entre as pontas do intervalo
	xk = (b+a)/2
	print("%-5s%-12s%-12s%-12s%-12s%-12s%-12s%-12s"%("K","A","xk","B","e","f(a)","f(xk)","f(b)"))
	while( (b-a)>e and k<=kmax):
		xk = (b+a)/2
		print("%-5d%-12f%-12f%-12f%-12f%-12f%-12f%-12f"%(k,a,xk,b,(b-a),f(a,sf),f(xk,sf), f(b,sf)))
		if ( f(a,sf) * f(xk,sf) < 0 ):
			b = xk
		else:
			a = xk
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),(b-a)))