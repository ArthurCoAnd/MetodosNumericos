from tkinter import *
# Importar Ferramentas
from ZeroDeFunções.dadosZDF import dados
from ZeroDeFunções.Funções.gerarGráfico import gerarGráfico as gG
# Importar Métodos
from ZeroDeFunções.Métodos.Bissecção import bissecção
from ZeroDeFunções.Métodos.PosiçãoFalsa import posiçãoFalsa
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

app=Tk()
app.title("Métodos Numéricos - UFSM")
app.iconbitmap("./Extras/UfsmLogo.ico")

# Tamanho Largura das Colunas
l=30
# Linha das Respostas
lr=14
d = dados(0,1,1e-3,10,"(3*x**3)-(4*x**2)-(10*x)+10","(9*x**2)-(8*x)-10","((3*x**3)-(4*x**2)+10)/10")

# Clique Botão Bissecção
def cBissecção():
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	d.sf = sfE.get()
	d.sdf = sdfE.get()
	d.spf = spfE.get()
	s=bissecção(d)
	Label(app, text=s, width=2*l).grid(row=lr, column=0, columnspan=2)

# Clique Botão Posição Falsa
def cPosiçãoFalse():
	d.sf = sfE.get()
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	s=posiçãoFalsa(d)
	Label(app, text=s, width=2*l).grid(row=lr, column=0, columnspan=2)

# Clique Botão Ponto Fixo
def cPontoFixo():
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	d.sf = sfE.get()
	d.sdf = sdfE.get()
	d.spf = spfE.get()
	s=pontoFixo(d)
	Label(app, text=s, width=2*l).grid(row=lr, column=0, columnspan=2)

# Clique Botão Newton Raphson
def cNewtonRaphson():
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	d.sf = sfE.get()
	d.sdf = sdfE.get()
	d.spf = spfE.get()
	s=newtonRaphson(d)
	Label(app, text=s, width=2*l).grid(row=lr, column=0, columnspan=2)

# Clique Botão Secante
def cSecante():
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	d.sf = sfE.get()
	d.sdf = sdfE.get()
	d.spf = spfE.get()
	s=secante(d)
	Label(app, text=s, width=2*l).grid(row=lr, column=0, columnspan=2)

def cgfr():
	d.a = float(aE.get())
	d.b = float(bE.get())
	d.e = float(eE.get())
	d.kmax = float(kmaxE.get())
	d.sf = sfE.get()
	d.sdf = sdfE.get()
	d.spf = spfE.get()
	s=secante(d)
	gG(d)

# ===== Definir Elementos =====
	# Textos
título = Label(app, text="Zero de Funções", width=(2*l))
sftxt = Label(app, text="Função - f(x)", width=l)
sdftxt = Label(app, text="Derivada da Função - f'(x)", width=l)
spftxt = Label(app, text="Função Ponto Fixo", width=l)
atxt = Label(app, text="Intervalo Inicial - a/xk", width=l)
btxt = Label(app, text="Intervalo Final - b/xkm", width=l)
etxt = Label(app, text="Erro - e ", width=l)
kmaxtxt = Label(app, text="Interações Máximas", width=l)

	# Botões
bgfr = Button(app, text="Gerar Gráfico", command=cgfr, fg="white", bg="black", width=(2*l))
bBissecção = Button(app, text="Bissecção", command=cBissecção, fg="white", bg="black", width=(2*l))
bPosiçãoFalsa = Button(app, text="Posição Falsa", command=cPosiçãoFalse, fg="white", bg="black", width=(2*l))
bPontoFixo = Button(app, text="Ponto Fixo", command=cPontoFixo, fg="white", bg="black", width=(2*l))
bNewtonRaphson = Button(app, text="Newton-Raphson", command=cNewtonRaphson, fg="white", bg="black", width=(2*l))
bSecante = Button(app, text="Secante", command=cSecante, fg="white", bg="black", width=(2*l))

	# Entradas
sfE = Entry(app, width=l)
sdfE = Entry(app, width=l)
spfE = Entry(app, width=l)
aE = Entry(app, width=l)
bE = Entry(app, width=l)
eE = Entry(app, width=l)
kmaxE = Entry(app, width=l)

# ===== Preset de valores para testes rápidos =====
aE.insert(END,d.a)
bE.insert(END,d.b)
eE.insert(END,d.e)
kmaxE.insert(END,d.kmax)
sfE.insert(END,d.sf)
sdfE.insert(END,d.sdf)
spfE.insert(END,d.spf)

# ===== Construir Elementos =====
	# Textos
título.grid(row=0 ,column=0, columnspan=2)
sftxt.grid(row=1 ,column=0)
sdftxt.grid(row=2 ,column=0)
spftxt.grid(row=3 ,column=0)
atxt.grid(row=4 ,column=0)
btxt.grid(row=5 ,column=0)
etxt.grid(row=6 ,column=0)
kmaxtxt.grid(row=7 ,column=0)

	# Botões
bBissecção.grid(row=8 ,column=0, columnspan=2)
bPosiçãoFalsa.grid(row=9 ,column=0, columnspan=2)
bPontoFixo.grid(row=10 ,column=0, columnspan=2)
bNewtonRaphson.grid(row=11 ,column=0, columnspan=2)
bSecante.grid(row=12 ,column=0, columnspan=2)
bgfr.grid(row=13 ,column=0, columnspan=2)

	# Entradas
sfE.grid(row=1 ,column=1)
sdfE.grid(row=2 ,column=1)
spfE.grid(row=3 ,column=1)
aE.grid(row=4 ,column=1)
bE.grid(row=5 ,column=1)
eE.grid(row=6 ,column=1)
kmaxE.grid(row=7 ,column=1)

app.mainloop()