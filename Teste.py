from tkinter import *
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa

app=Tk()
app.title("Métodos Numéricos - UFSM")
app.iconbitmap("./Extras/UfsmLogo.ico")

# Tamanho Largura das Colunas
l=25

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
título = Label(app, text="Zero de Funções", width=(2*l))
sftxt = Label(app, text="Função - f(x)", width=l)
atxt = Label(app, text="Intervalo Inicial - a/xk", width=l)
btxt = Label(app, text="Intervalo Final - b/xkm", width=l)
etxt = Label(app, text="Erro - e ", width=l)
kmaxtxt = Label(app, text="Interações Máximas", width=l)
	# Botões
bBissecção = Button(app, text="Bissecção", command=cBissecção, fg="white", bg="black", width=(2*l))
bPosiçãoFalsa = Button(app, text="Posição Falsa", command=cPosiçãoFalse, fg="white", bg="black", width=(2*l))

	# Entradas
sfE = Entry(app, width=l)
aE = Entry(app, width=l)
bE = Entry(app, width=l)
eE = Entry(app, width=l)
kmaxE = Entry(app, width=l)

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