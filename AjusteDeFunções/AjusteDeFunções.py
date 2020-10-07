# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
import random as rd
from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.rmve import rmve
from AjusteDeFunções.FerramentasADF.gerarGráficoAjuste import gerarGráfico as gG
from AjusteDeFunções.FerramentasADF.secanteADF import secanteADF
# Importar Métodos
from AjusteDeFunções.MétodosADF.Linear import linear

# Tamanho Largura das Colunas
l=30

class AdF(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Ajuste de Funções", width=3*l)
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
		self.t_título.grid(row=0, column=0, columnspan=3)
		self.t_nPontos.grid(row=1, column=0)
			# Botões
		self.b_criarPontos.grid(row=1,column=2)
		self.b_carregar.grid(row=0, column=0)
			# Entradas
		self.e_nPontos.grid(row=1, column=1)
		
		self.jPontos = None

	# Clique Gerar Pontos
	def cGerarPontos(self):
		self.b_salvar.grid(row=0, column=2)
		nP = int(self.e_nPontos.get())
		self.t_precisão.grid(row=2, column=0)
		self.e_precisão.grid(row=2, column=1)
		novaJanela = Pontos(self, nP)
		if self.jPontos is not None:
			self.jPontos.destroy()
		self.jPontos = novaJanela
		self.jPontos.grid(row=3, column=0, columnspan=3)

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
		self.cGerarPontos()
		self.e_precisão.delete(0,END)
		self.e_precisão.insert(END, prec)
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
		self.pontos = [[],[]]
		for p in range (0,self.n):
			# X
			Label(self, text=("x"+str(p)), width=int(l*3/n)).grid(row=0, column=p)
			self.pontos[0].append(Entry(self, width=int(l*3/n)))
			self.pontos[0][p].grid(row=1, column=p)
			# Y
			Label(self, text=("y"+str(p)), width=int(l*3/n)).grid(row=2, column=p)
			self.pontos[1].append(Entry(self, width=int(l*3/n)))
			self.pontos[1][p].grid(row=3, column=p)

		# ===== Definir e Cosntruir Elementos =====
		self.b_funcLinear = Button(self, text="Função Linear", command=self.cFuncLinear, fg="white", bg="black", width=l*3)
		self.b_funcLinear.grid(row=4, column=0, columnspan=n)

		self.b_funcQuadOri = Button(self, text="Função Quadrada Vértice Origem", command=self.cFuncQuadOri, fg="white", bg="black", width=l*3)
		self.b_funcQuadOri.grid(row=5, column=0, columnspan=n)

		self.b_funcQuadOri = Button(self, text="Função Quadrada", command=self.cFuncQuad, fg="white", bg="black", width=l*3)
		self.b_funcQuadOri.grid(row=6, column=0, columnspan=n)

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
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile="Ajuste de Funções", filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(str(self.n))
		arq.write("\n")
		arq.write(str(self.prec))
		arq.write("\n")
		pts = self.lerDados()
		for p in range (self.n):
			for xy in range (2):
				arq.write(str(pts[xy][p]))
				arq.write("\n")
		arq.close()

	# Print Matriz mat
	def printMat(self, mat):
		'''
		for l in range (len(mat)):
			r = "|\t"
			for c in range (len(mat[0])):
				r += "%-12f\t"%(mat[l][c])
			r += "|"
			print(r)
		'''
		tabelaMatriz = pd.DataFrame(mat)
		print(tabelaMatriz)

	# Fatorar Matriz mat
	def fatorarMat(self, mat):
		mm.mp.dps = self.prec
		for d in range (len(mat)-1):
			for l in range (d+1, len(mat)):
				div = mm.mpf(mat[l][d]/mat[d][d])
				for c in range (len(mat[0])):
					mat[l][c]=mat[l][c]-(div*mat[d][c])

	# Clique Função Linear
	def cFuncLinear(self):
		título("Função Linear", "=")
		print("Matriz Base:")
		print("f(x) = a + bx")

		# Ler Dados
		pts = self.lerDados()

		# Gerar Matriz Base de Análise
		mat = [[0.0,0.0,0.0],[0.0,0.0,0.0]]
			# Registrando Parte Esquerda da Igualdade da Matriz
		for l in range (0,2):
			for c in range (0,2):
				for k in range (0,self.n):
					mat[l][c] += ((pts[0][k])**l)*((pts[0][k])**c)
			# Registrando Parte Direita da Igualdade da Matriz
		for l in range (0,2):
			for k in range (0,self.n):
				mat[l][2] += pts[1][k]*(pts[0][k]**l)
			# Print Matriz Base de Análise
		print("\nMatriz Base:")
		self.printMat(mat)

		# Fatorar Matriz Base de Análise
		self.fatorarMat(mat)
		print("\nMatriz Base Fatorada:")
		self.printMat(mat)

		# Processar Dados Finais
		b = mat[1][2]/mat[1][1]
		a = (mat[0][2]-(mat[0][1]*b))/mat[0][0]

		# Gerar Resposta
		mm.mp.pretty = True
		stra = str(a)
		strb = str(b)
		print("\nFunção Aproximada:")
		print("f(x) = %s + %sx"%(stra,strb))
		s = ""
		s += "Função Linear Base:\n"
		s += "f(x) = a + bx\n"
		s += "Ajuste Encontrado:\n"
		s += "f(x) = %s + %sx"%(stra,strb)
		self.jResposta.txtResp = s
		self.jResposta.texto.config(text=self.jResposta.txtResp)

		# Finalizar
		self.jResposta.sf = "%f+%f*x"%(a,b)
		self.jResposta.opçõesRespostas()

	# Clique Função Quadrada com Vértice na Origem
	def cFuncQuadOri(self):
		título("Função Quadrada Vértice na Origem", "=")
		print("Matriz Base:")
		print("f(x) = ax²")

		# Ler Dados
		pts = self.lerDados()

		# Gerar Dados Base de Análise
		SumX2Y = 0
		SumX4 = 0
		for p in range (self.n):
			SumX2Y += (pts[0][p]**2)*(pts[1][p])
			SumX4 += (pts[0][p]**4)

		# Processar Dados Finais
		a = SumX2Y/SumX4

		# Gerar Resposta
		mm.mp.pretty = True
		stra = str(a)
		print("\nFunção Aproximada:")
		print("f(x) = %sx²"%(stra))
		s = ""
		s += "Função Quadrada Vértice na Origem Base:\n"
		s += "f(x) = ax²\n"
		s += "Ajuste Encontrado:\n"
		s += "f(x) = %sx²"%(stra)
		self.jResposta.txtResp = s
		self.jResposta.texto.config(text=self.jResposta.txtResp)

		# Finalizar
		self.jResposta.sf = "%f*x**2"%(a)
		self.jResposta.opçõesRespostas()

	# Clique Função Quadrada
	def cFuncQuad(self):
		título("Função Quadrada", "=")
		print("Matriz Base:")
		print("f(x) = ax² + bx + c")

		# Ler Dados
		pts = self.lerDados()

		# Gerar Matriz Base de Análise
		mat = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
			# Registrando Parte Esquerda da Igualdade da Matriz
		for l in range (0,3):
			for c in range (0,3):
				for k in range (0, self.n):
					mat[l][c] += (pts[0][k]**l)*(pts[0][k]**c)
			# Registrando Parte Direita da Igualdade da Matriz
		for l in range (0,3):
			for k in range (0, self.n):
				mat[l][3] += (pts[1][k])*(pts[0][k]**l)
			# Print Matriz Base de Análise
		print("\nMatriz Base:")
		self.printMat(mat)

		# Fatorar Matriz Base de Análise
		self.fatorarMat(mat)
		print("\nMatriz Base Fatorada:")
		self.printMat(mat)

		# Porcessar Dados Finais
		a = mat[2][3]/mat[2][2]
		b = (mat[1][3]-(mat[1][2]*a))/mat[1][1]
		c = (mat[0][3]-(mat[0][1]*b)-(mat[0][2]*a))/mat[0][0]

		# Gerar Resposta
		mm.mp.pretty = True
		stra = str(a)
		strb = str(b)
		strc = str(c)
		print("\nFunção Aproximada:")
		print("f(x) = %sx² + %sx + %s"%(stra,strb,strc))
		s = ""
		s += "Função Quadrada:\n"
		s += "f(x) = ax² + bx + c\n"
		s += "Ajuste Encontrado:\n"
		s += "f(x) = %sx² + %sx + %s"%(stra,strb,strc)
		self.jResposta.txtResp = s
		self.jResposta.texto.config(text=self.jResposta.txtResp)

		# Finalizar
		self.jResposta.sf = "(%f*x**2)+(%f*x)+%f"%(a,b,c)
		self.jResposta.opçõesRespostas()

class Resposta(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.n = n
		self.sf = "x"
		self.txtResp = "Clique em Algum Método"
		# ===== Definir Elementos =====
			# Textos
		self.texto = Label(self, text=self.txtResp, width=3*l)
		self.t_extrapolarX = Label(self, text="X para Extrapolar", width=l)
		self.t_extrapolarY = Label(self, text="Y para Extrapolar", width=l)
			# Botões
		self.b_extrapolarX = Button(self, text="Extrapolar X", command=self.cExtrapolarX, fg="white", bg="black", width=l)
		self.b_extrapolarY = Button(self, text="Extrapolar Y", command=lambda: self.cExtrapolarY(raiz), fg="white", bg="black", width=l)
		self.b_gerarGráfico = Button(self, text="GerarGráfico", command=lambda: self.cGerarGráfico(raiz), fg="white", bg="black", width=3*l)
			# Entradas
		self.e_extrapolarX = Entry(self)
		self.e_extrapolarY = Entry(self)
		
		# ===== Construir Elementos =====
			# Textos
		self.texto.grid(row=0, column=0, columnspan=3)
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
		self.b_gerarGráfico.grid(row=3, column=0, columnspan=3)
			# Entradas
		self.e_extrapolarX.grid(row=1, column=1)
		self.e_extrapolarY.grid(row=2, column=1)

	def cExtrapolarX(self):
		xs = self.e_extrapolarX.get()
		x = float(xs)
		txt = self.txtResp + "\n\nExtrapolação em %s(x) = %f"%(xs,f(x,self.sf))
		self.texto.config(text=txt)

	def cExtrapolarY(self, raiz):
		pts = raiz.lerDados()
		ys = self.e_extrapolarY.get()
		y = float(ys)
		sfE = self.sf + "-(" + ys +")"
		prec = int(raiz.raiz.e_precisão.get())
		x = secanteADF(min(pts[0]),pts[0][rd.randrange(1,len(pts[0]))],sfE,prec)
		txt = self.txtResp + "\n\nExtrapolação em %s(y) = %g"%(ys,x)
		self.texto.config(text=txt)

	def cGerarGráfico(self, raiz):
		pts = raiz.lerDados()
		gG(pts, self.sf)