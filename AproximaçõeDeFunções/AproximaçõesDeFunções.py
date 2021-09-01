# Importar Bibliotecas
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# Importar Ferramentas
from AproximaçõeDeFunções.Métodos.FunçãoLinear import FunçãoLinear as FL
from AproximaçõeDeFunções.Métodos.FunçãoQuadradaVérticeOrigem import FunçãoQuadradaVérticeOrigem as FQVO
from AproximaçõeDeFunções.Métodos.FunçãoQuadrada import FunçãoQuadrada as FQ
from AproximaçõeDeFunções.Ferramentas.Secante import Secante
from AproximaçõeDeFunções.Ferramentas.GerarGráfico import GerarGráfico as GG
from Ferramentas.f import f

class AproximaçõesDeFunções(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")
		self.métodos_txt = ["Função Linear", "Função Quadrada"]

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
		jMétodos.add_widget(Label(text="Selecione o método de aproximação:"))
		lJMétodos = BoxLayout()
		for m in range(len(self.métodos_txt)):
			lJMétodos.add_widget(Button(text=self.métodos_txt[m], on_press=partial(self.clique,m)))
		jMétodos.add_widget(lJMétodos)
		self.add_widget(jMétodos)

		jResposta = BoxLayout(orientation="vertical", size_hint_y=0.3)
		linhaResposta = BoxLayout()
		self.resposta = Label(text="-", font_size=20)
		linhaResposta.add_widget(self.resposta)
		jResposta.add_widget(linhaResposta)
		linhaExtrapolarX = BoxLayout()
		linhaExtrapolarX.add_widget(Label(text="Extrapolar em x = "))
		self.extrapolarX = TextInput(halign="center", font_size=20, write_tab=False)
		linhaExtrapolarX.add_widget(self.extrapolarX)
		linhaExtrapolarX.add_widget(Button(text="Extrapolar em x", on_press=partial(self.cliqueExtrapolar,"x")))
		self.respostasExtrapolarX = Label(text="-")
		linhaExtrapolarX.add_widget(self.respostasExtrapolarX)
		jResposta.add_widget(linhaExtrapolarX)
		linhaExtrapolarY = BoxLayout()
		linhaExtrapolarY.add_widget(Label(text="Extrapolar em y = "))
		self.extrapolarY = TextInput(halign="center", font_size=20, write_tab=False)
		linhaExtrapolarY.add_widget(self.extrapolarY)
		linhaExtrapolarY.add_widget(Button(text="Extrapolar em y", on_press=partial(self.cliqueExtrapolar,"y")))
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
		self.lerDados()
		self.calcularMétodo(i_método)

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
				self.resposta.text += FL(p)
			if i_método == 1:
				self.resposta.text += FQ(p)
		except:
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
			try:
				sf += f"-({self.extrapolarY.text})"
				self.respostasExtrapolarY.text = str(Secante(p,sf))
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