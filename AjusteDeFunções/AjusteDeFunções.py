from tkinter import *
# Importar Ferramentas
from Ferramentas.título import título
from AjusteDeFunções.gerarGráfico import gerarGráfico as GG
# Tamanho Largura das Colunas
l=30

class AdF(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Ajuste de Funções", width=3*l)
		self.t_nPontos = Label(self, text="Número de Pontos (n)", width=l)
			# Botôes
		self.b_criarPontos = Button(self, text="Criar Pontos", command=self.cGerarPontos, fg="white", bg="black",width=l)
			# Entradas
		self.e_nPontos = Entry(self, width=l)
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0 ,column=0, columnspan=3)
		self.t_nPontos.grid(row=1,column=0)
			# Botôes
		self.b_criarPontos.grid(row=1,column=2)
			# Entradas
		self.e_nPontos.grid(row=1, column=1)

		self.jPontos = None

	def cGerarPontos(self):
		nP = int(self.e_nPontos.get())
		novaJanela = Pontos(self, nP)
		if self.jPontos is not None:
			self.jPontos.destroy()
		self.jPontos = novaJanela
		self.jPontos.grid(row=2, column=0, columnspan=3)

class Pontos(Frame):
	def __init__(self, raiz, n):
		Frame.__init__(self, raiz)
		self.n = n
		self.lr = 5
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

		self.b_funcLinear = Button(self, text="Função Linear", command=self.cFuncLinear, fg="white", bg="black", width=l*3)
		self.b_funcLinear.grid(row=4, column=0, columnspan=n)

		self.t_resposta = Label(self, text="Clique em um Método", width=(3*l))
		self.t_resposta.grid(row=self.lr, column=0, columnspan=n)

	def lerDados(self):
		pts = [[],[]]
		for p in range (0,self.n):
			pts[0].append(float(self.pontos[0][p].get()))
			pts[1].append(float(self.pontos[1][p].get()))
		return pts

	def fatorarMat(self, mat):
		for d in range (len(mat)-1):
			for l in range (d+1, len(mat)):
				div = mat[l][d]/mat[d][d]
				for c in range (len(mat[0])):
					mat[l][c]=mat[l][c]-(div*mat[d][c])

	def cFuncLinear(self):
		pts = self.lerDados()
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

		self.fatorarMat(mat)

		b = mat[1][2]/mat[1][1]
		a = (mat[0][2]-(mat[0][1]*b))/mat[0][0]
		s = ""
		s += "Função Linear Base:\n"
		s += "f(x) = a + bx\n"
		s += "Resposta Função Linear:\n"
		s += "f(x) = %f + %fx"%(a,b)

		self.t_resposta.config(text=s)

		sf = "%f+%f*x"%(a,b)

		GG(pts,sf)


		