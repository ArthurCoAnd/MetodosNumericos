# Importar Bibliotecas
import os
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from time import time
# Importar Ferramentas
from Interpolação.Métodos.SistemaLinear import SistemaLinear as SL
from Interpolação.Métodos.Lagrange import Lagrange
from Interpolação.Métodos.Newton import Newton
from Interpolação.Ferramentas.Secante import Secante
from Interpolação.Ferramentas.GerarGráfico import GerarGráfico as GG
from Ferramentas.f import f

class Interpolação(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")
		self.métodos_txt = ["Sistema Linear", "Lagrange", "Newton"]

		jNPontos = BoxLayout(size_hint_y=0.1)
		jNPontos.add_widget(Label(text="Número de pontos:"))
		self.nPontos_in = TextInput(halign="center", font_size=20, write_tab=False)
		jNPontos.add_widget(self.nPontos_in)
		jNPontos.add_widget(Button(text="Gerar Pontos", on_press=self.gerarPontos))
		self.add_widget(jNPontos)

		self.jPontos = BoxLayout(orientation="vertical", size_hint_y=0.35)
		self.lPontos = BoxLayout()
		self.jPontos.add_widget(self.lPontos)
		self.add_widget(self.jPontos)

		jMétodos = BoxLayout(orientation="vertical", size_hint_y=0.25)
		jMétodos.add_widget(Label(text="Selecione o método de interpolação:"))
		lJMétodos = BoxLayout()
		for m in range(len(self.métodos_txt)):
			lJMétodos.add_widget(Button(text=self.métodos_txt[m], on_press=partial(self.clique,m)))
		jMétodos.add_widget(lJMétodos)
		self.add_widget(jMétodos)

		jResposta = BoxLayout(orientation="vertical", size_hint_y=0.3)
		linhaResposta = BoxLayout()
		self.método_resposta = Label(text="-", font_size=16, size_hint_x=0.15)
		linhaResposta.add_widget(self.método_resposta)
		self.resposta = Label(text="-", font_size=16)
		linhaResposta.add_widget(self.resposta)
		jResposta.add_widget(linhaResposta)
		linhaExtrapolarX = BoxLayout()
		linhaExtrapolarX.add_widget(Label(text="Interpolar em x = "))
		self.extrapolarX = TextInput(halign="center", font_size=20, write_tab=False)
		linhaExtrapolarX.add_widget(self.extrapolarX)
		linhaExtrapolarX.add_widget(Button(text="Interpolar em x", on_press=partial(self.cliqueExtrapolar,"x")))
		self.respostasExtrapolarX = Label(text="-")
		linhaExtrapolarX.add_widget(self.respostasExtrapolarX)
		jResposta.add_widget(linhaExtrapolarX)
		linhaExtrapolarY = BoxLayout()
		linhaExtrapolarY.add_widget(Label(text="Interpolar em y = "))
		self.extrapolarY = TextInput(halign="center", font_size=20, write_tab=False)
		linhaExtrapolarY.add_widget(self.extrapolarY)
		linhaExtrapolarY.add_widget(Button(text="Interpolar em y", on_press=partial(self.cliqueExtrapolar,"y")))
		self.respostasExtrapolarY = Label(text="-")
		linhaExtrapolarY.add_widget(self.respostasExtrapolarY)
		jResposta.add_widget(linhaExtrapolarY)
		self.add_widget(jResposta)

	def gerarPontos(self, *args, **kwargs):
		self.jPontos.remove_widget(self.lPontos)
		self.lPontos = BoxLayout(orientation="vertical")
		try:
			self.np = int(self.nPontos_in.text)
			self.nPontos_in.background_color = (255,255,255,1)
			self.pontos_in = []
			self.lPontos.add_widget(Label(text="Insira os pontos:", size_hint_y=0.15))
			cP = BoxLayout()
			for c in range(self.np):
				self.pontos_in.append([])
				self.pontos_in[c].append(TextInput(halign="center", font_size=20, write_tab=False))
				self.pontos_in[c].append(TextInput(halign="center", font_size=20, write_tab=False))
				colula = BoxLayout(orientation="vertical")
				colula.add_widget(Label(text=f"x{c}"))
				colula.add_widget(self.pontos_in[c][0])
				colula.add_widget(Label(text=f"y{c}"))
				colula.add_widget(self.pontos_in[c][1])
				cP.add_widget(colula)
			self.lPontos.add_widget(cP)
			self.jPontos.add_widget(self.lPontos)
		except:
			self.nPontos_in.background_color = (255,0,0,1)

	def clique(self, i_método, *args, **kwargs):
		os.system('cls' if os.name == 'nt' else 'clear')
		ti = time()
		self.lerDados()
		self.calcularMétodo(i_método)
		print(f"\n\n\n*** Tempo de execução: {time()-ti}s ***\n\n\n")

	def lerDados(self):
		self.pontos = []
		try:
			for i in range(self.np):
				self.pontos.append([])
				try:
					self.pontos[i].append(float(self.pontos_in[i][0].text))
					self.pontos_in[i][0].background_color = (255,255,255,1)
				except:
					self.pontos_in[i][0].background_color = (255,0,0,1)
				try:
					self.pontos[i].append(float(self.pontos_in[i][1].text))
					self.pontos_in[i][1].background_color = (255,255,255,1)
				except:
					self.pontos_in[i][1].background_color = (255,0,0,1)
		except:
			self.nPontos_in.background_color = (255,0,0,1)

	def calcularMétodo(self, i_método):
		try:
			p = self.pontos.copy()
			self.resposta.text = "f(x) = "
			if i_método == 0:
				self.métodos_Exec = 0
				self.método_resposta.text = "Sistema Linear:"
				resp, self.pap = SL(p)
				self.resposta.text += resp
			if i_método == 1:
				self.métodos_Exec = 1
				self.método_resposta.text = "Lagrange:"
				resp, self.pap = Lagrange(p)
				self.resposta.text += resp
			if i_método == 2:
				self.métodos_Exec = 2
				self.método_resposta.text = "Newton:"
				self.resposta.text, self.método_respostaInv, self.pap = Newton(p)
		except:
			self.métodos_Exec = "-"
			self.método_resposta.text = "-"
			self.resposta.text = "-"

	def cliqueExtrapolar(self, xy, *args, **kwargs):
		sf = self.resposta.text.replace("f(x) = ","").replace(" -","-").replace(" +","+")
		try:
			p = self.pontos.copy()
			self.nPontos_in.background_color = (255,255,255,1)
		except:
			self.nPontos_in.background_color = (255,0,0,1)
		if xy == "x":
			try:
				self.respostasExtrapolarX.text = str(f(float(self.extrapolarX.text),sf))
				self.extrapolarX.background_color = (255,255,255,1)
			except:
				self.respostasExtrapolarX.text = "_"
				self.extrapolarX.background_color = (255,0,0,1)
		if xy == "y":
			if self.métodos_Exec == 2:
				try:
					sf = self.método_respostaInv.replace("f(x) = ","").replace(" -","-").replace(" +","+")
					self.respostasExtrapolarY.text = str(round(f(float(self.extrapolarY.text),sf),7))
					self.extrapolarY.background_color = (255,255,255,1)
				except:
					self.respostasExtrapolarY.text = "-"
					self.extrapolarY.background_color = (255,0,0,1)
			else:
				try:
					sf += f"-({self.extrapolarY.text})"
					self.respostasExtrapolarY.text = str(round(Secante(p,sf),7))
					self.extrapolarY.background_color = (255,255,255,1)
				except:
					self.respostasExtrapolarY.text = "-"
					self.extrapolarY.background_color = (255,0,0,1)

	def Salvar(self):
		d = []
		d.append(self.nPontos_in.text)
		for p in range(self.np):
			d.append(self.pontos_in[p][0].text)
			d.append(self.pontos_in[p][1].text)
		return d

	def Carregar(self, d):
		self.nPontos_in.text = d[0]
		self.gerarPontos()
		di = 1
		for p in range(self.np):
			self.pontos_in[p][0].text = d[di]
			di += 1
			self.pontos_in[p][1].text = d[di]
			di += 1

	def GerarGráfico(self):
		self.lerDados()
		p = self.pontos.copy()
		sf = self.resposta.text.replace("f(x) = ","").replace(" -","-").replace(" +","+")
		GG(p,sf)

	def Passo_Passo(self):
		popup = Popup(title="Passo a Passo", size_hint=(1,1))
		papPop = BoxLayout(orientation="vertical")
		papPop.add_widget(TextInput(text=self.pap, font_size=20, write_tab=False, size_hint=(1,0.9)))
		papPop.add_widget(Button(text="Fechar Passo a Passo", on_press=popup.dismiss, size_hint=(1,0.1)))
		popup.content = papPop
		popup.open()