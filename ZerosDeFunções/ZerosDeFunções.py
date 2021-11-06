# Importar Bibliotecas
import os
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from random import randint
from time import time
# Importar Ferramentas
from ZerosDeFunções.Métodos.Bissecção import Bissecção
from ZerosDeFunções.Métodos.PosiçãoFalsa import PosiçãoFalsa
from ZerosDeFunções.Métodos.NewtonRaphson import NewtonRaphson
from ZerosDeFunções.Métodos.Secante import Secante
from ZerosDeFunções.Ferramentas.GerarGráfico import GerarGráfico as GG
from Ferramentas.f import f


class ZerosDeFunções(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")
		self.txt_métodos = ["Bissecção", "Posição Falsa", "Newton-Raphson", "Secante"]
		self.txt_entradas = ["Função - f(x)", "Derivada da função - f'(x)", "Limite inferior - a", "Limite superior - b", "Ponto inicial - x0", "Ponto inicial - x1", "Epsilon - ε", "Máximo de iterações - kmax"]
		self.t_dados = ["sf", "sdf", "a", "b", "x0", "x1", "e", "km"]
		self.dados = {"sf": "", "sdf": "", "a": "", "b": "", "x0": "", "x1": "", "e": "", "km": ""}
		self.txt_resultados = ["Método", "Iterações", "Raiz - xk", "Valor de f(xk)", "Erro"]
		self.t_resultado = ["met", "k", "xk", "fxk", "erro"]
		self.resultado = {"met": "", "k": "-", "xk": "-", "fxk": "-", "erro": "-"}

		self.entradas = []
		for e in range(len(self.txt_entradas)):
			linha = BoxLayout()
			linha.add_widget(Label(text=self.txt_entradas[e]))
			self.entradas.append(TextInput(halign="center", font_size=20, write_tab=False))
			linha.add_widget(self.entradas[e])
			self.add_widget(linha)
		
		self.add_widget(Label(text="Escolha o método para encontrar a raiz da função:"))
		self.seleção = []
		l1 = BoxLayout()
		l2 = BoxLayout()
		for s in range(len(self.txt_métodos)):
			if s < 2:
				l1.add_widget(Button(text=self.txt_métodos[s], on_press=partial(self.clique,s)))
			else:
				l2.add_widget(Button(text=self.txt_métodos[s], on_press=partial(self.clique,s)))
		self.add_widget(l1)
		self.add_widget(l2)

		self.resultados = []
		l1 = BoxLayout()
		l2 = BoxLayout()
		for r in range(len(self.txt_resultados)):
			l1.add_widget(Label(text=self.txt_resultados[r]))
			self.resultados.append(Label(text="-"))
			l2.add_widget(self.resultados[r])
		self.add_widget(l1)
		self.add_widget(l2)
		
	def clique(self, i_método, *args, **kwargs):
		os.system('cls' if os.name == 'nt' else 'clear')
		ti = time()
		self.lerDados()
		self.txt2numb()
		self.calcularMétodo(i_método)
		self.alterarRespostas()
		print(f"\n\n\n*** Tempo de execução: {time()-ti}s ***\n\n\n")

	def lerDados(self):
		self.resultado = {"k": "-", "xk": "-", "fxk": "-", "erro": "-"}
		for i in range(len(self.dados)):
			self.dados[self.t_dados[i]] = self.entradas[i].text

	# Tentar Converter os dados das entradas para seus respectivos formatos	
	def txt2numb(self):
		# Verificar se é uma função válida
		try:
			f(randint(-100,100),self.dados["sf"])
			self.entradas[0].background_color = (255,255,255,1)
		except:
			self.entradas[0].background_color = (255,255,0,1)
		# Verificar se é uma derivada válida
		try:
			f(randint(-100,100),self.dados["sdf"])
			self.entradas[1].background_color = (255,255,255,1)
		except:
			self.entradas[1].background_color = (255,255,0,1)
		# Verificar ser a - b - x0 - x1 - e são válidos
		for i in range(2,7):
			try:
				self.dados[self.t_dados[i]] = float(self.dados[self.t_dados[i]])
				self.entradas[i].background_color = (255,255,255,1)
			except:
				self.entradas[i].background_color = (255,0,0,1)
		# Verificar se k é valido
		try:
			self.dados[self.t_dados[7]] = int(self.dados[self.t_dados[7]])
			self.entradas[7].background_color = (255,255,255,1)
		except:
			self.entradas[7].background_color = (255,0,0,1)

	def calcularMétodo(self, i_método):
		try:
			d = self.dados.copy()
			if i_método == 0:
				self.resultado["met"] = "Bissecção"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados, self.pap = Bissecção(d)
			elif i_método == 1:
				self.resultado["met"] = "Posição Falsa"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados, self.pap = PosiçãoFalsa(d)
			elif i_método == 2:
				self.resultado["met"] = "Newton-Raphson"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados, self.pap = NewtonRaphson(d)
			else:
				self.resultado["met"] = "Secante"
				self.resultado["k"], self.resultado["xk"], self.resultado["fxk"], self.resultado["erro"], resultados, self.pap = Secante(d)
		except:
			self.resultado = {"met": "-", "k": "-", "xk": "-", "fxk": "-", "erro": "-"}

	def alterarRespostas(self):
		for r in range(len(self.txt_resultados)):
			self.resultados[r].text = str(self.resultado[self.t_resultado[r]])

	def Salvar(self):
		d = []
		for i in range(len(self.dados)):
			d.append(self.entradas[i].text)
		return d

	def Carregar(self, d):
		for i in range(len(self.dados)):
			self.entradas[i].text = d[i]

	def GerarGráfico(self):
		self.lerDados()
		self.txt2numb()
		d = self.dados.copy()
		GG(d)

	def Passo_Passo(self):
		popup = Popup(title="Passo a Passo", size_hint=(1,1))
		papPop = BoxLayout(orientation="vertical")
		papPop.add_widget(TextInput(text=self.pap, font_size=20, write_tab=False, size_hint=(1,0.9)))
		papPop.add_widget(Button(text="Fechar Passo a Passo", on_press=popup.dismiss, size_hint=(1,0.1)))
		popup.content = papPop
		popup.open()