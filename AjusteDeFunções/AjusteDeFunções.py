from tkinter import *
# Importar Ferramentas
#import numpy as np

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=15

class AdF(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Ajuste de Funções", width=3*l)
		self.t_nPontos = Label(self, text="Número de Pontos (n)", width=l)
			# Botôes
		self.b_criarPontos = Button(self, text="Criar Pontos", command=self.cGerarPontos, fg="white", bg="black",width=l)
		self.b_funcLinear = Button(self, text="Função Linear", command=self.bNada, fg="white", bg="black", width=3*l)
			# Entradas
		self.e_nPontos = Entry(self, width=l)
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0 ,column=0, columnspan=3)
		self.t_nPontos.grid(row=1,column=0)
			# Botôes
		self.b_criarPontos.grid(row=1,column=2)
		self.b_funcLinear.grid(row=2,column=0, columnspan=3)
			# Entradas
		self.e_nPontos.grid(row=1, column=1)

		self.jPontos = None

	def cGerarPontos(self):
		nP = int(self.e_nPontos.get())
		novaJanela = Pontos(self, nP)
		if self.jPontos is not None:
			self.jPontos.destroy()
		self.jPontos = novaJanela
		self.jPontos.grid(row=lr, column=0, columnspan=3)
		

	def bNada(self):
		print("Botão Apertado")

class Pontos(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		pontos = [[],[]]
		for p in range (0,n):
			# X
			Label(self, text=("x"+str(p))).grid(row=0, column=p)
			pontos[0].append(Entry(self))
			pontos[0][p].grid(row=1, column=p)
			# Y
			Label(self, text=("y"+str(p))).grid(row=2, column=p)
			pontos[1].append(Entry(self))
			pontos[1][p].grid(row=3, column=p)
