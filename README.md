# SofEMN
Software para Ensino de Métodos Numéricos

<a href="https://www.ufsm.br/laboratorios/lema"><img src="./Img/LEMA.png" height="100"></a>
<img src="./Img/UFSM.png" height="100">

# Sobre o Software
Desenvolvido como projeto de pesquisa e extensão pelo Laboratório de Estudos em Matemática Aplicada (LEMA), este software visa ser uma ferramenta para auxílio no ensino e aprendizado da matéria de Métodos Numéricos e Computacionais. Foi utilizado o plano de ensino dessa matéria da Universidade Federal de Santa Maria Campus Cachoeira do Sul (UFSM-CS) com os seguintes métodos desenvolvidos:

## Menu
<img src="./Img/Prints/Menu.png">

## Métodos Numéricos Desenvolvidos
- Zeros de Funções
- Zeros de Polinômios
- Sistemas Lineares
- Aproximações de Funções
- Interpolação
- Integração Numérica

# Dependências
Desenvolvido utilizando Python 3.9.7
### <a href="https://kivy.org/#home">Kivy</a>
```
pip install -U kivy
```
### <a href="https://matplotlib.org/stable/index.html">Matplotlib</a>
```
pip install -U matplotlib
```
### <a href="https://www.scipy.org">Scipy</a>
```
pip install -U scipy
```
### <a href="https://numpy.org">Numpy</a>
```
pip install -U numpy
```
### <a href="https://github.com/robertlugg/easygui">EasyGUI</a>
```
pip install -U easygui
```
### Ctrl C + Ctrl V
```
pip install -U kivy matplotlib scipy numpy easygui
```
# Compilar
```
pyinstaller --noconfirm --onefile --windowed --icon "Img/UFSM.ico" --add-data "Img;Img/" "./SofEMN.py"
```
# Compilar - Versão Teste
```
pyinstaller --noconfirm --onefile --icon "Img/UFSM.ico" --add-data "Img;Img/" "./SofEMN.py"
```
## Dependências:
### <a herf="https://www.pyinstaller.org/">Pyinstaller</a>
```
pip install -U pyinstaller
```