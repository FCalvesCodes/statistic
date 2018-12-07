# -*- coding: utf-8 -*-


import os

try:
	from terminaltables import AsciiTable
	install_terminaltables = True
except:
	install_terminaltables = False
	print("\nModulo terminaltables não está instalado,\n Favor instalar para funcionar corretamente.")
	time.sleep(2)
	
def status():
	""" Retorna o status do terminaltables"""
	global install_terminaltables
	return install_terminaltables

def terminal_size(string, caractere="" ):
	""" Retorna string ajustada com o tamanho do terminal."""
	size_terminal = os.get_terminal_size().columns
	size_string = len(string)
	size = size_terminal - size_string
	return caractere*(size//2)+string+caractere*(size//2)

def tables(matriz, ult_borda= False,title= "", separar_linhas=False):
		""" Recebe a tabela em formatos Matriz."""
		tables_terminal = AsciiTable(matriz)
		tables_terminal.inner_footing_row_border = ult_borda
		tables_terminal.inner_row_border = separar_linhas
		tables_terminal.title = title
		if tables_terminal.ok:
			print(tables_terminal.table)
		else:
			print("Tabela Muito grande, Recue o zoom\nou aumente a janela do terminal!")