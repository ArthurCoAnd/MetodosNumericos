# Importar Bibliotecas
from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from Ferramentas.fts import fts
from Ferramentas.rmve import rmve
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados
from ZeroDeFunções.FerramentasZDF.RespostaZDF import RespostaZDF as rZDF
from ZeroDeFunções.FerramentasZDF.GerarGráficoZDF import gerarGráficoZDF as gG
from ZeroDeFunções.FerramentasZDF.ValidarIntervalo import validarIntervalo as vI
# Importar Métodos
from ZeroDeFunções.MétodosZDF.Bissecção import bissecção
from ZeroDeFunções.MétodosZDF.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.MétodosZDF.PontoFixo import pontoFixo
from ZeroDeFunções.MétodosZDF.NewtonRaphson import newtonRaphson
from ZeroDeFunções.MétodosZDF.Secante import secante

# Tamanho Largura das Colunas
l=45

class ZdF(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Zero de Funções", width=(2*l))
		self.t_resposta = Label(self, text="Aperte um Método Para Calcular a Raiz da Função", width=(2*l), anchor=W, justify=LEFT, font="Consolas 9")
		self.t_calculos = Label(self, width=(3*l), font="Consolas 9")
		self.t_sf = Label(self, text="Função - f(x)", width=l)
		self.t_sdf = Label(self, text="Derivada da Função - f'(x)", width=l)
		self.t_sddf = Label(self, text="Derivada Segunda da Função - f''(x)", width=l)
		self.t_spf = Label(self, text="Função Ponto Fixo", width=l)
		self.t_a = Label(self, text="Intervalo Inicial - a/xk0", width=l)
		self.t_b = Label(self, text="Intervalo Final - b/xk1", width=l)
		self.t_e = Label(self, text="Epsilon - ε", width=l)
		self.t_kmax = Label(self, text="Interações Máximas - kmax", width=l)
		self.t_prec = Label(self, text="Precisão - Dígitos", width=l)
			# Botões
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvar, fg="white", bg="DodgerBlue4")
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregar, fg="white", bg="DodgerBlue4")
		self.b_gfr = Button(self, text="Gerar Gráfico", command=self.cgfr, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_vi = Button(self, text="Verificar Intervalo", command=self.cvi, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_Bissecção = Button(self, text="Bissecção", command=self.cBissecção, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_PosiçãoFalsa = Button(self, text="Posição Falsa", command=self.cPosiçãoFalse, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_PontoFixo = Button(self, text="Ponto Fixo", command=self.cPontoFixo, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_NewtonRaphson = Button(self, text="Newton-Raphson", command=self.cNewtonRaphson, fg="white", bg="DodgerBlue4", width=(2*l))
		self.b_Secante = Button(self, text="Secante", command=self.cSecante, fg="white", bg="DodgerBlue4", width=(2*l))
			# Botões Verificadores
		self.bv_calculos_var = IntVar()
		self.bv_calculos = Checkbutton(self, text="Mostrar Cálculos?", variable=self.bv_calculos_var, onvalue=1, offvalue=0)
			# Entradas
		self.e_sf = Entry(self, width=l)
		self.e_sdf = Entry(self, width=l)
		self.e_sddf = Entry(self, width=l)
		self.e_spf = Entry(self, width=l)
		self.e_a = Entry(self, width=l)
		self.e_b = Entry(self, width=l)
		self.e_e = Entry(self, width=l)
		self.e_kmax = Entry(self, width=l)
		self.e_prec = Entry(self, width=l)

		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.t_resposta.grid(row=18, column=0, columnspan=2)
		self.t_sf.grid(row=1, column=0)
		self.t_sdf.grid(row=2, column=0)
		self.t_sddf.grid(row=3, column=0)
		self.t_spf.grid(row=4, column=0)
		self.t_a.grid(row=5, column=0)
		self.t_b.grid(row=6, column=0)
		self.t_e.grid(row=7, column=0)
		self.t_kmax.grid(row=8, column=0)
		self.t_prec.grid(row=9, column=0)
			# Botões
		self.b_carregar.grid(row=0, column=0)
		self.b_salvar.grid(row=0, column=1)
		self.b_Bissecção.grid(row=11, column=0, columnspan=2)
		self.b_PosiçãoFalsa.grid(row=12, column=0, columnspan=2)
		self.b_PontoFixo.grid(row=13, column=0, columnspan=2)
		self.b_NewtonRaphson.grid(row=14, column=0, columnspan=2)
		self.b_Secante.grid(row=15, column=0, columnspan=2)
		self.b_gfr.grid(row=16, column=0, columnspan=2)
		# self.b_vi.grid(row=17, column=0, columnspan=2)
			# Botões Verificadores
		# self.bv_calculos.grid(row=10, column=0, columnspan=2)
			# Entradas
		self.e_sf.grid(row=1, column=1)
		self.e_sdf.grid(row=2, column=1)
		self.e_sddf.grid(row=3, column=1)
		self.e_spf.grid(row=4, column=1)
		self.e_a.grid(row=5, column=1)
		self.e_b.grid(row=6, column=1)
		self.e_e.grid(row=7, column=1)
		self.e_kmax.grid(row=8, column=1)
		self.e_prec.grid(row=9, column=1)

	def lerDados(self):
		a = self.e_a.get()
		b = self.e_b.get()
		e = self.e_e.get()
		kmax = self.e_kmax.get()
		sf = self.e_sf.get()
		sdf = self.e_sdf.get()
		sddf = self.e_sddf.get()
		spf = self.e_spf.get()
		dec = self.e_prec.get()
		vcalc = self.bv_calculos_var.get()
		x = dados(a,b,e,kmax,sf,sdf,sddf,spf,dec,vcalc)
		return x

	# Clique Botão Carregar
	def cCarregar(self):
		arqN = filedialog.askopenfilename(initialdir="./", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		self.e_sf.delete(0,END)
		self.e_sf.insert(END,rmve(arq.readline()))
		self.e_sdf.delete(0,END)
		self.e_sdf.insert(END,rmve(arq.readline()))
		self.e_sddf.delete(0,END)
		self.e_sddf.insert(END,rmve(arq.readline()))
		self.e_spf.delete(0,END)
		self.e_spf.insert(END,rmve(arq.readline()))
		self.e_a.delete(0,END)
		self.e_a.insert(END,rmve(arq.readline()))
		self.e_b.delete(0,END)
		self.e_b.insert(END,rmve(arq.readline()))
		self.e_e.delete(0,END)
		self.e_e.insert(END,rmve(arq.readline()))
		self.e_kmax.delete(0,END)
		self.e_kmax.insert(END,rmve(arq.readline()))
		self.e_prec.delete(0,END)
		self.e_prec.insert(END,rmve(arq.readline()))
		self.bv_calculos_var.set(rmve(arq.readline()))
		arq.close()
		self.t_resposta.config(text="Arquivo Carregado", bg="green", width=2*l)

	# Clique Botão Salvar
	def cSalvar(self):
		arqS = fts(self.e_sf.get())
		arqN = filedialog.asksaveasfilename(initialdir="./", title="Escolha um Arquivo", initialfile=arqS, filetypes=[("Text files",".txt")], defaultextension=".txt")
		arq = open(arqN, "w")
		arq.write(self.e_sf.get())
		arq.write("\n")
		arq.write(self.e_sdf.get())
		arq.write("\n")
		arq.write(self.e_sddf.get())
		arq.write("\n")
		arq.write(self.e_spf.get())
		arq.write("\n")
		arq.write(self.e_a.get())
		arq.write("\n")
		arq.write(self.e_b.get())
		arq.write("\n")
		arq.write(self.e_e.get())
		arq.write("\n")
		arq.write(self.e_kmax.get())
		arq.write("\n")
		arq.write(self.e_prec.get())
		arq.write("\n")
		arq.write(str(self.bv_calculos_var.get()))
		arq.close()
		self.t_resposta.config(text="Arquivo Salvo", bg="green", width=2*l)

	# Clique Botão Bissecção
	def cBissecção(self):
		self.t_resposta.config(text="ERRO - DADOS INVÁLIDOS", bg="red", width=2*l)
		d = self.lerDados()
		self.t_resposta.config(text="ERRO - INTERVALO INVÁLIDO", bg="red", width=2*l)
		r = bissecção(d)
		self.t_resposta.config(text=r.resp, bg="white", width=2*l)
		
		# self.t_calculos.grid(row=0, column=2, rowspan=18)
		# self.t_calculos.config(text=r.calc)

	# Clique Botão Posição Falsa
	def cPosiçãoFalse(self):
		self.t_resposta.config(text="ERRO - DADOS INVÁLIDOS", bg="red", width=2*l)
		d = self.lerDados()
		self.t_resposta.config(text="ERRO - INTERVALO INVÁLIDO", bg="red", width=2*l)
		s = posiçãoFalsa(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)
			
	# Clique Botão Ponto Fixo
	def cPontoFixo(self):
		self.t_resposta.config(text="ERRO - DADOS INVÁLIDOS", bg="red", width=2*l)
		d = self.lerDados()
		self.t_resposta.config(text="ERRO - INTERVALO INVÁLIDO", bg="red", width=2*l)
		s=pontoFixo(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Newton Raphson
	def cNewtonRaphson(self):
		self.t_resposta.config(text="ERRO - DADOS INVÁLIDOS", bg="red", width=2*l)
		d = self.lerDados()
		self.t_resposta.config(text="ERRO - INTERVALO INVÁLIDO", bg="red", width=2*l)
		s=newtonRaphson(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Secante
	def cSecante(self):
		self.t_resposta.config(text="ERRO - DADOS INVÁLIDOS", bg="red", width=2*l)
		d = self.lerDados()
		self.t_resposta.config(text="ERRO - INTERVALO INVÁLIDO", bg="red", width=2*l)
		s=secante(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Gerar Gráfico
	def cgfr(self):
		d = self.lerDados()
		gG(d)

	# Cliqeu Botâo Verificar Intervalo
	def cvi(self):
		d = self.lerDados()
		s = vI(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)
		
			