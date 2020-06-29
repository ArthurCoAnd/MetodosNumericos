from tkinter import *
# Importar Ferramentas
from ZeroDeFunções.dadosZDF import dados
from ZeroDeFunções.Funções.gerarGráfico import gerarGráfico as gG
# Importar Métodos
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

l=30

class ZdF:
	def __init__(self, raiz):
		janela = Frame(raiz)
		janela.grid(row=0, column=0)

		# Tamanho Largura das Colunas
		l=30
		# Linha das Respostas
		lr=14
		# Padrão de Dados Para Testres - Deletar no Futuro
		p = dados(0,1,1e-3,10,"(3*x**3)-(4*x**2)-(10*x)+10","(9*x**2)-(8*x)-10","((3*x**3)-(4*x**2)+10)/10")

		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(janela, text="Zero de Funções", width=(2*l))
		self.t_resposta = Label(janela, text="Aperte um Método Para Calcular a Raiz", width=(2*l))
		self.t_sf = Label(janela, text="Função - f(x)", width=l)
		self.t_sdf = Label(janela, text="Derivada da Função - f'(x)", width=l)
		self.t_spf = Label(janela, text="Função Ponto Fixo", width=l)
		self.t_a = Label(janela, text="Intervalo Inicial - a/xk", width=l)
		self.t_b = Label(janela, text="Intervalo Final - b/xkm", width=l)
		self.t_e = Label(janela, text="Erro - e ", width=l)
		self.t_kmax = Label(janela, text="Interações Máximas", width=l)

			# Botões
		self.b_gfr = Button(janela, text="Gerar Gráfico", command=self.cgfr, fg="white", bg="black", width=(2*l))
		self.b_Bissecção = Button(janela, text="Bissecção", command=self.cBissecção, fg="white", bg="black", width=(2*l))
		self.b_PosiçãoFalsa = Button(janela, text="Posição Falsa", command=self.cPosiçãoFalse, fg="white", bg="black", width=(2*l))
		self.b_PontoFixo = Button(janela, text="Ponto Fixo", command=self.cPontoFixo, fg="white", bg="black", width=(2*l))
		self.b_NewtonRaphson = Button(janela, text="Newton-Raphson", command=self.cNewtonRaphson, fg="white", bg="black", width=(2*l))
		self.b_Secante = Button(janela, text="Secante", command=self.cSecante, fg="white", bg="black", width=(2*l))

			# Entradas
		self.e_sf = Entry(janela, width=l)
		self.e_sdf = Entry(janela, width=l)
		self.e_spf = Entry(janela, width=l)
		self.e_a = Entry(janela, width=l)
		self.e_b = Entry(janela, width=l)
		self.e_e = Entry(janela, width=l)
		self.e_kmax = Entry(janela, width=l)

		# ===== Preset de valores para testes rápidos =====
		self.e_a.insert(END,p.a)
		self.e_b.insert(END,p.b)
		self.e_e.insert(END,p.e)
		self.e_kmax.insert(END,p.kmax)
		self.e_sf.insert(END,p.sf)
		self.e_sdf.insert(END,p.sdf)
		self.e_spf.insert(END,p.spf)

		# ===== Construir Elementos =====
			# Textos
		self.t_título.grid(row=0 ,column=0, columnspan=2)
		self.t_resposta.grid(row=lr ,column=0, columnspan=2)
		self.t_sf.grid(row=1 ,column=0)
		self.t_sdf.grid(row=2 ,column=0)
		self.t_spf.grid(row=3 ,column=0)
		self.t_a.grid(row=4 ,column=0)
		self.t_b.grid(row=5 ,column=0)
		self.t_e.grid(row=6 ,column=0)
		self.t_kmax.grid(row=7 ,column=0)

			# Botões
		self.b_Bissecção.grid(row=8 ,column=0, columnspan=2)
		self.b_PosiçãoFalsa.grid(row=9 ,column=0, columnspan=2)
		self.b_PontoFixo.grid(row=10 ,column=0, columnspan=2)
		self.b_NewtonRaphson.grid(row=11 ,column=0, columnspan=2)
		self.b_Secante.grid(row=12 ,column=0, columnspan=2)
		self.b_gfr.grid(row=13 ,column=0, columnspan=2)

			# Entradas
		self.e_sf.grid(row=1 ,column=1)
		self.e_sdf.grid(row=2 ,column=1)
		self.e_spf.grid(row=3 ,column=1)
		self.e_a.grid(row=4 ,column=1)
		self.e_b.grid(row=5 ,column=1)
		self.e_e.grid(row=6 ,column=1)
		self.e_kmax.grid(row=7 ,column=1)

	def lerDados(self):
		x = dados(0,0,0,0,"","","")
		x.a = float(self.e_a.get())
		x.b = float(self.e_b.get())
		x.e = float(self.e_e.get())
		x.kmax = float(self.e_kmax.get())
		x.sf = self.e_sf.get()
		x.sdf = self.e_sdf.get()
		x.spf = self.e_spf.get()
		return x

	# Clique Botão Bissecção
	def cBissecção(self):
		s = "ERRO"
		self.t_resposta.config(text=s, bg="red", width=2*l)
		d = self.lerDados()
		s = bissecção(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Posição Falsa
	def cPosiçãoFalse(self):
		s = "ERRO"
		self.t_resposta.config(text=s, bg="red", width=2*l)
		d = self.lerDados()
		s=posiçãoFalsa(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Ponto Fixo
	def cPontoFixo(self):
		s = "ERRO"
		self.t_resposta.config(text=s, bg="red", width=2*l)
		d = self.lerDados()
		s=pontoFixo(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Newton Raphson
	def cNewtonRaphson(self):
		s = "ERRO"
		self.t_resposta.config(text=s, bg="red", width=2*l)
		d = self.lerDados()
		s=newtonRaphson(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Secante
	def cSecante(self):
		s = "ERRO"
		self.t_resposta.config(text=s, bg="red", width=2*l)
		d = self.lerDados()
		s=secante(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)

	# Clique Botão Gerar Gráfico
	def cgfr(self):
		d = self.lerDados()
		gG(d)