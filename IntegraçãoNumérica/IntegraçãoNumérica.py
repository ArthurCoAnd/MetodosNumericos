from tkinter import *
# from tkinter import filedialog

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=7

class iNum(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Integração Numérica", width=(2*l))
		self.t_resposta = Label(self, text="Aperte um Método Para Calcular a Área Abaixo da Curva", width=(2*l))
		self.t_sf = Label(self, text="Função - f(x)", width=l)
			# Botões
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregar, fg="white", bg="black")
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvar, fg="white", bg="black")
		self.b_Trap = Button(self, text="Trapézios", command=self.cCarregar, fg="white", bg="black", width=(2*l))
		self.b_TrapR = Button(self, text="Trapézios Repetidos", command=self.cCarregar, fg="white", bg="black", width=(2*l))
		self.b_Simp13 = Button(self, text="1/3 de Simpson", command=self.cCarregar, fg="white", bg="black", width=(2*l))
		self.b_Simp13R = Button(self, text="1/3 de Simpson Repetido", command=self.cCarregar, fg="white", bg="black", width=(2*l))
		self.b_Simp38 = Button(self, text="3/8 de Simpson", command=self.cCarregar, fg="white", bg="black", width=(2*l))
			# Entradas
		self.e_sf = Entry(self, width=l)
		
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.t_resposta.grid(row=lr, column=0, columnspan=2)
		self.t_sf.grid(row=1, column=0)
			# Botões
		self.b_carregar.grid(row=0, column=0)
		self.b_salvar.grid(row=0, column=1)
		self.b_Trap.grid(row=2, column=0, columnspan=2)
		self.b_TrapR.grid(row=3, column=0, columnspan=2)
		self.b_Simp13.grid(row=4, column=0, columnspan=2)
		self.b_Simp13R.grid(row=5, column=0, columnspan=2)
		self.b_Simp38.grid(row=6, column=0, columnspan=2)
			# Entradas
		self.e_sf.grid(row=1, column=1)

	def cSalvar(self):
		print("Botão Apertado")

	def cCarregar(self):
		print("Botão Apertado")

	def cTrap(self):
		print("Botão Apertado")

	def cTrapR(self):
		print("Botão Apertado")

	def cSimp13(self):
		print("Botão Apertado")

	def cSimp13R(self):
		print("Botão Apertado")

	def cSimp38(self):
		print("Botão Apertado")