import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
from ZeroDeFunções.dadosZDF import dados as d
# Importando Funções
from ZeroDeFunções.Funções.f import f

def bissecção(d):
	título("Bissecçâo", '=')
	k = 1
	xk = (d.a+d.b)/2
	print("%-5s%-12s%-12s%-12s%-12s%-12s%-12s%-12s"%("K","A","xk","B","e","f(a)","f(xk)","f(b)"))
	while(calcularErro(d.sf,d.a,d.b,xk)>d.e and k<=d.kmax):
		xk = (d.b+d.a)/2
		print("%-5d%-12f%-12f%-12f%-12f%-12f%-12f%-12f"%(k,d.a,xk,d.b,calcularErro(d.sf,d.a,d.b,xk),f(d.a,d.sf),f(xk,d.sf), f(d.b,d.sf)))
		if ( f(d.a,d.sf) * f(xk,d.sf) < 0 ):
			d.b = xk
		else:
			d.a = xk
		k+=1
	s="Bissecção\n%-15s\tk = %i\n%-15s\tx = %f\n%-15s\tf(x) = %f\n%-15s\te = %f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,d.sf),"Erro",calcularErro(d.sf,d.a,d.b,xk))
	print("\n"+s+"\n\n")

	return s