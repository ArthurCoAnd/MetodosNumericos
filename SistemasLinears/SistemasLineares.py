# Importar Bibliotecas
import mpmath as mm
import pandas as pd
from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.Matriz.FatorarMatriz import FatorarMatriz as fM
from Ferramentas.rmve import rmve
	# Importar Métodos
from SistemasLinears.MétodosSL.Cramer import Cramer
from SistemasLinears.MétodosSL.Gauss import Gauss
from SistemasLinears.MétodosSL.LU import LU
from SistemasLinears.MétodosSL.Cholesky import Cholesky

# Tamanho Largura das Colunas
l=30

class SL(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Sistemas Lineares", width=3*l)
		self.t_nVar = Label(self, text="Número de Variáveis (n)", width=l)
		self.t_precisão = Label(self, text="Precisão - Dígitos", width=l)
			# Botões
		self.b_gerarMatriz = Button(self, text="Criar Matriz", command=self.cGerarMatriz, fg="white", bg="black",width=l)
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvarMatriz, fg="white", bg="black")
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregarMatriz, fg="white", bg="black")
			# Botões Verificadores
		self.bv_piv_var = IntVar()
		self.bv_piv = Checkbutton(self, text="Pivotamento", variable=self.bv_piv_var, onvalue=1, offvalue=0)
		self.bv_pivT_var = IntVar()
		self.bv_pivT = Checkbutton(self, text="Total", variable=self.bv_pivT_var, onvalue=1, offvalue=0)
			# Entradas
		self.e_nVar = Entry(self, width=l)
		self.e_precisão = Entry(self, width=l)
		
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=0, columnspan=3)
		self.t_nVar.grid(row=1, column=0)
			# Botões
		self.b_gerarMatriz.grid(row=0,column=2)
		self.b_carregar.grid(row=0, column=0, sticky=W)
			# Entradas
		self.e_nVar.grid(row=1, column=1)
		
		self.jMatriz = None

	# Clique Gerar Pontos
	def cGerarMatriz(self):
		self.b_salvar.grid(row=0, column=0, sticky=E)
		nV = int(self.e_nVar.get())
		self.t_precisão.grid(row=2, column=0)
		self.e_precisão.grid(row=2, column=1)
		self.bv_piv.grid(row=1, column=2)
		self.bv_pivT.grid(row=2, column=2)
		novaJanela = Matriz(self, nV)
		if self.jMatriz is not None:
			self.jMatriz.destroy()
		self.jMatriz = novaJanela
		self.jMatriz.grid(row=3, column=0, columnspan=3)

	# Clique Salvar
	def cSalvarMatriz(self):
		self.jMatriz.Salvar()

	# Clique Carregar
	def cCarregarMatriz(self):
		arqN = filedialog.askopenfilename(initialdir="./", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		nV = int(rmve(arq.readline()))
		prec = int(rmve(arq.readline()))
		self.e_nVar.delete(0,END)
		self.e_nVar.insert(END, nV)
		self.cGerarMatriz()
		self.e_precisão.delete(0,END)
		self.e_precisão.insert(END, prec)
		for pl in range (nV):
			for pc in range(nV+1):
				self.jMatriz.matriz[pl][pc].insert(END,rmve(arq.readline()))
		arq.close()

class Matriz(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.raiz = raiz
		self.n = n
		self.prec = 0
		self.matriz = [[]]
		self.wdt = int(l*3/(n+1))
		for pl in range (0,self.n):
			for pc in range (0,(self.n+1)):
				# X
				if(pc<self.n):
					Label(self, text=("a"+str(pl+1)+" x"+str(pc+1)), width=self.wdt).grid(row=((pl+1)*2)-2, column=pc)
					self.matriz[pl].append(Entry(self, width=self.wdt))
					self.matriz[pl][pc].grid(row=(((pl+1)*2)-1), column=pc)
				# Y
				else:
					Label(self, text=("y"+str(pl+1)), width=self.wdt).grid(row=((pl+1)*2)-2, column=pc)
					self.matriz[pl].append(Entry(self, width=self.wdt))
					self.matriz[pl][pc].grid(row=(((pl+1)*2)-1), column=pc)
			self.matriz.append([])

		# ===== Definir e Cosntruir Elementos =====
			# Linha Inicial Dos Botões Dos Métodos
		self.lm = self.n*2

		self.b_Cramer = Button(self, text="Cramer", command=self.cCramer, fg="white", bg="black", width=l*3)
		self.b_Cramer.grid(row=self.lm+0, column=0, columnspan=n+1)

		self.b_Gauss = Button(self, text="Eliminação de Gauss", command=self.cGauss, fg="white", bg="black", width=l*3)
		self.b_Gauss.grid(row=self.lm+1, column=0, columnspan=n+1)

		self.b_LU = Button(self, text="Fatoração LU", command=self.cLU, fg="white", bg="black", width=l*3)
		self.b_LU.grid(row=self.lm+2, column=0, columnspan=n+1)

		self.b_Cholesky = Button(self, text="Fatoração Cholesky", command=self.cCholesky, fg="white", bg="black", width=l*3)
		self.b_Cholesky.grid(row=self.lm+3, column=0, columnspan=n+1)

		self.t_Resposta = Label(self, text="Escolha um Método Para Resolver a Matriz", width=int(l*3/2), anchor=W, justify=LEFT, font="Consolas 9")
		self.t_Resposta.grid(row=self.lm+4, column=0, columnspan=int((n+1)/2))

		self.t_Ressíduo = Label(self, text="", width=int(l*3/2), anchor=E, justify=LEFT, font="Consolas 9")
		self.t_Ressíduo.grid(row=self.lm+4, column=2, columnspan=int((n+1)/2))

		# self.jResposta = Resposta(self, self.n)
		# self.jResposta.grid(row=self.lm+1, column=0, columnspan=n)

	def lerDados(self):
		self.prec = int(self.raiz.e_precisão.get())
		mm.mp.dps = self.prec
		mtz = []
		for pl in range (0,self.n):
			mtz.append([])
			for pc in range(0,(self.n+1)):
				mtz[pl].append(mm.mpf(self.matriz[pl][pc].get()))
		return mtz

	# Função chamada pelo Clique Salvar
	def Salvar(self):
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile="Sistema Linear", filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(str(self.n))
		arq.write("\n")
		arq.write(str(self.prec))
		arq.write("\n")
		mtz = self.lerDados()
		for pl in range (self.n):
			for pc in range (self.n+1):
				arq.write(str(mtz[pl][pc]))
				arq.write("\n")
		arq.close()

	# Clique Método de Cramer
	def cCramer(self):
		mat = self.lerDados()
		resp, ress = Cramer(mat, self.prec)
		self.t_Resposta.config(text=resp)
		self.t_Ressíduo.config(text=ress)

	# Clique Método de Gauss
	def cGauss(self):
		piv = self.raiz.bv_piv_var.get()
		pivT = self.raiz.bv_pivT_var.get()
		mat = self.lerDados()
		resp, ress = Gauss(mat, self.prec, piv, pivT)
		self.t_Resposta.config(text=resp)
		self.t_Ressíduo.config(text=ress)

	# Clique Método Fatoração LU
	def cLU(self):
		mat = self.lerDados()
		resp, ress = LU(mat, self.prec)
		self.t_Resposta.config(text=resp)
		self.t_Ressíduo.config(text=ress)

	# Clique Método Fatoração Cholesky
	def cCholesky(self):
		mat = self.lerDados()
		resp, ress = Cholesky(mat, self.prec)
		self.t_Resposta.config(text=resp)
		self.t_Ressíduo.config(text=ress)

		