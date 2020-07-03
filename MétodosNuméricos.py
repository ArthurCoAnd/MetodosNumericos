from tkinter import *
# Importar Métodos
from ZeroDeFunções.ZeroDeFunções import ZdF
from AjusteDeFunções.AjusteDeFunções import AdF

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
		self.b_zdf = Button(self, text="Zero De Funções", command=lambda: raiz.TrocarJanela(ZdF), fg="white", bg="black", width=2*l)
		self.b_adf = Button(self, text="Ajuste De Funções", command=lambda: raiz.TrocarJanela(AdF), fg="white", bg="black", width=2*l)
		# ===== Construir Elementos =====
		self.b_zdf.grid(row=0, column=0, columnspan=2)
		self.b_adf.grid(row=1, column=0, columnspan=2)

app = Aplicativo()
app.mainloop()