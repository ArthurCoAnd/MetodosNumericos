# Importar Bibliotecas
from tkinter import *
# Importar Métodos
from ZeroDeFunções.ZeroDeFunções import ZdF
from ZeroDePolinômios.ZeroDePolinômios import ZdP
from SistemasLinears.SistemasLineares import SL
from AjusteDeFunções.AjusteDeFunções import AdF
from IntegraçãoNumérica.IntegraçãoNumérica import iNum

# Tamanho Largura das Colunas
l=30

class Aplicativo(Tk):
	def __init__(self):
		Tk.__init__(self)
		# ===== Definir Elementos =====
		self.t_título = Label(self, text="Menu", width=2*l)
		self.b_voltar = Button(self, text="<", command=lambda: self.TrocarJanela(Métodos), fg="white", bg="black")
		# ===== Construir Elementos =====
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.b_voltar.grid(row=0, column=0, sticky=W)
		self.janela = None
		self.TrocarJanela(Métodos)

	def TrocarJanela(self, tipoJanela):
		novaJanela = tipoJanela(self)
		if self.janela is not None:
			self.janela.destroy()
		self.janela = novaJanela
		self.janela.grid(row=1, column=0)

class Métodos(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
		self.b_zdf = Button(self, text="Zeros De Funções", command=lambda: raiz.TrocarJanela(ZdF), fg="white", bg="black", width=2*l)
		self.b_zdp = Button(self, text="Zeros De Polinômios", command=lambda: raiz.TrocarJanela(ZdP), fg="white", bg="black", width=2*l)
		self.b_sl = Button(self, text="Sistemas Lineares", command=lambda: raiz.TrocarJanela(SL), fg="white", bg="black", width=2*l)
		self.b_adf = Button(self, text="Aproximações De Funções", command=lambda: raiz.TrocarJanela(AdF), fg="white", bg="black", width=2*l)
		self.b_inter = Button(self, text="Interpolação", command=self.cNada, fg="white", bg="black", width=2*l)
		self.b_iNum = Button(self, text="Integração Numérica", command=lambda: raiz.TrocarJanela(iNum), fg="white", bg="black", width=2*l)
		# ===== Construir Elementos =====
		self.b_zdf.grid(row=0, column=0, columnspan=2)
		self.b_sl.grid(row=3, column=0, columnspan=2)
		self.b_adf.grid(row=4, column=0, columnspan=2)
		self.b_iNum.grid(row=6, column=0, columnspan=2)
		
		self.b_zdp.grid(row=2, column=0, columnspan=2)
		self.b_inter.grid(row=5, column=0, columnspan=2)

	def cNada(self):
		print("\n\nBotão Apertado\n\n")

app = Aplicativo()
app.title("Métodos Numéricos - UFSM")
app.iconbitmap("Extras/UfsmLogo.ico")
app.mainloop()
