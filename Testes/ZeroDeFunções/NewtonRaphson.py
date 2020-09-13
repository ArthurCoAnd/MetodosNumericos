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
	s = ""
	s += "%-5s%-12s%-12s%-12s%-12s%-12s%-12s\n"%("K","xk-1","f(xk-1)","f'(xk-1)","xk","f(xk)","e")
	while( (calcularErro(d.sf,xk,xkAnt,xk)>d.e) and (k<=d.kmax) ):
		xkAnt=xk
		xk = xkAnt - (f(xkAnt,d.sf)/f(xkAnt,d.sdf))
		# Printa-se xkAnt como xk
		s += "%-5d%-12f%-12f%-12f%-12f%-12f%-12f\n"%(k,xkAnt,f(xkAnt,d.sf),f(xkAnt,d.sdf),xk,f(xk,d.sf),calcularErro(d.sf,xk,xkAnt,xk))
		k+=1

	s += "\nNewton-Raphson\n%-15s\tk\t=\t%i\n%-15s\tx\t=\t%f\n%-15s\tf(x)\t=\t%f\n%-15s\te\t=\t%f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,d.sf),"e de parada",calcularErro(d.sf,xk,xkAnt,xk))
	print("\n"+s+"\n\n")

	return s