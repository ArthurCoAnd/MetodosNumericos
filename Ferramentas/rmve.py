'''
rmvE - ReMoVedor de Enter

Remove o Char '\ n' da String

Geralmente usada para ler e salvar arquivos
'''
def rmvE(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="\n"):
			p += 1
			continue
		else:
			r += s[p]
		p += 1
	return r