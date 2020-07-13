import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.dadosZDF import dados
# Importando Funções
from ZeroDeFunções.Funções.f import f

def validarIntervalo(d):
	título("Validar Intervalo", '=')
	resposta = False

	# if alternativo para melhor validação, mas que está danto problema
	# if( ( (f(d.a,d.sf)*f(d.b,d.sf)) < 0 ) and ( (f(d.a,d.sdf)*f(d.b,d.sdf)) > 0 ) ):
	if( (f(d.a,d.sf)*f(d.b,d.sf)) < 0 ):
		print("Válido em - [%f]:[%f]"%(d.a,d.b))
		resposta = True
	else:
		print("Inválido em - [%f]:[%f]"%(d.a,d.b))

	return resposta