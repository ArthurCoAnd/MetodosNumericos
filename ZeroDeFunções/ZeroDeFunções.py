import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
from Ferramentas.pedirFunção import pedirFunção
# Importar Ferramentas Zero de Funções
from ZeroDeFunções.MenuMétodos import printMenuMétodos
import ZeroDeFunções.MenuDados as MD
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
	sddf = "(18*x)-8"

	escolha = -1
	while (escolha != 0):
		printMenu()
		escolha = pedirInt(chave=False,s="Escolha")

		# MENU DE DADOS
		if (escolha==1):
			escolhaM = -1
			while (escolhaM != 0):
				MD.printMenuDados(sf,sdf,sddf,a,b,e,kmax)
				escolhaM = pedirInt(chave=False,s="Escolha")
				# Definir Todos os Dados
				if (escolhaM==1):
					título("Definir Funções", '=')
					escolhaMM = -1
					while((escolhaMM!=0) and (escolhaMM!=1)):
						MD.printFunções(sf,sdf,sddf)
						print("Deseja Alterar as Funções Atuais?")
						print("1- Sim | 0- Não")
						escolhaMM = pedirInt(chave=False,s="Escolha")
						if(escolhaMM==1):
							sf=pedirFunção()
							sdf=pedirFunção(s="Função Derivada Primeira")
							sddf=pedirFunção(s="Função Derivada Segunda")
						elif(escolhaMM==0):
							escolhaMM=0
						else:
							título("ERRO - Escolha Inválida", '*')
					título("Definir Intervalos", '=')
					a=pedirFloat(chave=False,s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,chave=False,s="Posição FINAL")
					e=pedirFloat(s="Erro")
					kmax=pedirIntPos(s="Máximo de Interações")
				# Definir Função
				elif (escolhaM==2):
					sf=pedirFunção()
				# Definir Função Derivada Primeira
				elif (escolhaM==3):
					sdf=pedirFunção(s="Função Derivada Primeira")
				# Definir Função Derivada Segunda
				elif (escolhaM==4):
					sddf=pedirFunção(s="Função Derivada Segunda")
				# Definir Intervalo
				elif (escolhaM==5):
					título("Definir Intervalo", '=')
					a=pedirFloat(chave=False,s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,chave=False,s="Posição FINAL")
				# Definir Erro
				elif (escolhaM==6):
					e=pedirFloatMaiorQue(0.0,s="Erro")
				# Definir Máximo de Interações
				elif (escolhaM==7):
					kmax=pedirIntPos(s="Máximo de Interações")
				# Procurar Intervalos Válidos
				elif (escolhaM==8):
					intervalosVálidos(sf)
				# Verificar Intervalo Atual
				elif (escolhaM==9):
					print("Verifar Intervalo Atual")
				elif (escolhaM==0):
					escolhaM=0
				else:
					título("ERRO - Escolha Inválida", '*')

		# MENU DE MÉTODOS
		elif (escolha==2):
			escolhaM = -1
			while (escolhaM != 0):
				printMenuMétodos()
				escolhaM = pedirInt(chave=False,s="Escolha")
				# Bissecção
				if (escolhaM==1):
					bissecção(a,b,e,kmax,sf)
				# Posição Falsa
				elif (escolhaM==2):
					posiçãoFalsa(a,b,e,kmax,sf)
				# Ponto Fixo
				elif (escolhaM==3):
					pontoFixo(a,b,e,kmax,sf)
				# Newton-Raphson
				elif (escolhaM==4):
					newtonRaphson(a,e,kmax,sf,sdf)
				# Secante
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