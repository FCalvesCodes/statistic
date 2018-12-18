# -*- coding: utf-8 -*-
#Modo auditória para checar variáveis (Em desenvolvimento)

class ModoAudit(object):
	def __init__(self, obj):
		
		#Recebe a instância da classe statistic
		self.obj= obj
		
	def print_dada(self):
		print("self.amplitude:", self.obj.amplitude)
		print("self.initial:", self.obj.initial)
		
		print("self.xmin:", self.obj.xmin)
		print("self.xmax:",self.obj.xmax)
		
		print("self.x1:", self.obj.x1)
		
		
		print("self.sum_xi:", self.obj.sum_xi)
		print("self.sum_fi:", self.obj.sum_fi)
		print("self.sum_fi_xi:", self.obj.sum_fi_xi)
		print("self.sum_x3:", self.obj.sum_x3)
		print("self.sum_x4:", self.obj.sum_x4)
		print("self.sum_fi_x3:", self.obj.sum_fi_x3)
		print("self.sum_fi_x4:", self.obj.sum_fi_x4)
		
		
		print("self.quant_xi:", self.obj.quant_xi)
		print("self.quant_fi:", self.obj.quant_fi)
		
		print("self.decimal:", self.obj.decimal)
		print("self.total_amplitude:", self.obj.total_amplitude)
		print("self.initial:", self.obj.initial)
		
		
		print(self.obj.list_xi)
		print(self.obj.list_fi)
		print(self.obj.list_fi_xi)
		print(self.obj.list_x2)
		print(self.obj.list_x3)
		print(self.obj.list_x4)
		print(self.obj.list_fi_x3)
		print(self.obj.list_fi_x4)
		print(self.obj.list_fri)
		print(self.obj.list_Fi)
		print(self.obj.list_Fri)
		
		#Amostral e populacional
		print(self.obj.sample)
		print(self.obj.populational)

		#Dados Agrupados - Moda
		print(self.obj.lmo)
		print(self.obj.indice)
		print(self.obj.value)
		print(self.obj.ffant)
		print(self.obj.fpost)
		print(self.obj.delta_2)
		print(self.obj.delta_1)
		print(self.obj.amplitude)
		print(self.obj.modal)
		
		#Configurações para visualizar tabela de frequencia
		#0 - fri%     1- Fi        2 - Fri%     3 - xi     4 - xi.fi
		print(self.obj.list_config)
		
		#Configura os dados do menu configurações
		print(self.obj.modo_agrupados)
	
	


