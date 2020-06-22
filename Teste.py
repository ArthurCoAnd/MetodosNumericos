from tkinter import *
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa

app=Tk()

# Clique Botão Bissecção
def cBissecção():
	sf = sfE.get()
	a = float(aE.get())
	b = float(bE.get())
	e = float(eE.get())
	kmax = float(kmaxE.get())
	bissecção(a,b,e,kmax,sf)

# Clique Botão Posição Falsa
def cPosiçãoFalse():
	sf = sfE.get()
	a = float(aE.get())
	b = float(bE.get())
	e = float(eE.get())
	kmax = float(kmaxE.get())
	posiçãoFalsa(a,b,e,kmax,sf)

# ===== Definir Elementos =====
	# Textos
título = Label(app, text="Zero de Funções")
sftxt = Label(app, text="Função")
atxt = Label(app, text="Intervalo Inicial")
btxt = Label(app, text="Intervalo Final")
etxt = Label(app, text="Erro")
kmaxtxt = Label(app, text="Interações Máximas")
	# Botões
bBissecção = Button(app, text="Bissecção", command=cBissecção, fg="white", bg="black")
bPosiçãoFalsa = Button(app, text="Posição Falsa", command=cPosiçãoFalse, fg="white", bg="black")

	# Entradas
sfE = Entry(app)
aE = Entry(app)
bE = Entry(app)
eE = Entry(app)
kmaxE = Entry(app)

# ===== Construir Elementos =====
	# Textos
título.grid(row=0 ,column=0, columnspan=2)
sftxt.grid(row=1 ,column=0)
atxt.grid(row=2 ,column=0)
btxt.grid(row=3 ,column=0)
etxt.grid(row=4 ,column=0)
kmaxtxt.grid(row=5 ,column=0)

	# Botões
bBissecção.grid(row=6 ,column=0, columnspan=2)
bPosiçãoFalsa.grid(row=7 ,column=0, columnspan=2)

	# Entradas
sfE.grid(row=1 ,column=1)
aE.grid(row=2 ,column=1)
bE.grid(row=3 ,column=1)
eE.grid(row=4 ,column=1)
kmaxE.grid(row=5 ,column=1)

app.mainloop()