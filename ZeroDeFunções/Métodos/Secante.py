import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
# Importando Funções
from ZeroDeFunções.Funções.f import f

def secante(a,b,e,kmax,sf):
	título("Secante", '=')
	xk=a
	xkAnt=b
	k = 1
	print("%-5s%-12s%-12s%-12s"%("K","xk","f(xk)","e"))
	while( (calcularErro(sf,xk,xkAnt,xk)>e) and (e<=kmax)):
		aux = xk
		xk = (xkAnt*f(xk,sf)-xk*f(xkAnt,sf))/(f(xk,sf)-f(xkAnt,sf))
		xkAnt = aux
		print("%-5d%-12f%-12f%-12f"%(k,xk,f(xk,sf),calcularErro(sf,xk,xkAnt,xk)))
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),calcularErro(sf,xk,xkAnt,xk)))