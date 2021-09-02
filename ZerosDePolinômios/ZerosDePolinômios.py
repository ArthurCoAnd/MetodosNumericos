# Importar Bibliotecas
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# Importar Ferramentas
from ZerosDePolinômios.Métodos.BirgeVieta import BirgeVieta
from ZerosDePolinômios.Métodos.NewtonRaphson import NewtonRaphson

class ZerosDeFunções(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")
		self.txt_métodos = ["Birge-Vieta", "Newton-Rapshon"]
		self.txt_resultados = ["Método", "Iterações", "Raiz - xk", "Valor de f(xk)", "Erro"]
		self.t_resultado = ["met", "k", "xk", "fxk", "erro"]
		self.resultado = {"met": "", "k": "-", "xk": "-", "fxk": "-", "erro": "-"}
		self.txt_dados = ["Ponto inicial - x0", "Epsilon - ε", "Máximo de iterações - kmax"]
		self.t_dados = ["sf", "x0", "e", "km"]
		self.dados = {"sf": "", "x0": "", "e": "", "km": ""}
		self.polinômio_in = []
		self.polinômio = []
		self.gp = 0
		
		l = BoxLayout()
		c = BoxLayout(orientation="vertical")
		c.add_widget(Label(text="Grau do polinômio:"))
		self.grau = TextInput(halign="center", font_size=20, write_tab=False)
		c.add_widget(self.grau)
		l.add_widget(c)
		l.add_widget(Button(text="Gerar Polinômio", on_press=self.gerarPolinômio))
		self.add_widget(l)

		self.linhaPolinômio = BoxLayout(orientation="vertical")
		self.linhaPolinômioTxt = BoxLayout()
		self.linhaPolinômio.add_widget(self.linhaPolinômioTxt)
		self.linhaPolinômioEnt = BoxLayout()
		self.linhaPolinômio.add_widget(self.linhaPolinômioEnt)
		self.add_widget(self.linhaPolinômio)

		l = BoxLayout()
		self.dandos_in = []
		for d in range(len(self.t_dados)-1):
			c = BoxLayout(orientation="vertical")
			c.add_widget(Label(text=self.txt_dados[d]))
			self.dandos_in.append(TextInput(halign="center", font_size=20, write_tab=False))
			c.add_widget(self.dandos_in[d])
			l.add_widget(c)
		self.add_widget(l)

		self.add_widget(Label(text="Escolha o método para calcular a raiz do polinômio:"))
		l = BoxLayout()
		for b in range(len(self.txt_métodos)):
			l.add_widget(Button(text=self.txt_métodos[b], on_press=partial(self.clique,b)))
		self.add_widget(l)

		self.resultados = []
		l1 = BoxLayout()
		l2 = BoxLayout()
		for r in range(len(self.txt_resultados)):
			l1.add_widget(Label(text=self.txt_resultados[r]))
			self.resultados.append(Label(text="-"))
			l2.add_widget(self.resultados[r])
		self.add_widget(l1)
		self.add_widget(l2)

	def gerarPolinômio(self, *args, **kwargs):
		self.linhaPolinômio.remove_widget(self.linhaPolinômioTxt)
		self.linhaPolinômio.remove_widget(self.linhaPolinômioEnt)
		self.polinômio_in = []
		try:
			self.gp = int(self.grau.text)
			self.grau.background_color = (255,255,255,1)
			for p in range(self.gp+1):
				self.polinômio_in.append(TextInput(halign="center", font_size=20, write_tab=False))
			self.linhaPolinômioTxt = BoxLayout()
			self.linhaPolinômioEnt = BoxLayout()
			for p in range(self.gp,-1,-1):
				self.linhaPolinômioTxt.add_widget(Label(text=f"a{p}"))
				self.linhaPolinômioEnt.add_widget(self.polinômio_in[p])
			self.linhaPolinômio.add_widget(self.linhaPolinômioTxt)
			self.linhaPolinômio.add_widget(self.linhaPolinômioEnt)
		except:
			self.grau.background_color = (255,0,0,1)

	def clique(self, i_método, *args, **kwargs):
		self.lerDados()
		self.calcularMétodo(i_método)
		self.alterarRespostas()

	def lerDados(self):
		self.resultado = {"met": "-", "k": "-", "xk": "-", "fxk": "-", "erro": "-"}
		self.polinômio = []
		for i in range(self.gp+1):
			try:
				self.polinômio.append(float(self.polinômio_in[i].text))
				self.polinômio_in[i].background_color = (255,255,255,1)
			except:
				try:
					self.polinômio_in[i].background_color = (255,0,0,1)
				except:
					pass
		try:
			self.dados["sf"] = self.poli2str()
		except:
			pass
		for i in range(len(self.dados)):
			try:
				if i != 3:
					self.dados[self.t_dados[i+1]] = float(self.dandos_in[i].text)
				else:
					self.dados[self.t_dados[i+1]] = int(self.dandos_in[i].text)
				self.dandos_in[i].background_color = (255,255,255,1)
			except:
				try:
					self.dandos_in[i].background_color = (255,0,0,1)
				except:
					pass

	def calcularMétodo(self, i_método):
		try:
			p = self.polinômio.copy()
			d = self.dados.copy()
			if i_método == 0:
				self.resultado["met"] = "Birge Vieta"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados = BirgeVieta(p,d)
			elif i_método == 1:
				self.resultado["met"] = "Newton-Raphson"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados = NewtonRaphson(p,d)
		except:
			self.resultado = {"met": "-", "k": "-", "xk": "-", "fxk": "-", "erro": "-"}

	def alterarRespostas(self):
		for r in range(len(self.txt_resultados)):
			self.resultados[r].text = str(self.resultado[self.t_resultado[r]])

	def poli2str(self):
		sf = ""
		for p in range(self.gp+1):
			sf += f"+({self.polinômio_in[p].text}*x**{p})"
		return sf

	def Salvar(self):
		d = []
		d.append(self.grau.text)
		for i in range(len(self.polinômio_in)):
			d.append(self.polinômio_in[i].text)
		for i in range(len(self.dandos_in)):
			d.append(self.dandos_in[i].text)
		return d
	
	def Carregar(self, d):
		self.grau.text = d[0]
		self.gerarPolinômio()
		for i in range(self.gp+1):
			self.polinômio_in[i].text = d[i+1]
		for i in range(len(self.dandos_in)):
			self.dandos_in[i].text = d[i+self.gp+2]