# -*- coding: utf-8 -*-

from decimal import Decimal
import os
import math

class Statistic(object):
	
	def __init__(self):
		
		#Recebe o xmin e xmax dos dados
		self.xmax = 0
		self.xmin = 0
		
	def rol_raw_data(self, list_):
		"""Faz a ordenação de uma lista númerica(crescente)."""
		list_copy = list_[:]
		for x in range(0, len(list_copy)):
			for y in range(x+1, len(list_copy)):
				if list_copy[x] > list_copy[y]:
					copy = list_copy[y]
					list_copy[y], list_copy[x] = list_copy[x], copy
		return list_copy
		
	def total_amplitude1(self, list_1):
		"""Retorna a amplitude total de dados brutos."""
		list = self.rol_raw_data(list_1)
		self.xmin = list[0]
		self.xmax = list[-1]
		return list[-1] - list[0]
	
	def total_amplitude2(self, initial, amplitude, quant_fi):
		""" Atualiza a amplitude total de dados agrupados."""
		#initial - int
		#amplititude - int
		#quant_fi - int
		global total_amp
		a = initial
		for i in range(0, quant_fi):
			a+= amplitude
		
		self.xmin = self.tr(initial)
		self.xmax = self.tr(a)
		
		if str(a-initial).endswith(".0"):
			return round(a - initial)
		else:
			return a-initial
	
	def standard_deviation(self, sum, list_):
		#Desvio padrão - Dados brutos
		a = sum/len(list_)
		#Retorna a raiz
		return math.sqrt(a)
		
	def tr(self, obj):
		""" Retira as casas decimais"""
		if type(obj) == list:
			new_list = []
			for n in obj:
				if str(n).endswith(".0") or str(n).endswith(".00") or str(n).endswith(".000") or str(n).endswith(".0000") or str(n).endswith(".00000"):
					n = round(n)
					new_list.append(n)
				else:
					new_list.append(n)
					
			return new_list
		else:
			if str(obj).endswith(".0") or str(obj).endswith(".00") or str(obj).endswith(".000") or str(obj).endswith(".0000") or str(obj).endswith(".00000"):
				return round(obj)
			else:
				return obj
		
		
		
		
		