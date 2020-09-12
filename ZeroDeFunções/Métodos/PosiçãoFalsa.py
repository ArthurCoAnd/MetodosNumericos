import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
from ZeroDeFunções.dadosZDF import dados as d
# Importando Funções
from ZeroDeFunções.Funções.f import f

def posiçãoFalsa(d):
	título("Posição Falsa", '=')
	k = 1
	xkAnt = 0
	xk = (d.a*abs(f(d.b,d.sf)) + d.b*abs(f(d.a,d.sf))) / (abs(f(d.a,d.sf)) + abs(f(d.b,d.sf)))
	s = ""
	s += "%-5s%-12s%-12s%-12s%-12s%-12s%-12s%-12s\n"%("K","A","xk","B","e","f(a)","f(xk)","f(b)")
	while( (calcularErro(d.sf,d.a,d.b,xk)>d.e) and (k<=d.kmax) ):
		xkAnt = xk
		xk = (d.a*abs(f(d.b,d.sf)) + d.b*abs(f(d.a,d.sf))) / (abs(f(d.a,d.sf)) + abs(f(d.b,d.sf)))
		s += "%-5d%-12f%-12f%-12f%-12f%-12f%-12f%-12f\n"%(k,d.a,xk,d.b,calcularErro(d.sf,d.a,d.b,xk),f(d.a,d.sf),f(xk,d.sf),f(d.b,d.sf))
		if ( f(d.a,d.sf) * f(xk,d.sf) < 0 ):
			d.b = xk
		else:
			d.a = xk
		k+=1

	s += "\nPosição Falsa\n%-15s\tk\t=\t%i\n%-15s\tx\t=\t%f\n%-15s\tf(x)\t=\t%f\n%-15s\te\t=\t%f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,d.sf),"e de parada",calcularErro(d.sf,d.a,d.b,xk))
	print("\n"+s+"\n\n")

	return s