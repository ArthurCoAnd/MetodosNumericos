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
from SistemasLineares.Métodos.Cramer import Cramer
from SistemasLineares.Métodos.EliminaçãoDeGauss import EliminaçãoDeGauss as EdG
from SistemasLineares.Métodos.FatoraçãoLU import FatoraçãoLU as LU
from SistemasLineares.Métodos.FatoraçãoCholesky import FatoraçãoCholesky as Cholesky
from SistemasLineares.Métodos.GaussJacobi import GaussJacobi
from SistemasLineares.Métodos.GaussSeidel import GaussSeidel

class SistemasLineares(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(orientation="vertical")
		self.txt_métodos = ["Cramer", "Eliminação de Gauss", "Fatoração LU", "Fatoração Cholosky", "Gauss-Jacobi", "Gauss-Seidel"]
		
		# Topo
		jtopo = BoxLayout(orientation="vertical", size_hint_y=0.3)
		topo = BoxLayout()
		esq = BoxLayout(orientation="vertical", size_hint_x=0.4)
		esq.add_widget(Label(text="Número de Variáveis:"))
		self.nvariáveis = TextInput(halign="center", font_size=20, write_tab=False)
		esq.add_widget(self.nvariáveis)
		esq.add_widget(Button(text="Gerar Variáveis", on_press=self.gerarVariáveis))
		topo.add_widget(esq)

		dir = BoxLayout(orientation="vertical", size_hint_x=0.6)
		dir.add_widget(Label(text="Selecione o método para resolver o sistema:"))
		for m in range(len(self.txt_métodos)):
			if m%3 == 0:
				dirL = BoxLayout()
			dirL.add_widget(Button(text=self.txt_métodos[m], on_press=partial(self.clique,m)))
			if m%3 == 1:
				dir.add_widget(dirL)
		topo.add_widget(dir)
		jtopo.add_widget(topo)
		self.add_widget(jtopo)

		# Variáveis dos Coeficientes
		self.janelaVariáveis = BoxLayout(orientation="vertical", size_hint_y=0.6)
		self.linhasVariáveis = BoxLayout(orientation="vertical")
		self.janelaVariáveis.add_widget(self.linhasVariáveis)
		self.add_widget(self.janelaVariáveis)

		# Variaveis Vetor Inicial
		self.janelaVetor = BoxLayout(orientation="vertical", size_hint_y=0.2)
		self.linhaVetor = BoxLayout(orientation="vertical")
		self.janelaVetor.add_widget(self.linhaVetor)
		self.add_widget(self.janelaVetor)

		# Resposta
		self.janelaResposta = BoxLayout(orientation="vertical", size_hint_y=0.15)
		self.linhaResposta = BoxLayout(orientation="vertical")
		self.janelaResposta.add_widget(self.linhaResposta)
		self.add_widget(self.janelaResposta)

	def gerarVariáveis(self, *args, **kwargs):
		# Variáveis dos Coeficientes
		self.janelaVariáveis.remove_widget(self.linhasVariáveis)
		self.linhasVariáveis = BoxLayout(orientation="vertical")
		self.linhasVariáveis.add_widget(Label(text="Insira os coeficiêntes do sistema:", size_hint_y=0.2))
		self.variáveis_in = []
		try:
			self.nv = int(self.nvariáveis.text)
			self.nvariáveis.background_color = (255,255,255,1)
			for l in range(self.nv):
				linha = BoxLayout()
				self.variáveis_in.append([])
				for c in range(self.nv+1):
					coluna = BoxLayout(orientation="vertical")
					if c != self.nv:
						coluna.add_widget(Label(text=f"a{l}{c}"))
					else:
						coluna.add_widget(Label(text=f"b{l}"))
					self.variáveis_in[l].append(TextInput(halign="center", font_size=20, write_tab=False))
					coluna.add_widget(self.variáveis_in[l][c])
					linha.add_widget(coluna)
				self.linhasVariáveis.add_widget(linha)
			self.janelaVariáveis.add_widget(self.linhasVariáveis)
		except:
			self.nvariáveis.background_color = (255,0,0,1)
		# Variaveis Vetor Inicial
		self.janelaVetor.remove_widget(self.linhaVetor)
		self.linhaVetor = BoxLayout(orientation="vertical")
		self.linhaVetor.add_widget(Label(text="Insira o vetor inicial:", size_hint_y=0.35))
		try:
			linha = BoxLayout()
			for c in range(self.nv):
				linha.add_widget(Label(text=f"x({c})"))
			linha.add_widget(Label(text="Epsilon - ε"))
			self.linhaVetor.add_widget(linha)	
			linha = BoxLayout()
			self.vetor_in = []
			for c in range(self.nv):
				self.vetor_in.append(TextInput(halign="center", font_size=20, write_tab=False))
				linha.add_widget(self.vetor_in[c])
			self.erro_in = TextInput(halign="center", font_size=20, write_tab=False)
			linha.add_widget(self.erro_in)
			self.linhaVetor.add_widget(linha)
			self.janelaVetor.add_widget(self.linhaVetor)
		except:
			self.nvariáveis.background_color = (255,0,0,1)
		# Respotas
		self.janelaResposta.remove_widget(self.linhaResposta)
		self.linhaResposta = BoxLayout(orientation="vertical")
		self.respostaMétodo = Label(text="Método - ")
		self.linhaResposta.add_widget(self.respostaMétodo)
		try:
			linha = BoxLayout()
			for c in range(self.nv):
				linha.add_widget(Label(text=f"x{c}"))
			self.linhaResposta.add_widget(linha)	
			linha = BoxLayout()
			self.resposta_txt = []
			for c in range(self.nv):
				self.resposta_txt.append(Label(text="-"))
				linha.add_widget(self.resposta_txt[c])
			self.linhaResposta.add_widget(linha)
			self.janelaResposta.add_widget(self.linhaResposta)
		except:
			self.nvariáveis.background_color = (255,0,0,1)

	def clique(self, i_método, *args, **kwargs):
		try:
			os.system('cls' if os.name == 'nt' else 'clear')
			ti = time()
			self.lerDados()
			self.calcularMétodo(i_método)
			self.alterarRespostas()
			print(f"\n\n\n*** Tempo de execução: {time()-ti}s ***\n\n\n")
		except:
			self.nvariáveis.background_color = (255,0,0,1)

	def lerDados(self):
		self.variáveis = []
		self.vetor = []
		try:
			for l in range(self.nv):
				self.variáveis.append([])
				for c in range(self.nv+1):
					try:
						self.variáveis[l].append(float(self.variáveis_in[l][c].text))
						self.variáveis_in[l][c].background_color = (255,255,255,1)
					except:
						self.variáveis_in[l][c].background_color = (255,0,0,1)
			for c in range(self.nv):
				try:
					self.vetor.append(float(self.vetor_in[c].text))
					self.vetor_in[c].background_color = (255,255,255,1)
				except:
					self.vetor_in[c].background_color = (255,0,0,1)
			try:
				self.erro = float(self.erro_in.text)
				self.erro_in.background_color = (255,255,255,1)
			except:
				self.erro_in.background_color = (255,0,0,1)
		except:
			pass

	def calcularMétodo(self, i_método):
		try:
			va = self.variáveis.copy()
			ve = self.vetor.copy()
			if i_método == 0:
				self.respostaMétodo.text = "Método - Cramer"
				self.resposta, self.pap = Cramer(va)
			elif i_método == 1:
				self.respostaMétodo.text = "Método - Eliminação de Gauss"
				self.resposta, self.pap = EdG(va)
			elif i_método == 2:
				self.respostaMétodo.text = "Método - Fatoração LU"
				self.resposta, self.pap = LU(va)
			elif i_método == 3:
				self.respostaMétodo.text = "Método - Fatoração Cholesky"
				self.resposta, self.pap = Cholesky(va)
			elif i_método == 4:
				self.respostaMétodo.text = "Método - Gauss-Jacobi"
				self.resposta, self.pap = GaussJacobi(va, ve, self.erro)
			elif i_método == 5:
				self.respostaMétodo.text = "Método - Gauss-Seidel"
				self.resposta, self.pap = GaussSeidel(va, ve, self.erro)
		except:
			self.respostaMétodo.text = "Método - "
			self.resposta = []
			for r in range(self.nv):
				self.resposta.append("-")

	def alterarRespostas(self):
		try:
			for r in range(self.nv):
				self.resposta_txt[r].text = str(round(self.resposta[r],7))
		except:
			for r in range(self.nv):
				self.resposta_txt[r].text = "-"

	def Salvar(self):
		d = []
		d.append(self.nvariáveis.text)
		for l in range(self.nv):
			for c in range(self.nv+1):
				d.append(self.variáveis_in[l][c].text)
		for i in range(self.nv):
			d.append(self.vetor_in[i].text)
		d.append(self.erro_in.text)
		return d

	def Carregar(self, d):
		self.nvariáveis.text = d[0]
		self.gerarVariáveis()
		p = 1
		for l in range(self.nv):
			for c in range(self.nv+1):
				self.variáveis_in[l][c].text = d[p]
				p += 1
		for i in range(self.nv):
			self.vetor_in[i].text = d[p]
			p += 1
		self.erro_in.text = d[p]

	def Passo_Passo(self):
		popup = Popup(title="Passo a Passo", size_hint=(1,1))
		papPop = BoxLayout(orientation="vertical")
		papPop.add_widget(TextInput(text=self.pap, font_size=20, write_tab=False, size_hint=(1,0.9)))
		papPop.add_widget(Button(text="Fechar Passo a Passo", on_press=popup.dismiss, size_hint=(1,0.1)))
		popup.content = papPop
		popup.open()