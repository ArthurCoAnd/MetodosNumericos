# Importar Bibliotecas
import mpmath as mm
import pandas as pd
from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tsf
from Ferramentas.rmve import rmve
from Ferramentas.título import título
from Interpolação.FerramentasInter.secanteInter import secanteInter
from Interpolação.FerramentasInter.gerarGráficoInter import gerarGráfico as gG

# Importar Métodos
from Interpolação.MétodosInter.SistemaLinear import SL
from Interpolação.MétodosInter.Lagrange import Lagrange
from Interpolação.MétodosInter.Newton import Newton

# Tamanho Largura das Colunas
l=25

class Inter(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Interpolação", width=4*l)
		self.t_nPontos = Label(self, text="Número de Pontos (n)", width=l)
		self.t_precisão = Label(self, text="Precisão - Dígitos", width=l)
			# Botões
		self.b_criarPontos = Button(self, text="Criar Pontos", command=self.cGerarPontos, fg="white", bg="black",width=l)
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvarPontos, fg="white", bg="black")
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregarPontos, fg="white", bg="black")
			# Entradas
		self.e_nPontos = Entry(self, width=l)
		self.e_precisão = Entry(self, width=l)
		
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=0, columnspan=4)
		self.t_nPontos.grid(row=1, column=0)
			# Botões
		self.b_criarPontos.grid(row=1, column=2, columnspan=2)
		self.b_carregar.grid(row=0, column=0)
			# Entradas
		self.e_nPontos.grid(row=1, column=1)
		
		self.jPontos = None

	# Clique Gerar Pontos
	def cGerarPontos(self):
		self.b_salvar.grid(row=0, column=3)
		nP = int(self.e_nPontos.get())
		self.t_precisão.grid(row=2, column=0)
		self.e_precisão.grid(row=2, column=1)
		novaJanela = Pontos(self, nP)
		if self.jPontos is not None:
			self.jPontos.destroy()
		self.jPontos = novaJanela
		self.jPontos.grid(row=3, column=0, columnspan=4)

	# Clique Salvar
	def cSalvarPontos(self):
		self.jPontos.Salvar()

	# Clique Carregar
	def cCarregarPontos(self):
		arqN = filedialog.askopenfilename(initialdir="./", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		np = int(rmve(arq.readline()))
		prec = int(rmve(arq.readline()))
		self.e_nPontos.delete(0,END)
		self.e_nPontos.insert(END, np)
		self.e_precisão.delete(0,END)
		self.e_precisão.insert(END, prec)
		self.cGerarPontos()
		for p in range (np):
			self.jPontos.pontos[0][p].insert(END,rmve(arq.readline()))
			self.jPontos.pontos[1][p].insert(END,rmve(arq.readline()))
		arq.close()

class Pontos(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.raiz = raiz
		self.n = n
		self.prec = 0
		self.wdt = int(l*4/n)
		self.pontos = [[],[]]
		for p in range (0,self.n):
			# X
			Label(self, text=("x"+str(p)), width=self.wdt).grid(row=0, column=p)
			self.pontos[0].append(Entry(self, width=self.wdt))
			self.pontos[0][p].grid(row=1, column=p)
			# Y
			Label(self, text=("y"+str(p)), width=self.wdt).grid(row=2, column=p)
			self.pontos[1].append(Entry(self, width=self.wdt))
			self.pontos[1][p].grid(row=3, column=p)

		# ===== Definir e Cosntruir Elementos =====
		self.b_SistemaLinear = Button(self, text="Sistema Linear", command=self.cSL, fg="white", bg="black", width=l*4)
		self.b_SistemaLinear.grid(row=4, column=0, columnspan=n)

		self.b_Lagrange = Button(self, text="Lagrange", command=self.cLagrange, fg="white", bg="black", width=l*4)
		self.b_Lagrange.grid(row=5, column=0, columnspan=n)

		self.b_Newton = Button(self, text="Newton", command=self.cNewton, fg="white", bg="black", width=l*4)
		self.b_Newton.grid(row=6, column=0, columnspan=n)

		self.jResposta = Resposta(self, self.n)
		self.jResposta.grid(row=7, column=0, columnspan=n)

	def lerDados(self):
		self.prec = int(self.raiz.e_precisão.get())
		mm.mp.dps = self.prec
		pts = [[],[]]
		for p in range (0,self.n):
			pts[0].append(mm.mpf(self.pontos[0][p].get()))
			pts[1].append(mm.mpf(self.pontos[1][p].get()))
		return pts

	# Função chamada pelo Clique Salvar
	def Salvar(self):
		pts = self.lerDados()
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile="Interpolação", filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(str(self.n))
		arq.write("\n")
		arq.write(str(self.prec))
		arq.write("\n")
		for p in range (self.n):
			for xy in range (2):
				arq.write(str(pts[xy][p]))
				arq.write("\n")
		arq.close()

	# Clique Sistema Linear
	def cSL(self):
		pts = self.lerDados()
		pol = SL(pts, self.prec)
		resp = "Sistema Linear\n\n"+pol+"\n"
		self.jResposta.txtResp = resp
		self.jResposta.texto.config(text=self.jResposta.txtResp)
		self.jResposta.sf = tsf(pol)
		self.jResposta.opçõesRespostas()

	# Clique Lagrange
	def cLagrange(self):
		pts = self.lerDados()
		pol = Lagrange(pts, self.prec)
		resp = "Lagrange\n\n"+pol+"\n"
		self.jResposta.txtResp = resp
		self.jResposta.texto.config(text=self.jResposta.txtResp)
		self.jResposta.sf = tsf(pol)
		self.jResposta.opçõesRespostas()

	# Clique Newton
	def cNewton(self):
		pts = self.lerDados()
		pol = Newton(pts, self.prec)
		resp = "Newton\n\n"+pol+"\n"
		self.jResposta.txtResp = resp
		self.jResposta.texto.config(text=self.jResposta.txtResp)
		self.jResposta.sf = tsf(pol)
		self.jResposta.opçõesRespostas()

class Resposta(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.raiz = raiz
		self.n = n
		self.sf = "x"
		self.txtResp = "Clique em Algum Método"
		# ===== Definir Elementos =====
			# Textos
		self.texto = Label(self, text=self.txtResp, width=3*l)
		self.t_extrapolarX = Label(self, text="X para Extrapolar", width=l)
		self.t_extrapolarY = Label(self, text="Y para Extrapolar", width=l)
			# Botões
		self.b_extrapolarX = Button(self, text="Extrapolar X", command=self.cInterpolarX, fg="white", bg="black", width=l)
		self.b_extrapolarY = Button(self, text="Extrapolar Y", command=lambda: self.cInterpolarY(raiz), fg="white", bg="black", width=l)
		self.b_gerarGráfico = Button(self, text="GerarGráfico", command=lambda: self.cGerarGráfico(raiz), fg="white", bg="black", width=l)
			# Entradas
		self.e_extrapolarX = Entry(self)
		self.e_extrapolarY = Entry(self)
		
		# ===== Construir Elementos =====
			# Textos
		self.texto.grid(row=0, column=0, columnspan=4)
			# Botões
			# Entradas

	def opçõesRespostas(self):
		# ===== Construir Elementos =====
			# Textos
		self.t_extrapolarX.grid(row=1, column=0)
		self.t_extrapolarY.grid(row=2, column=0)
			# Botões
		self.b_extrapolarX.grid(row=1, column=2)
		self.b_extrapolarY.grid(row=2, column=2)
		self.b_gerarGráfico.grid(row=1, column=3, rowspan=2)
			# Entradas
		self.e_extrapolarX.grid(row=1, column=1)
		self.e_extrapolarY.grid(row=2, column=1)

	def cInterpolarX(self):
		xs = self.e_extrapolarX.get()
		self.raiz.lerDados()
		mm.mp.dps = self.raiz.prec
		x = mm.mpf(xs)
		txt = self.txtResp + "\nInterpolar em %s(x) = "%(xs) + str(f(x,self.sf,self.raiz.prec)) + "\n"
		self.texto.config(text=txt)

	def cInterpolarY(self, raiz):
		pts = raiz.lerDados()
		ys = self.e_extrapolarY.get()
		prec = self.raiz.prec
		mm.mp.dps = prec
		y = mm.mpf(ys)
		sfE = self.sf + "-(" + ys +")"
		# x = secanteInter(min(pts[0]),pts[0][rd.randrange(1,len(pts[0]))],sfE,prec)
		x = secanteInter(min(pts[0]),max(pts[0]),sfE,prec)
		txt = self.txtResp + "\nInterpolar em %s(y) = "%(ys) + str(x) + "\n"
		self.texto.config(text=txt)

	def cGerarGráfico(self, raiz):
		pts = raiz.lerDados()
		gG(pts, self.sf)
		print("cGerarGráfico Apertado")