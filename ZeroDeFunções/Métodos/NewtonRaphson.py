import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
# Importando Funções
from ZeroDeFunções.Funções.f import f

def newtonRaphson(a,e,kmax,sf,sdf):
	título("Newton-Raphson", '=')
	xk=a
	xkAnt=a*a
	k=1
	print("%-5s%-12s%-12s%-12s%-12s%-12s"%("K","xk","f(xk)","f'(xk-1)","xk+1","e"))
	while( (calcularErro(sf,xk,xkAnt,xk)>e) and k<=kmax ):
		xkAnt=xk
		xk = xkAnt - (f(xkAnt,sf)/f(xkAnt,sdf))
		# Printa-se xkAnt como xk
		print("%-5d%-12f%-12f%-12f%-12f%-12f"%(k,xkAnt,f(xkAnt,sf),f(xkAnt,sdf),xk,calcularErro(sf,xk,xkAnt,xk)))
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),calcularErro(sf,xk,xkAnt,xk)))