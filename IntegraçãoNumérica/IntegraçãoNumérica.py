# Importar Bibliotecas
from tkinter import *
	# from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.fts import fts
from Ferramentas.rmve import rmve
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN

from IntegraçãoNumérica.MétodosIN.Trapézio import Trapézio
from IntegraçãoNumérica.MétodosIN.TrapézioRepetido import TrapézioRepetido
from IntegraçãoNumérica.MétodosIN.Simpson13 import Simpson13
from IntegraçãoNumérica.MétodosIN.Simpson13Repetido import Simpson13Repetido
from IntegraçãoNumérica.MétodosIN.Simpson38 import Simpson38
from IntegraçãoNumérica.MétodosIN.Simpson38Repetido import Simpson38Repetido

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=15

class iNum(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Integração Numérica", width=(2*l))
		self.t_resposta = Label(self, text="Aperte um Método Para Calcular a Aproximação da Integral", width=(2*l), anchor=W, justify=LEFT, font="Consolas 9")
		self.t_sf = Label(self, text="Função - f(x)", width=l)
		self.t_sdf = Label(self, text="Função Derivada Erro - f°(x)", width=l)
		self.t_a = Label(self, text="Intervalo Inicial - a", width=l)
		self.t_c = Label(self, text="c para a < c < b", width=l)
		self.t_b = Label(self, text="Intervalo Final - b", width=l)
		self.t_m = Label(self, text="Subdivisões - m", width=l)
		self.t_e = Label(self, text="Erro Máximo - e", width=l)
		self.t_pDec = Label(self, text="Precisão - Decimais", width=l)
			# Botões
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregar, fg="white", bg="black")
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvar, fg="white", bg="black")
		self.b_Trap = Button(self, text="Trapézios", command=self.cTrap, fg="white", bg="black", width=(2*l))
		self.b_TrapR = Button(self, text="Trapézios Repetido", command=self.cTrapR, fg="white", bg="black", width=(2*l))
		self.b_Simp13 = Button(self, text="1/3 de Simpson", command=self.cSimp13, fg="white", bg="black", width=(2*l))
		self.b_Simp13R = Button(self, text="1/3 de Simpson Repetido", command=self.cSimp13R, fg="white", bg="black", width=(2*l))
		self.b_Simp38 = Button(self, text="3/8 de Simpson", command=self.cSimp38, fg="white", bg="black", width=(2*l))
		self.b_Simp38R = Button(self, text="3/8 de Simpson Repetido", command=self.cSimp38R, fg="white", bg="black", width=(2*l))
		self.b_GerarGráfico = Button(self, text="Gerar Gráfico", command=self.cGerarGráfico, fg="white", bg="black", width=(2*l))
			# Botões Verificadores
		self.bv_sdf_var = IntVar()
		self.bv_sdf = Checkbutton(self, variable=self.bv_sdf_var, onvalue=1, offvalue=0)
		self.bv_c_var = IntVar()
		self.bv_c = Checkbutton(self, variable=self.bv_c_var, onvalue=1, offvalue=0)
		self.bv_e_var = IntVar()
		self.bv_e = Checkbutton(self, variable=self.bv_e_var, onvalue=1, offvalue=0)
			# Entradas
		self.e_sf = Entry(self, width=l)
		self.e_sdf = Entry(self, width=l)
		self.e_a = Entry(self, width=l)
		self.e_c = Entry(self, width=l)
		self.e_b = Entry(self, width=l)
		self.e_m = Entry(self, width=l)
		self.e_e = Entry(self, width=l)
		self.e_pDec = Entry(self, width=l)
		
		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.t_resposta.grid(row=lr, column=0, columnspan=2)
		self.t_sf.grid(row=1, column=0)
		self.t_sdf.grid(row=2, column=0)
		self.t_a.grid(row=3, column=0)
		self.t_c.grid(row=4, column=0)
		self.t_b.grid(row=5, column=0)
		self.t_m.grid(row=6, column=0)
		self.t_e.grid(row=7, column=0)
		self.t_pDec.grid(row=8, column=0)
			# Botões
		self.b_carregar.grid(row=0, column=0)
		self.b_salvar.grid(row=0, column=1)
		self.b_Trap.grid(row=9, column=0, columnspan=2)
		self.b_TrapR.grid(row=10, column=0, columnspan=2)
		self.b_Simp13.grid(row=11, column=0, columnspan=2)
		self.b_Simp13R.grid(row=12, column=0, columnspan=2)
		self.b_Simp38.grid(row=13, column=0, columnspan=2)
		self.b_Simp38R.grid(row=14, column=0, columnspan=2)
			# Botões Verificadores
		self.bv_sdf.grid(row=2 ,column=0, sticky=E)
		self.bv_c.grid(row=4 ,column=0, sticky=E)
		self.bv_e.grid(row=7 ,column=0, sticky=E)
			# Entradas
		self.e_sf.grid(row=1, column=1)
		self.e_sdf.grid(row=2, column=1)
		self.e_a.grid(row=3, column=1)
		self.e_c.grid(row=4, column=1)
		self.e_b.grid(row=5, column=1)
		self.e_m.grid(row=6, column=1)
		self.e_e.grid(row=7, column=1)
		self.e_pDec.grid(row=8, column=1)

	# Ler Dados das Entradas
	def lerDados(self):
		sf = self.e_sf.get()
		sdf = self.e_sdf.get()
		vsdf = self.bv_sdf_var.get()
		a = self.e_a.get()
		c = self.e_c.get()
		vc = self.bv_c_var.get()
		b = self.e_b.get()
		m = self.e_m.get()
		e = self.e_e.get()
		ve = self.bv_e_var.get()
		pDec = self.e_pDec.get()
		dados = DadosIN(sf,sdf,vsdf,a,c,vc,b,m,e,ve,pDec)
		return dados

	# Clique do Botão Salvar - Salva dados em um arquivo e pasta de escolha do usuário
	def cSalvar(self):
		arqS = fts(self.e_sf.get())
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile=arqS, filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(self.e_sf.get())
		arq.write("\n")
		arq.write(self.e_sdf.get())
		arq.write("\n")
		arq.write(str(self.bv_sdf_var.get()))
		arq.write("\n")
		arq.write(self.e_a.get())
		arq.write("\n")
		arq.write(self.e_c.get())
		arq.write("\n")
		arq.write(str(self.bv_c_var.get()))
		arq.write("\n")
		arq.write(self.e_b.get())
		arq.write("\n")
		arq.write(self.e_m.get())
		arq.write("\n")
		arq.write(self.e_e.get())
		arq.write("\n")
		arq.write(str(self.bv_e_var.get()))
		arq.write("\n")
		arq.write(self.e_pDec.get())
		arq.close()
		self.t_resposta.config(text="Arquivo Salvo", bg="green", width=2*l)

	# Clique Botão Carregar - Carrega dados de um arquivo escolhido pelo usuário
	def cCarregar(self):
		arqN = filedialog.askopenfilename(initialdir="./", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		self.e_sf.delete(0,END)
		self.e_sf.insert(END,rmve(arq.readline()))
		self.e_sdf.delete(0,END)
		self.e_sdf.insert(END,rmve(arq.readline()))
		self.bv_sdf_var.set(rmve(arq.readline()))
		self.e_a.delete(0,END)
		self.e_a.insert(END,rmve(arq.readline()))
		self.e_c.delete(0,END)
		self.e_c.insert(END,rmve(arq.readline()))
		self.bv_c_var.set(rmve(arq.readline()))
		self.e_b.delete(0,END)
		self.e_b.insert(END,rmve(arq.readline()))
		self.e_m.delete(0,END)
		self.e_m.insert(END,rmve(arq.readline()))
		self.e_e.delete(0,END)
		self.e_e.insert(END,rmve(arq.readline()))
		self.bv_e_var.set(rmve(arq.readline()))
		self.e_pDec.delete(0,END)
		self.e_pDec.insert(END,rmve(arq.readline()))
		arq.close()
		self.t_resposta.config(text="Arquivo Carregado", bg="green", width=2*l)

	# Clique Botão Trapézio
	def cTrap(self):
		dados = self.lerDados()
		Resp = Trapézio(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cTrapR(self):
		dados = self.lerDados()
		Resp = TrapézioRepetido(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cSimp13(self):
		dados = self.lerDados()
		Resp = Simpson13(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cSimp13R(self):
		dados = self.lerDados()
		Resp = Simpson13Repetido(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cSimp38(self):
		dados = self.lerDados()
		Resp = Simpson38(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cSimp38R(self):
		dados = self.lerDados()
		Resp = Simpson38Repetido(dados)
		self.t_resposta.config(text=Resp, bg="white", width=(2*l))

	def cGerarGráfico(self):
		print("Botão Gerar Gráfico Apertado")