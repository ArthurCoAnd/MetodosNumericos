# Importar Bibliotecas
import mpmath as mm
import pandas as pd
from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.título import título
from Ferramentas.rmve import rmve
# Importar Métodos
from ZeroDePolinômios.MétodosZdP.BirgeVieta import BirgeVieta as BV
from ZeroDePolinômios.MétodosZdP.BriotRuffini import BriotRuffini as BR
from ZeroDePolinômios.MétodosZdP.Newton import Newton

# Tamanho Largura das Colunas
l=30

class ZdP(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Zero de Polinômios", width=l)
		self.t_n = Label(self, text="Grau do Polinômio", width=l)
		self.t_x0 = Label(self, text="x0", width=l)
		self.t_k = Label(self, text="Número de Interações", width=l)
		self.t_e = Label(self, text="Epsilon", width=l)
		self.t_prec = Label(self, text="Precisão", width=l)
			# Botões
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvar, fg="white", bg="DodgerBlue4")
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregar, fg="white", bg="DodgerBlue4")
		self.b_gerarPolinômio = Button(self, text="Gerar Polinômio", command=self.cGerarPolinômio, fg="white", bg="DodgerBlue4", width=l)
			# Botões Verificadores
			# Entradas
		self.e_n = Entry(self, width=l)
		self.e_x0 = Entry(self, width=l)
		self.e_k = Entry(self, width=l)
		self.e_e = Entry(self, width=l)
		self.e_prec = Entry(self, width=l)

		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=1)
		self.t_n.grid(row=1, column=0)
			# Botões
		self.b_carregar.grid(row=0, column=0)
		self.b_gerarPolinômio.grid(row=1, column=2)
			# Entradas
		self.e_n.grid(row=1, column=1)

		self.jPolinômio = None

	# Clique Gerar Pontos
	def cGerarPolinômio(self):
		self.b_salvar.grid(row=0, column=2)
		n = 1 + int(self.e_n.get())
		self.t_x0.grid(row=2, column=0)
		self.e_x0.grid(row=2, column=1)
		self.t_k.grid(row=3, column=0)
		self.e_k.grid(row=3, column=1)
		self.t_e.grid(row=4, column=0)
		self.e_e.grid(row=4, column=1)
		self.t_prec.grid(row=5, column=0)
		self.e_prec.grid(row=5, column=1)
		if self.jPolinômio is not None:
			self.jPolinômio.destroy()
		self.jPolinômio = Polinômio(self, n)
		self.jPolinômio.grid(row=6, column=0, columnspan=3)

	# Clique Botão Carregar
	def cCarregar(self):
		arqN = filedialog.askopenfilename(initialdir="./", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		n = int(rmve(arq.readline()))
		self.e_n.delete(0,END)
		self.e_n.insert(END, n)
		self.cGerarPolinômio()
		self.e_x0.delete(0,END)
		self.e_x0.insert(END, rmve(arq.readline()))
		self.e_k.delete(0,END)
		self.e_k.insert(END, rmve(arq.readline()))
		self.e_e.delete(0,END)
		self.e_e.insert(END, rmve(arq.readline()))
		self.e_prec.delete(0,END)
		self.e_prec.insert(END, rmve(arq.readline()))
		for p in range (n+1):
			self.jPolinômio.ePolinômio[p].insert(END,rmve(arq.readline()))
		arq.close()
		self.jPolinômio.t_resposta.config(text="Arquivo Carregado", bg="green")

	# Clique Botão Salvar
	def cSalvar(self):
		self.jPolinômio.salvarPolinômio()

class Polinômio(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.raiz = raiz
		self.n = n
		self.x0 = mm.mpf("0")
		self.k = 0
		self.e = 0
		self.prec = 0
		self.wdt = int(l*3/n)
		self.ePolinômio = []
		for p in range (self.n):
			Label(self, text=("x^"+str(p)), width=self.wdt).grid(row=0, column=p)
			self.ePolinômio.append(Entry(self, width=self.wdt))
			self.ePolinômio[p].grid(row=1, column=p)

		# ===== Elementos =====
		self.t_escolha = Label(self, text="Escolha o método para encontrar a raiz do polinômio:", width = 3*l)
		self.t_escolha.grid(row=2, column=0, columnspan=self.n)

		self.b_BirgeVieta = Button(self, text="Birge-Vieta", command=self.cBirgeVieta, fg="white", bg="DodgerBlue4", width=3*l)
		self.b_BirgeVieta.grid(row=3, column=0, columnspan=self.n)

		self.b_BriotRuffini = Button(self, text="Briot-Ruffini", command=self.cBriotRuffini, fg="white", bg="DodgerBlue4", width=3*l)
		self.b_BriotRuffini.grid(row=4, column=0, columnspan=self.n)

		self.b_Newton = Button(self, text="Newton", command=self.cNewton, fg="white", bg="DodgerBlue4", width=3*l)
		self.b_Newton.grid(row=5, column=0, columnspan=self.n)

		self.t_resposta = Label(self, text="Escolha um método para achar a raiz do polinômio.", width=3*l)
		# self.t_resposta.grid(row=6, column=0, columnspan=self.n)

	def lerDados(self):
		self.prec = int(self.raiz.e_prec.get())
		mm.mp.dps = self.prec
		self.x0 = mm.mpf(self.raiz.e_x0.get())
		self.k = self.raiz.e_k.get()
		self.e = self.raiz.e_e.get()
		mm.mp.dps = self.prec
		poli = []
		for p in range(self.n):
			poli.append(mm.mpf(self.ePolinômio[p].get()))
		return poli

	def salvarPolinômio(self):
		poli = self.lerDados()
		arqS = "ZeroDePolinômios"
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile=arqS, filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(str(self.n-1))
		arq.write("\n")
		arq.write(str(self.x0))
		arq.write("\n")
		arq.write(str(self.k))
		arq.write("\n")
		arq.write(str(self.e))
		arq.write("\n")
		arq.write(str(self.prec))
		arq.write("\n")
		for p in range (self.n):
			arq.write(str(poli[p]))
			arq.write("\n")
		arq.close()
		self.t_resposta.config(text="Arquivo Salvo", bg="green")

	def cBirgeVieta(self):
		título("Birge-Vieta","=")
		poli = self.lerDados()
		print("Polinômio:")
		print(mm.matrix(poli))
		print("Raiz:")
		r = BV(poli, self.prec, self.x0, mm.mpf(self.e), int(self.k))
		print(r)
		rs = "Método de Birge-Vieta\nRaiz: "+str(r)
		self.t_resposta.grid(row=6, column=0, columnspan=self.n)
		self.t_resposta.config(text=rs, bg="white")

	def cBriotRuffini(self):
		título("Briot-Ruffini","=")
		poli = self.lerDados()
		print("Polinômio:")
		print(mm.matrix(poli))
		print("Raiz:")
		r = BR(poli, self.prec, self.x0)
		print(r)
		rs = "Método de Briot-Ruffini\nP(x0): "+str(r)
		self.t_resposta.grid(row=6, column=0, columnspan=self.n)
		self.t_resposta.config(text=rs, bg="white")

	def cNewton(self):
		título("Newton","=")
		poli = self.lerDados()
		print("Polinômio:")
		print(mm.matrix(poli))
		print("Raiz:")
		r = Newton(poli, self.prec, self.x0, mm.mpf(self.e), int(self.k))
		print(r)
		rs = "Método de Newton\nRaiz: "+str(r)
		self.t_resposta.grid(row=6, column=0, columnspan=self.n)
		self.t_resposta.config(text=rs, bg="white")