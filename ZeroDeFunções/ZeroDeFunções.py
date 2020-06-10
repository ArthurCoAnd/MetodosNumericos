import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
# Importando Funções
from ZeroDeFunções.Funções.f import f
from ZeroDeFunções.Funções.df import df
from ZeroDeFunções.Funções.ddf import ddf
from ZeroDeFunções.Funções.intervalosVálidos import intervalosVálidos
# Importando Métodos
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

def printMenu():
	título("Menu Zero De Funções", '=')
	print("1 - Definir Dados")
	print("2 - Executar Métodos")
	print("0 - Fechar Programa")

def printMenuDados(sf,sdf,sddf,a,b,e,kmax):
	título("Menu Gerenciamento de Dados Zero De Funções", '=')
	printDadosAtuais(sf,sdf,sddf,a,b,e,kmax)
	print("1 - Definir Todos os Dados")
	print("2 - Definir Intervalo")
	print("3 - Definir Erro")
	print("4 - Definir Máximo de Interações")
	print("5 - Intervalos Válidos")
	print("0 - Voltar")

def printDadosAtuais(sf,sdf,sddf,a,b,e,kmax):
	print("Dados Atuais:")
	print("%-20s - %s"%("f(x)",sf))
	print("%-20s - %s"%("df(x)",sdf))
	print("%-20s - %s"%("ddf(x)",sddf))
	print("%-20s - [%f]:[%f]"%("Intervalo Atual",a,b))
	print("%-20s - %f"%("Erro Atual",e,))
	print("%-20s - %i"%("Máximo de Interações",kmax))
	print("")

def printMenuMétodos():
	título("Menu Métodos Zero De Funções", '=')
	print("1 - Bissecção")
	print("2 - Posição Falsa")
	print("3 - Ponto Fixo")
	print("4 - Newton-Raphson")
	print("5 - Secante")
	print("0 - Voltar")

def menu():
	# a - Valor Intervalo Inicial
	a=-2
	# b - Valor Intervalo Final
	b=0
	# e - Valor Erro
	e=0.001
	# kmax - Valor Máximo de Interações
	kmax=10
	# sf - String da Função
	sf = "(3*x**3)-(4*x**2)-(10*x)+10"
	# sdf - String da Derivada Primeira da Função
	sdf = "(9*x**2)-(8*x)-10"
	# sddf - Strind da Derivada Segunda da Função
	sddf = ""

	escolha = -1
	while (escolha != 0):
		printMenu()
		escolha = int(input("Escolha : "))

		# MENU DE DADOS
		if (escolha==1):
			escolhaM = -1
			while (escolhaM != 0):
				printMenuDados(sf,sdf,sddf,a,b,e,kmax)
				escolhaM = int(input("Escolha : "))
				if (escolhaM==1):
					título("Definir Intervalos", '=')
					a=pedirFloat(chave=False,s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,chave=False,s="Posição FINAL")
					e=pedirFloat(s="Erro")
					kmax=pedirIntPos(s="Máximo de Interações")
				elif (escolhaM==2):
					título("Definir Intervalos", '=')
					a=pedirFloat(chave=False,s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,chave=False,s="Posição FINAL")
				elif (escolhaM==3):
					e=pedirFloatMaiorQue(0.0,s="Erro")
				elif (escolhaM==4):
					kmax=pedirIntPos(s="Máximo de Interações")
				elif (escolhaM==5):
					intervalosVálidos(sf)
				elif (escolhaM==0):
					escolhaM=0
				else:
					título("ERRO - Escolha Inválida", '*')

		# MENU DE MÉTODOS
		elif (escolha==2):
			escolhaM = -1
			while (escolhaM != 0):
				printMenuMétodos()
				escolhaM = int(input("Escolha : "))
				if (escolhaM==1):
					bissecção(a,b,e,kmax,sf)
				elif (escolhaM==2):
					posiçãoFalsa(a,b,e,kmax,sf)
				elif (escolhaM==3):
					pontoFixo(a,b,e,kmax,sf)
				elif (escolhaM==4):
					newtonRaphson(a,e,kmax,sf,sdf)
				elif (escolhaM==5):
					secante(a,b,e,kmax,sf)
				elif (escolhaM==0):
					escolhaM=0
				else:
					título("ERRO - Escolha Inválida", '*')
		
		elif (escolha==0):
			título("Obrigado Por usar a Calculadora de Raízes do ArthurCoAnd", '=')
		else:
			título("ERRO - Escolha Inválida", '*')
