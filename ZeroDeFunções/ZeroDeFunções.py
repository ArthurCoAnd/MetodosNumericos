from tkinter import *
from tkinter import filedialog
# Importar Ferramentas
from ZeroDeFunções.dadosZDF import dados
from ZeroDeFunções.Funções.gerarGráfico import gerarGráfico as gG
from ZeroDeFunções.Funções.validarIntervalo import validarIntervalo as vI
from Ferramentas.fts import fts
from Ferramentas.rmve import rmve
# Importar Métodos
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=15
# ===== Padrão de Dados Para Testres - Deletar no Futuro ======
p = dados(0,1,1e-3,10,"(3*x**3)-(4*x**2)-(10*x)+10","(9*x**2)-(8*x)-10","((3*x**3)-(4*x**2)+10)/10")

class ZdF(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
			# Textos
		self.t_título = Label(self, text="Zero de Funções", width=(2*l))
		self.t_resposta = Label(self, text="Aperte um Método Para Calcular a Raiz da Função", width=(2*l), anchor=W, justify=LEFT)
		self.t_sf = Label(self, text="Função - f(x)", width=l)
		self.t_sdf = Label(self, text="Derivada da Função - f'(x)", width=l)
		self.t_spf = Label(self, text="Função Ponto Fixo", width=l)
		self.t_a = Label(self, text="Intervalo Inicial - a/xk", width=l)
		self.t_b = Label(self, text="Intervalo Final - b/xkm", width=l)
		self.t_e = Label(self, text="Erro - e ", width=l)
		self.t_kmax = Label(self, text="Interações Máximas", width=l)

			# Botões
		self.b_salvar = Button(self, text="Salvar", command=self.cSalvar, fg="white", bg="black")
		self.b_carregar = Button(self, text="Carregar", command=self.cCarregar, fg="white", bg="black")
		self.b_gfr = Button(self, text="Gerar Gráfico", command=self.cgfr, fg="white", bg="black", width=(2*l))
		self.b_vi = Button(self, text="Verificar Intervalo", command=self.cvi, fg="white", bg="black", width=(2*l))
		self.b_Bissecção = Button(self, text="Bissecção", command=self.cBissecção, fg="white", bg="black", width=(2*l))
		self.b_PosiçãoFalsa = Button(self, text="Posição Falsa", command=self.cPosiçãoFalse, fg="white", bg="black", width=(2*l))
		self.b_PontoFixo = Button(self, text="Ponto Fixo", command=self.cPontoFixo, fg="white", bg="black", width=(2*l))
		self.b_NewtonRaphson = Button(self, text="Newton-Raphson", command=self.cNewtonRaphson, fg="white", bg="black", width=(2*l))
		self.b_Secante = Button(self, text="Secante", command=self.cSecante, fg="white", bg="black", width=(2*l))

			# Entradas
		self.e_sf = Entry(self, width=l)
		self.e_sdf = Entry(self, width=l)
		self.e_spf = Entry(self, width=l)
		self.e_a = Entry(self, width=l)
		self.e_b = Entry(self, width=l)
		self.e_e = Entry(self, width=l)
		self.e_kmax = Entry(self, width=l)

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
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.t_resposta.grid(row=lr, column=0, columnspan=2)
		self.t_sf.grid(row=1, column=0)
		self.t_sdf.grid(row=2, column=0)
		self.t_spf.grid(row=3, column=0)
		self.t_a.grid(row=4, column=0)
		self.t_b.grid(row=5, column=0)
		self.t_e.grid(row=6, column=0)
		self.t_kmax.grid(row=7, column=0)

			# Botões
		self.b_carregar.grid(row=0, column=0)
		self.b_salvar.grid(row=0, column=1)
		self.b_Bissecção.grid(row=8, column=0, columnspan=2)
		self.b_PosiçãoFalsa.grid(row=9, column=0, columnspan=2)
		self.b_PontoFixo.grid(row=10, column=0, columnspan=2)
		self.b_NewtonRaphson.grid(row=11, column=0, columnspan=2)
		self.b_Secante.grid(row=12, column=0, columnspan=2)
		self.b_gfr.grid(row=13, column=0, columnspan=2)
		self.b_vi.grid(row=14, column=0, columnspan=2)

			# Entradas
		self.e_sf.grid(row=1, column=1)
		self.e_sdf.grid(row=2, column=1)
		self.e_spf.grid(row=3, column=1)
		self.e_a.grid(row=4, column=1)
		self.e_b.grid(row=5, column=1)
		self.e_e.grid(row=6, column=1)
		self.e_kmax.grid(row=7, column=1)

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

	# Clique Botão Carregar
	def cCarregar(self):
		arqN = filedialog.askopenfilename(initialdir="/ZeroDeFunções/Configurações", title="Escolha um Arquivo")
		arq = open(arqN, "r")
		
		self.e_sf.delete(0,END)
		self.e_sf.insert(END,rmve(arq.readline()))
		
		self.e_sdf.delete(0,END)
		self.e_sdf.insert(END,rmve(arq.readline()))
		
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

		self.t_resposta.config(text="Arquivo Carregado", bg="green", width=2*l)

	# Clique Botão Salvar
	def cSalvar(self):
		arqS = fts(self.e_sf.get())
		arq = open("ZeroDeFunções/Configurações/"+arqS+".txt", "w")
		arq.write(self.e_sf.get())
		arq.write("\n")
		arq.write(self.e_sdf.get())
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
		arq.close()
		self.t_resposta.config(text="Arquivo Salvo", bg="green", width=2*l)

	# Clique Botão Bissecção
	def cBissecção(self):
		d = self.lerDados()
		self.t_resposta.config(text="Intervalo INVÁLIDO", bg="red", width=2*l)
		s = bissecção(d)
		self.t_resposta.config(text=s, bg="white", width=2*l)
			
	# Clique Botão Posição Falsa
	def cPosiçãoFalse(self):
		d = self.lerDados()
		self.t_resposta.config(text="Intervalo INVÁLIDO", bg="red", width=2*l)
		s = posiçãoFalsa(d)
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

	# Cliqeu Botâo Verificar Intervalo
	def cvi(self):
		d = self.lerDados()
		self.t_resposta.config(text="Intervalo INVÁLIDO", bg="red", width=2*l)
		chave = vI(d)
		if(chave):
			self.t_resposta.config(text="Intervalo VÁLIDO", bg="green", width=2*l)
			