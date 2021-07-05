# Importar Bibliotecas
from tkinter import *
import os
import sys
# Importar Métodos
from ZeroDeFunções.ZeroDeFunções import ZdF
from ZeroDePolinômios.ZeroDePolinômios import ZdP
from SistemasLinears.SistemasLineares import SL
from AjusteDeFunções.AjusteDeFunções import AdF
from Interpolação.Interpolação import Inter
from IntegraçãoNumérica.IntegraçãoNumérica import iNum

# Tamanho Largura das Colunas
l=35

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)

class Aplicativo(Tk):
	def __init__(self):
		Tk.__init__(self)
		# ===== Definir Elementos =====
		self.t_título = Label(self, text="Menu", width=2*l)
		self.b_voltar = Button(self, text="Voltar", command=lambda: self.VoltarMenu(Métodos), fg="white", bg="DodgerBlue4")
		# ===== Construir Elementos =====
		self.t_título.grid(row=0, column=0, columnspan=2)
		# self.b_voltar.grid(row=0, column=0, sticky=W)
		self.janela = None
		self.VoltarMenu(Métodos)

	def TrocarJanela(self, tipoJanela):
		self.t_título.grid_forget()
		self.b_voltar.grid(row=0, column=0, sticky=W)
		novaJanela = tipoJanela(self)
		if self.janela is not None:
			self.janela.destroy()
		self.janela = novaJanela
		self.janela.grid(row=1, column=0)

	def VoltarMenu(self, tipoJanela):
		self.t_título.grid(row=0, column=0, columnspan=2)
		self.b_voltar.grid_forget()
		novaJanela = tipoJanela(self)
		if self.janela is not None:
			self.janela.destroy()
		self.janela = novaJanela
		self.janela.grid(row=1, column=0)

class Métodos(Frame):
	def __init__(self, raiz):
		Frame.__init__(self, raiz)
		# ===== Definir Elementos =====
		self.b_zdf = Button(self, text="Zeros de funções", command=lambda: raiz.TrocarJanela(ZdF), fg="white", bg="DodgerBlue4", width=2*l)
		self.b_zdp = Button(self, text="Zeros de polinômios", command=lambda: raiz.TrocarJanela(ZdP), fg="white", bg="DodgerBlue4", width=2*l)
		self.b_sl = Button(self, text="Sistemas lineares", command=lambda: raiz.TrocarJanela(SL), fg="white", bg="DodgerBlue4", width=2*l)
		self.b_adf = Button(self, text="Aproximações de funções", command=lambda: raiz.TrocarJanela(AdF), fg="white", bg="DodgerBlue4", width=2*l)
		self.b_inter = Button(self, text="Interpolação", command=lambda: raiz.TrocarJanela(Inter), fg="white", bg="DodgerBlue4", width=2*l)
		self.b_iNum = Button(self, text="Integração numérica", command=lambda: raiz.TrocarJanela(iNum), fg="white", bg="DodgerBlue4", width=2*l)
		# ===== Construir Elementos =====
		self.b_zdf.grid(row=0, column=0, columnspan=2)
		self.b_zdp.grid(row=2, column=0, columnspan=2)
		self.b_sl.grid(row=3, column=0, columnspan=2)
		self.b_adf.grid(row=4, column=0, columnspan=2)
		self.b_inter.grid(row=5, column=0, columnspan=2)
		self.b_iNum.grid(row=6, column=0, columnspan=2)
		
	def cNada(self):
		print("\n\nBotão Apertado\n\n")

if __name__ == "__main__":
	app = Aplicativo()
	app.resizable(False, False)
	app.title("SofEMN")
	try:
		app.iconbitmap("Extras/UfsmLogo.ico")
	except:
		try:
			app.iconbitmap(resource_path("UfsmLogo.ico"))
		except:
			pass
	app.mainloop()
