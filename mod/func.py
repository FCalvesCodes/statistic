# -*- coding: utf-8 -*-

from decimal import Decimal
import os
import math

class Basic(object):
	def __init__(self):
		self.decimal = 2
	
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

		
	def truncate_(self, f, n):
		'''Truncates/pads a float f to n decimal places without rounding'''
		s = '{}'.format(f)
		if 'e' in s or 'E' in s:
			return '{0:.{1}f}'.format(f, n)
		i, p, d = s.partition('.')
		return Decimal('.'.join([i, (d+'0'*n)[:n]]))
	
	def sum_list(self, list_):
		""" Faz a soma de uma lista com números."""
		if len(list_) < 2:
			return 0
		sum = Decimal('0')
		for n in list_:
			sum += self.truncate_(n, self.decimal)
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
		return math.sqrt(a)
		
		
		
		