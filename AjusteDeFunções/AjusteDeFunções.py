from tkinter import *
# Importar Ferramentas
	#from ZeroDeFunções.dadosZDF import dados

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=15

class AdF:
	def __init__(self, raiz):
		janela = Frame(raiz)
		janela.grid(row=0, column=0)

		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(janela, text="Ajuste de Funções", width=3*l)
		self.t_nPontos = Label(janela, text="Número de Pontos (n)", width=l)

			# Botôes
		self.b_criarPontos = Button(janela, text="Criar Pontos", command=self.bNada, fg="white", bg="black",width=l)
		self.b_funcLinear = Button(janela, text="Função Linear", command=self.bNada, fg="white", bg="black", width=3*l)

			# Entradas
		self.e_nPontos = Entry(janela, width=l)

		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0 ,column=0, columnspan=3)
		self.t_nPontos.grid(row=1,column=0)

			# Botôes
		self.b_criarPontos.grid(row=1,column=2)
		self.b_funcLinear.grid(row=2,column=0, columnspan=3)

			# Entradas
		self.e_nPontos.grid(row=1, column=1)


	def bNada(self):
		print("Botão Apertado")