# -*- coding: utf-8 -*-

from decimal import Decimal
import os
import math

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
		
		
		
		