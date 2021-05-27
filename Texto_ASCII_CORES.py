# _______     _________ _    _  ____  _   _ 
#|  __ \ \   / /__   __| |  | |/ __ \| \ | |
#| |__) \ \_/ /   | |  | |__| | |  | |  \| |
#|  ___/ \   /    | |  |  __  | |  | | . ` |
#| |      | |     | |  | |  | | |__| | |\  |
#|_|      |_|     |_|  |_|  |_|\____/|_| \_|
# Esse programa é apenas para diversão
# Basicamente ele transformar qualquer texto em desenho ascii
# Está bem explicado o programa.
# Feito por Jonathan Jonas
#=================================================
from pyfiglet import Figlet # Responsavel por transformar em ascii
from termcolor import cprint # Responsavel em deixa colorido
from os import system # Responsavel em dar comandos no cmd
from time import sleep # Responsavel por dar um pequeno delay 
#=================================================

system('cls') # Limpa o terminal
Texto_digitado = str(input("Digite alguma coisa: "))
Cor_digitada = str(input("Escolha uma cor [R,G,B]:")).lower()
fonte = Figlet(font='banner3-D') # Tipo de formatação da fonte que será usado.

system('cls') # Limpa o terminal
if Cor_digitada == 'r':
    cprint(fonte.renderText(Texto_digitado), 'red') # Formata o que foi escrito para a cor vermelha
if Cor_digitada == 'g':
    cprint(fonte.renderText(Texto_digitado), 'green')# Formata o que foi escrito para a cor verde
if Cor_digitada == 'b':
    cprint(fonte.renderText(Texto_digitado), 'blue')# Formata o que foi escrito para a cor azul

sleep(1)