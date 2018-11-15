#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-



class Basic(object):
	def __init__(self):
		pass
		
	def dismemberment(self, string):
		# Desmembramento de string
		# "1,2,3,4" para [1,2,3,4]
		
		list_ = []
		base = ""
		
		for i, letter in enumerate(string):
			if letter == "," or i == len(string)-1:
				try:
					list_.append(int(base))
					base = ""
				except:
					print("Error ao verificar dados.")
					return []
			else:
				base += letter
				
		return list_
				