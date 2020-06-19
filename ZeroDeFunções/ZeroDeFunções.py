import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
from Ferramentas.pedirFunção import pedirFunção
# Importar Ferramentas Zero de Funções
from ZeroDeFunções.MenuMétodos import MenuMétodos
import ZeroDeFunções.MenuDados as MD
# Importando Funções
from ZeroDeFunções.Funções.f import f
from ZeroDeFunções.Funções.intervalosVálidos import intervalosVálidos
from ZeroDeFunções.Funções.gerarGráfico import gerarGráfico as gG


def printMenu():
	título("Menu Zero De Funções", '=')
	print("1 - Gerenciamento de Dados")
	print("2 - Executar Métodos")
	print("0 - Voltar")

def menu():
	# a - Valor Intervalo Inicial
	a=0
	# b - Valor Intervalo Final
	b=1
	# e - Valor Erro
	e=0.001
	# kmax - Valor Máximo de Interações
	kmax=10
	# sf - String da Função
	sf = "(3*x**3)-(4*x**2)-(10*x)+10"
	# sdf - String da Derivada Primeira da Função
	sdf = "(9*x**2)-(8*x)-10"
	# spf
	spf = "((3*x**3)-(4*x**2)+10)/10"

	escolha = -1
	while (escolha != 0):
		printMenu()
		escolha = pedirInt(s="Escolha")
		# MENU DE DADOS
		if (escolha==1):
			escolhaM = -1
			while (escolhaM != 0):
				MD.printMenuDados(sf,sdf,spf,a,b,e,kmax)
				escolhaM = pedirInt(s="Escolha")
				# Definir Todos os Dados
				if (escolhaM==1):
					título("Definir Funções", '=')
					escolhaMM = -1
					while((escolhaMM!=0) and (escolhaMM!=1)):
						MD.printFunções(sf,sdf,spf)
						print("Deseja Alterar as Funções Atuais?")
						print("1- Sim | 0- Não")
						escolhaMM = pedirInt(s="Escolha")
						if(escolhaMM==1):
							sf=pedirFunção(chave=True)
							sdf=pedirFunção(chave=True, s="Função Derivada Primeira")
						elif(escolhaMM==0):
							escolhaMM=0
						else:
							título("ERRO - Escolha Inválida", '*')
					título("Definir Intervalos", '=')
					a=pedirFloat(s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,s="Posição FINAL")
					e=pedirFloat(chave=True, s="Erro")
					kmax=pedirIntPos(chave=True, s="Máximo de Interações")
				# Definir Função
				elif (escolhaM==2):
					sf=pedirFunção()
				# Definir Função Derivada Primeira
				elif (escolhaM==3):
					sdf=pedirFunção(chave=True, s="Função Derivada Primeira")
				# Definir Função do Ponto Fixo
				elif (escolhaM==4):
					spf=pedirFunção(chave=True, s="Função do Ponto Fixo")
				# Definir Intervalo
				elif (escolhaM==5):
					título("Definir Intervalo", '=')
					a=pedirFloat(s="Posição INICIAL")
					b=pedirFloatMaiorQue(a,s="Posição FINAL")
				# Definir Erro
				elif (escolhaM==6):
					e=pedirFloatMaiorQue(0.0, chave=True, s="Erro")
				# Definir Máximo de Interações
				elif (escolhaM==7):
					kmax=pedirIntPos(s="Máximo de Interações")
				# Procurar Intervalos Válidos
				elif (escolhaM==8):
					intervalosVálidos(sf,sdf)
				# Verificar Intervalo Atual
				elif (escolhaM==9):
					título("Verifar Intervalo Atual", '=')
				# Gerar Gráfico
				elif (escolhaM==10):
					gG(sf,sdf)
				elif (escolhaM==0):
					escolhaM=0
				else:
					título("ERRO - Escolha Inválida", '*')
		# MENU DE MÉTODOS
		elif (escolha==2):
			MenuMétodos(sf,sdf,spf,a,b,e,kmax)
		elif (escolha==0):
			escolha==0
		else:
			título("ERRO - Escolha Inválida", '*')