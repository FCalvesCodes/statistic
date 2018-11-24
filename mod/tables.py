# -*- coding: utf-8 -*-


import time

try:
	from terminaltables import AsciiTable
except:
	print("Instale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)


class TablesTerminal():
	def __init__(self):
		self.is_terminaltables = True
		
		try:
			self.tables_terminal = AsciTable
		except:
			self.is_terminaltables
			
		
	
			
		
		
		
	def is_terminal(self):
		"""Returna True ou Falso."""
		return self.is_terminaltables
		
	def tables(self, data, ult_borda= False,title= ""):
		""" Recebe a tabela em formatos
			Matriz."""
		self.tables_terminal = AsciiTable(data)
		self.tables_terminal.inner_footing_row_border = ult_borda
		self.tables_terminal.padding_left = 2
		self.tables_terminal.title = title
		if self.tables_terminal.ok:
			print(self.tables_terminal.table)
		else:
			print("Tabela não pode ser visualizada, \n Recua o zoom do terminal e tente novamente.")
	


