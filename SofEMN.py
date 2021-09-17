# Importar Bibliotecas
import os
import sys
os.environ["KIVY_NO_CONSOLELOG"] = "1"
from easygui import  fileopenbox, filesavebox
from functools import partial
from kivy.app import App
from kivy.resources import resource_add_path, resource_find
from kivy.uix.actionbar import ActionBar, ActionButton, ActionGroup, ActionPrevious, ActionView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# Importar Métodos
from ZerosDeFunções.ZerosDeFunções import ZerosDeFunções as ZdF
from ZerosDePolinômios.ZerosDePolinômios import ZerosDeFunções as ZdP
from SistemasLineares.SisteamasLineares import SistemasLineares as SL
from AproximaçõeDeFunções.AproximaçõesDeFunções import AproximaçõesDeFunções as AdP
from Interpolação.Interpolação import Interpolação as Inter
from IntegraçãoNumérica.IntegraçãoNumérica import IntegraçãoNumérica as IN
# Importar Ferramentas
from Ferramentas.título import título as ttl

class Aplicativo(App):
	def build(self):
		if getattr(sys, 'frozen', False):
			resource_add_path(sys._MEIPASS)
			resource_add_path(os.path.join(sys._MEIPASS, "Img"))
		try:
			self.icon = "Img/UFSM.ico"
			self.icon = resource_find("UFSM.ico")
		except:
			pass
		self.title = "SofEMN"
		self.métodos_txt = ["Menu", "Zeros de Funções", "Zeros de Polinômios", "Sistemas Lineares", "Aproximações de Funções", "Interpolação", "Integração Numérica"]
		self.método_t = ["self.Métodos()", "ZdF()","ZdP()","SL()", "AdP()", "Inter()", "IN()"]
		self.métodos_b = []

		app = BoxLayout(orientation="vertical")
		app.add_widget(self.Menu())
		self.JanelaMétodos = self.Métodos()
		app.add_widget(self.JanelaMétodos)
		return app

	def TrocarMétodo(self, m, *args, **kwargs):
		os.system('cls' if os.name == 'nt' else 'clear')
		ttl(self.métodos_txt[m],"=")
		self.bMenu.title = self.métodos_txt[m]
		self.root.remove_widget(self.JanelaMétodos)
		self.JanelaMétodos = eval(self.método_t[m])
		self.root.add_widget(self.JanelaMétodos)
		self.bSalvar.on_press = partial(self.Salvar,m)

	def Métodos(self,*args, **kwargs):
		JM = BoxLayout(orientation="vertical")
		for m in range(1,len(self.métodos_txt)):
			if m%2 == 1:
				LM = BoxLayout()
			LM.add_widget(Button(text=self.métodos_txt[m], font_size=20, on_press=partial(self.TrocarMétodo,m)))
			if m%2 == 0:
				JM.add_widget(LM)
		return JM

	def Salvar(self, m, *args, **kwargs):
		if m != 0:
			try:
				dados = self.JanelaMétodos.Salvar()
				nomeArq = filesavebox()
				with open(nomeArq, "w", encoding="utf-8") as arq:
					arq.write(f"{m}")
					for d in dados:
						arq.write(f"\n{d}")
			except:
				pass

	def Carregar(self, *args, **kwargs):
		try:
			nomeArq = fileopenbox()
			dados = []
			with open(nomeArq, "r", encoding="utf-8") as arq:
				m = arq.readline().replace("\n","")
				while True:
					l = arq.readline()
					if not l:
						break
					dados.append(l.replace("\n",""))
			self.TrocarMétodo(int(m))
			self.JanelaMétodos.Carregar(dados)
		except:
			pass

	def GerarGráfico(self, *args, **kwargs):
		try:
			self.JanelaMétodos.GerarGráfico()
		except:
			pass

	def Passo_Passo(self, *args, **kwargs):
		try:
			self.JanelaMétodos.Passo_Passo()
		except:
			pass

	def Menu(self):
		menu = ActionBar()
		menuAV = ActionView()
		self.bMenu = ActionPrevious(title="Menu", with_previous=False, on_press=partial(self.TrocarMétodo,0))
		try:
			self.bMenu.app_icon = "Img/LEMAvoltar.ico"
			self.bMenu.app_icon = resource_find("LEMAvoltar.ico")
		except:
			pass
		menuAV.add_widget(self.bMenu)
		self.menuAQR = ActionGroup(text="Arquivo", mode="spinner")
		self.menuAQR.add_widget(ActionButton(text="Carregar", on_press=self.Carregar))
		self.bSalvar = ActionButton(text="Salvar")
		self.menuAQR.add_widget(self.bSalvar)
		self.menuOPS = ActionGroup(text="Opções", mode="spinner")
		self.menuOPS.add_widget(ActionButton(text="Gerar Gráfico", on_press=self.GerarGráfico))
		# self.menuOPS.add_widget(ActionButton(text="Passo a Passo", on_press=self.Passo_Passo))
		menuAV.add_widget(self.menuOPS)
		menuAV.add_widget(self.menuAQR)
		menu.add_widget(menuAV)
		return menu

if __name__ == "__main__":
	Aplicativo().run()