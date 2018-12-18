# -*- coding: utf-8 -*-


import os
import sys
import time

try:
	from terminaltables import AsciiTable
	install_terminaltables = True
except:
	install_terminaltables = False
	print("\nModulo terminaltables não está instalado,\n Favor instalar para funcionar corretamente.")
	time.sleep(2)
	
try:
	from termcolor import colored
	install_termcolor = True
except:
	install_termcolor = False
	
def status_table():
	""" Retorna o status do terminaltables"""
	global install_terminaltables
	return install_terminaltables

def status_color():
	""" Retorna o status do termcolor"""
	global install_termcolor
	return install_termcolor

def terminal_size(string, caractere="" ):
	""" Retorna string ajustada com caractere."""
	size_terminal = os.get_terminal_size().columns
	size_string = len(string)
	size = size_terminal - size_string
	return caractere*(size//2)+string+caractere*(size//2)

def tables(matriz, ult_borda= False,title= "", separar_linhas=False):
		""" Recebe a tabela em formatos Matriz e a imprime no terminal."""
		tables_terminal = AsciiTable(matriz)
		tables_terminal.inner_footing_row_border = ult_borda
		tables_terminal.inner_row_border = separar_linhas
		tables_terminal.title = title
		if tables_terminal.ok:
			print(tables_terminal.table)
		else:
			print("Tabela Muito grande, Recue o zoom\nou aumente a janela do terminal!")

def print_color(string, cor):
	"""Adiciona cor no terminal caso install_termcolor for instalado."""
	#string(str, int, float, bool)
	#cor(cores em inglês)
	global install_termcolor
	
	if install_termcolor and sys.platform == "linux":
		print(colored(str(string), cor))
	else:
		print(string)

def clear_():
	""" Limpa o terminal de acordo com a sua plataforma."""
	if sys.platform == "linux":
		os.system("clear")
		os.system("reset")
		
	elif sys.platform == "win32":
		os.system("mode con cols=110 lines=80")
		os.system("cls")