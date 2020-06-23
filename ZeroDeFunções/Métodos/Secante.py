import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
from ZeroDeFunções.dadosZDF import dados as d
# Importando Funções
from ZeroDeFunções.Funções.f import f

def secante(d):
	título("Secante", '=')
	xk=d.a
	xkAnt=d.b
	k = 1
	print("%-5s%-12s%-12s%-12s"%("K","xk","f(xk)","e"))
	while( (calcularErro(d.sf,xk,xkAnt,xk)>d.e) and (k<=d.kmax)):
		aux = xk
		xk = (xkAnt*f(xk,d.sf)-xk*f(xkAnt,d.sf))/(f(xk,d.sf)-f(xkAnt,d.sf))
		xkAnt = aux
		print("%-5d%-12f%-12f%-12f"%(k,xk,f(xk,d.sf),calcularErro(d.sf,xk,xkAnt,xk)))
		k+=1
	s="Secante x= %f \t f(x)=%f \t e= %f"%(xk,f(xk,d.sf),calcularErro(d.sf,xk,xkAnt,xk))
	print("\n"+s+"\n\n")

	return s