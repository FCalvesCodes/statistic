


class Basic(object):
	
	def __init__(self):
		pass
	
	def ordination(self, _list):
		"""Faz a ordenação de uma lista 'Dados Brutos'."""
		for x in range(0, len(_list)):
			for y in range(x+1, len(_list)):
				
				if _list[x] > _list[y]:
					copy = _list[y]
					_list[y] = _list[x]
					_list[x] = copy
		return _list

class RawData(object):
	#Dados brutos
	def __init__(self):
		pass
	
	def total_amplitude(self, _list):
		#Amplitude total
		return _list[-1] - _list[0]
	

class GroupedData(object):
	#Dados Agrupados
	def __init__(self):
		pass

	def calculate_xi_fi(self, list_xi, list_fi):
		#xi.fi
		pass
	def calculate_xi_x(self, list_xi, x):
		#|xi-'x-barra'|
		pass
		
	def calculate_fi_x_2(self, list_fi, list_xi_x):
		#fi.|xi-'x-barra'
		pass
	
	def calculate_fi_xi_x_2(self, list_fi, list_fi_x_2):
		#fi.(xi-'x-barra')²
		pass
