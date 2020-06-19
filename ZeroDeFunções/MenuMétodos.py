import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
from Ferramentas.pedirFunção import pedirFunção

import ZeroDeFunções.MenuDados as MD

# Importando Métodos
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

def MenuMétodos(sf,sdf,spf,a,b,e,kmax):
	escolha = -1
	while (escolha != 0):
		printMenuMétodos()
		escolha = pedirInt(s="Escolha")
		# Bissecção
		if (escolha==1):
			bissecção(a,b,e,kmax,sf)
		# Posição Falsa
		elif (escolha==2):
			posiçãoFalsa(a,b,e,kmax,sf)
		# Ponto Fixo
		elif (escolha==3):
			pontoFixo(a,b,e,kmax,sf,spf)
		# Newton-Raphson
		elif (escolha==4):
			newtonRaphson(a,e,kmax,sf,sdf)
		# Secante
		elif (escolha==5):
			secante(a,b,e,kmax,sf)
		elif (escolha==0):
			escolha=0
		else:
			título("ERRO - Escolha Inválida", '*')

def printMenuMétodos():
	título("Menu Métodos Zero De Funções", '=')
	print("1 - Bissecção")
	print("2 - Posição Falsa")
	print("3 - Ponto Fixo")
	print("4 - Newton-Raphson")
	print("5 - Secante")
	print("0 - Voltar")