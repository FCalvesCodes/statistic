


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

	
		
	