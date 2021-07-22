'''
fts - Function To String

Transforma Chars ** para ^ em Strings de Funções

Geralmente usada para ler e salvar arquivos
'''
def fts(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="*"):
			if(s[p+1]=="*"):
				r += "^"
				p += 1
			else:
				p += 1
				continue
		else:
			r += s[p]
		p += 1
	return r