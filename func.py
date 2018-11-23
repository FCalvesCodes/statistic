# -*- coding: utf-8 -*-

import os

class Basic(object):
	def __init__(self):
		pass
	
	def checker_string(self, string, list_allowed=[",","0","1","2","3","4","5","6","7","8","9"]):
		""" Verifica se a string contém caracteres
				indiferente do desejado. """
		# return False - Para caracteres indesejados
		# return True - não tem caracteres indesejados
				
		if string == None:
			return False
		
		for i in string:
			if i in list_allowed:
				pass 
			else:
				return False
		
		return True
	
	def sum_list(self, list_):
		""" Faz a soma de uma lista com números."""
		# return sum
		sum = 0
		for n in list_:
			sum += n
		return sum
		
	def dismemberment(self, string):
		""" Pega uma string com números separados
			por vírgula e retorna lista com os números 
			separados. """
		# return
		
		list_ = []
		base = ""
		
		if self.checker_string(string):
			pass
		else:
			return
		
		for i, letter in enumerate(string):
			if letter == "," or i == len(string)-1:
				if i == len(string)-1:
					base += letter
					
				try:
					list_.append(int(base))
					base = ""
				except:
					print("Error ao verificar dados.")
					return
			else:
				base += letter
		return list_
	
	
	def terminal_size(self, string, caractere):
		#Calcula o terminal e return string ajustada
		
		size_terminal = os.get_terminal_size().columns
		size_string = len(string)
		size = size_terminal - size_string
		return caractere*(size//2)+string+caractere*(size//2)

 
class Statistic(object):
	
	def __init__(self):
		pass
		
	def rol_raw_data(self, list_):
		"""Coloca uma lista de números em ordem crescente."""
		for x in range(0, len(list_)):
			for y in range(x+1, len(list_)):
				if list_[x] > list_[y]:
					copy = list_[y]
					list_[y] = list_[x]  
					list_[x] = copy
		return list_
		
	def total_amplitude1(self, list_):
		"""Retorna a amplitude total de dados brutos."""
		list_ = self.rol_raw_data(list_)
		return list_[-1] - list_[0]
	
	def total_amplitude2(self, initial, amplitude, quant_fi):
		""" Atualiza a amplitude total de dados agrupados."""
		#initial - int
		#amplititude - int
		#quant_fi - int
		global total_amp
		a = initial
		for i in range(0, quant_fi):
			a+= amplitude
		if str(a-initial).endswith(".0"):
			return round(a - initial)
		else:
			return a-initial
	
	def standard_deviation(self, sum, list_):
		#Desvio padrão - Dados brutos
		a = sum/len(list_)
		#Retorna a raiz
		return a**0.5
		
		
		
		