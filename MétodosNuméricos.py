from tkinter import *
# Importar Métodos
from ZeroDeFunções.ZeroDeFunções import ZdF
from AjusteDeFunções.AjusteDeFunções import AdF

# Tamanho Largura das Colunas
l=30

class Menu:
	def __init__(self, raiz):
		janela = Frame(raiz)
		janela.grid(row=0, column=0)

		self.t_título = Label(janela, text="Menu", width=(2*l))
		self.t_título.grid(row=0, column=0)

		self.b_ZDF = Button(janela, text="Zero de Funções", command=self.c_zdf, fg="white", bg="black", width=(2*l))
		self.b_ZDF.grid(row=1, column=0)

		self.b_ADF = Button(janela, text="Ajuste de Funções", command=self.c_adf, fg="white", bg="black", width=(2*l))
		self.b_ADF.grid(row=3, column=0)

	def c_zdf(self):
		janela = ZdF(raiz)

	def c_adf(self):
		janela = AdF(raiz)

raiz=Tk()
raiz.title("Métodos Numéricos - UFSM")
raiz.iconbitmap("./Extras/UfsmLogo.ico")

app = Menu(raiz)

raiz.mainloop()