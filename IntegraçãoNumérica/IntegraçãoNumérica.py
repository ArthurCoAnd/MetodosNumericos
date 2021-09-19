# Importar Bibliotecas
import os
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from time import time
from random import randint
# Importar Ferramentas
from IntegraçãoNumérica.Métodos.Trapézio import Trapézio
from IntegraçãoNumérica.Métodos.Simpson13 import Simpson13
from IntegraçãoNumérica.Métodos.Simpson38 import Simpson38
from IntegraçãoNumérica.Ferramentas.GerarGráfico import GerarGráfico as GG
from Ferramentas.f import f

class IntegraçãoNumérica(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")		
		self.txt_métodos = ["Trapézio", "1/3 de Simpson", "3/8 de Simpson"]
		self.txt_entradas = ["Função - f(x)", "Derivada segunda da função - f''(x)", "Derivada quarta da função - f''''(x)", "Limite inferior - a", "Limite superior - b", "Subdivisões - m"]
		self.t_dados = ["sf", "sdsf", "sdqf", "a", "b", "m"]
		self.dados = {"sf": "", "sdsf": "", "sdqf": "", "a": "", "b": "", "m": ""}
		self.txt_resultados = ["Método", "Integral", "Erro"]
		self.t_resultado = ["met", "Int", "er"]
		self.resultado = {"met": "-", "Int": "-", "er": "-"}

		self.entradas = []
		for e in range(len(self.txt_entradas)):
			linha = BoxLayout()
			linha.add_widget(Label(text=self.txt_entradas[e], size_hint_x=0.5))
			self.entradas.append(TextInput(halign="center", font_size=20, write_tab=False, size_hint_x=0.5))
			linha.add_widget(self.entradas[e])
			self.add_widget(linha)
		
		self.add_widget(Label(text="Escolha o método para encontrar a raiz da função:"))
		self.seleção = []
		l1 = BoxLayout()
		for s in range(len(self.txt_métodos)):
			l1.add_widget(Button(text=self.txt_métodos[s], on_press=partial(self.clique,s)))
		self.add_widget(l1)

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
		self.resultado = {"met": "-", "Int": "-", "er": "-"}
		for i in range(len(self.dados)):
			self.dados[self.t_dados[i]] = self.entradas[i].text.replace(",",".")

	# Tentar Converter os dados das entradas para seus respectivos formatos	
	def txt2numb(self):
		# Verificar se é uma função válida
		try:
			f(randint(-100,100),self.dados["sf"])
			self.entradas[0].background_color = (255,255,255,1)
		except:
			self.entradas[0].background_color = (255,255,0,1)
		# Verificar se é uma derivada segunda válida
		try:
			f(randint(-100,100),self.dados["sdsf"])
			self.entradas[1].background_color = (255,255,255,1)
		except:
			self.entradas[1].background_color = (255,255,0,1)
		# Verificar se é uma derivada quarta válida
		try:
			f(randint(-100,100),self.dados["sdqf"])
			self.entradas[2].background_color = (255,255,255,1)
		except:
			self.entradas[2].background_color = (255,255,0,1)
		# Verificar ser a - b - m são válidos
		for i in range(3,6):
			try:
				if i != 5:
					self.dados[self.t_dados[i]] = float(self.dados[self.t_dados[i]])
					self.entradas[i].background_color = (255,255,255,1)
				else:
					self.dados[self.t_dados[i]] = int(self.dados[self.t_dados[i]])
					self.entradas[i].background_color = (255,255,255,1)
			except:
				self.entradas[i].background_color = (255,0,0,1)

	def calcularMétodo(self, i_método):
		try:
			d = self.dados.copy()
			if i_método == 0:
				self.resultado["met"] = "Trapézio"
				self.resultado["Int"], self.resultado["er"], self.pap = Trapézio(d)
			elif i_método == 1:
				self.resultado["met"] = "1/3 de Simpson"
				self.resultado["Int"], self.resultado["er"], self.pap = Simpson13(d)
			else:
				self.resultado["met"] = "3/8 de Simpson"
				self.resultado["Int"], self.resultado["er"], self.pap = Simpson38(d)
		except:
			self.resultado = {"met": "-", "Int": "-", "er": "-"}

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