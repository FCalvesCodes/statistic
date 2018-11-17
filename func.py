#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Basic(object):
	def __init__(self):
		pass
	
	def checker_string(self, string, list_allowed=[",","0","1","2","3","4","5","6","7","8","9"]):
		#Verifica se na string contém caracteres permitidos
		if string == None:
			return False
		
		for i in string:
			if i in list_allowed:
				pass 
			else:
				return
		
		return True
		
	def dismemberment(self, string):
		# Desmembramento de string
		# "1,2,3,4" para [1,2,3,4]
		
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
		
	def total_amplitude1(self, list_):
		#retorna a amplitude da classe para dados brutos em rol
		return list_[-1] - list_[0]
		
	def rol_raw_data(self, list_):
		#Coloca uma list de números em ordem crescente
		for x in range(0, len(list_)):
			for y in range(x+1, len(list_)):
				if x > y:
					copy = list_[y]
					list_[y] = list_[x]    #list_[y], list_[x] = list_[x], list_[y]
					list_[x] = copy
					
		return list_
		
		
		