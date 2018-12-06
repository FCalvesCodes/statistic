# -*- coding: utf-8 -*-
#Modo auditória para checar variáveis (Em desenvolvimento)

class ModoAudit(object):
	def __init__(self, obj):
		
		#Recebe a instância da classe statistic
		self.obj = obj
		
	def features(self, list_):
		#Mostra uma lista.
		for i in range(0, len(list_)):
			print(f"{list_[i]}[{i}]")
			
	
	
	


