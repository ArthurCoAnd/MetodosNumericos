# Classe com padrão de resposta para usar nos Métodos de Zeros de Funções
class Resposta(Frame):
	def __init__(self, raiz, k,xk,fxk,e,r):
		Frame.__init__(self, raiz)
		self.k = k
		self.xk = xk
		self.fxk = fxk
        self.e = e
        self.r = r

		# ===== Definir Elementos =====
			# Textos
			self.t_calculos = Label(self, text=r)
			# Botões
			# Entradas

		# ===== Construir Elementos =====
			# Textos
			# Botões
			# Entradas