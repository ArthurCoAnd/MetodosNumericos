import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
from ZeroDeFunções.dadosZDF import dados as d
# Importando Funções
from ZeroDeFunções.Funções.f import f

def newtonRaphson(d):
	título("Newton-Raphson", '=')
	xk=d.a
	xkAnt=999
	k=1
	print("%-5s%-12s%-12s%-12s%-12s%-12s"%("K","xk","f(xk)","f'(xk-1)","xk+1","e"))
	while( (calcularErro(d.sf,xk,xkAnt,xk)>d.e) and k<=d.kmax ):
		xkAnt=xk
		xk = xkAnt - (f(xkAnt,d.sf)/f(xkAnt,d.sdf))
		# Printa-se xkAnt como xk
		print("%-5d%-12f%-12f%-12f%-12f%-12f"%(k,xkAnt,f(xkAnt,d.sf),f(xkAnt,d.sdf),xk,calcularErro(d.sf,xk,xkAnt,xk)))
		k+=1

	s="Newton-Raphson\n%-15s\tk = %i\n%-15s\tx = %f\n%-15s\tf(x) = %f\n%-15s\te = %f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,d.sf),"Erro",calcularErro(d.sf,xk,xkAnt,xk))
	print("\n"+s+"\n\n")

	return s