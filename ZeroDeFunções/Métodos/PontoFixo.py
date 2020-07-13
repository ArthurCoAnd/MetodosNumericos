import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
from ZeroDeFunções.dadosZDF import dados as d
# Importando Funções
from ZeroDeFunções.Funções.f import f

def pontoFixo(d):
	título("Ponto Fixo", '=')
	xk=d.a
	xkAnt=d.b
	k = 1
	print("%-5s%-10s%-10s%-10s"%("K","xk","e","f(xk)"))
	while( (calcularErro(d.sf,xk,xkAnt,xk)>d.e) and (k<=d.kmax) ):
		xkAnt=xk
		xk = f(xkAnt,d.spf)
		print("%-5d%-10f%-10f%-10f"%(k,xk,calcularErro(d.sf,xk,xkAnt,xk),f(xk,d.sf)))
		k+=1

	s="Ponto Fixo\n%-15s\tk\t=\t%i\n%-15s\tx\t=\t%f\n%-15s\tf(x)\t=\t%f\n%-15s\te\t=\t%f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,d.sf),"Erro",calcularErro(d.sf,xk,xkAnt,xk))
	print("\n"+s+"\n\n")

	return s