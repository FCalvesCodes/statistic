# coding:utf-8
#
from func import Basic, RawData, GroupedData
import os
import time

basic = Basic()
rawdata = RawData()
groupeddata = GroupedData()


_list = []
_sum = 0
_arithmetic_mean = 0

#xi - "x-barra"
_xi_x = []
_sum_xi_x = 0

#xi - "x-barra"^2
xi_x_2 = []
_sum_xi_x_2 = 0


#fi
fi = []
sum_fi = 0

#xi
xi = []
sum_xi =0

#xi.fi
xi_fi = []
sum_xi_fi = 0

#




commands = ["[1] - Adicionar dados brutos", \
							"[2] - Amplitude Total", \
							"[3] - Desvio Médio simples",\
							"[4] - Desvio Padrão",\
							"[5] - Adicionar fi e xi (Dados agrupados)",\
							"[6] - Aprender calcular xi (Dados agrupados)",\
							"[7] - Mostrar tabela completa (Dados Agrupados)",\
							"[6] - Sair"]

commands2 = ["[1] - Dados brutos", "Dados Agrupados"]


# ------------------------------------------------------------------------------
def input_error(string):
	""" Tratamento de error no while principal. """
	global commands
	n = len(commands)
	
	while 1:
		try:
			x = int(input(string))
			if x > n:
				print("Opção Invalida.")
			else:
				break
		except:
			print("Opção invalida.")
	return x

# ------------------------------------------------------------------------------
def arithmetic_mean(indice):
	#Média aritmética
	global _list
	global _sum
		
	for n in _list[indice]:
		_sum += n
	m = round(_sum/len(_list[indice]), 2)
	print(f"\n Tirando a Média aritmética: {m}\n")
	_sum = 0
	return m
	
# ------------------------------------------------------------------------------
def input_list():
	""" Responsavel em receber os dados da
			lista. """
	global _list
	
	list_ = []
	
	n = int(input("Quantidade de dados: "))
	modo = input("Inteiro/Real: ")
	
	for i in range(1, n+1):
		
		if modo.lower() == "inteiro":
			while 1:
				try:
					d = int(input("{} - : ".format(i)))
					list_.append(d)
					break
				except:
					print("Dados inválidos. ")
					
		elif modo.lower() == "real":
			while 1:
				try:
					d = float(input("{} - : ".format(i)))
					list_.append(d)
					break
				except:
					print("Dados inválidos. ")
					
	_list.append(list_)
	print(_list[-1])
	input("...")

# ------------------------------------------------------------------------------
def print_list():
	""" Imprime os dados armazenados em _list
			com seu indice na lista. """
	global _list
	for indice, list_ in enumerate(_list):
		print("[{}]-- {}".format(indice, list_))
		
# ------------------------------------------------------------------------------
def total_amplitude():
	#Amplitude total dados brutos
	global _list
	
	if len(_list) != 0:
		print_list()
		ind = int(input("Indice: "))
		
		print("\nColocando a lista em ordem.")
		_list_ = basic.ordination(_list[ind])
	
		at = rawdata.total_amplitude(_list_)
	
		print(f"Amplitude total é {at}")
		input("...")
	else:
		print("Não foi criado dados ainda.")
		time.sleep(1)

def total_amplitude():
	#Amplitude total Dados Agrupados
	pass
	
# ------------------------------------------------------------------------------
def simple_mean_deviation():
	#Desvio médio simples
	global _list
	global _arithmetic_mean
	global _xi_xi
	global _sum_xi_x
	
	if len(_list) > 0:
		print_list()
	
		ind = int(input("Indice: "))
	
		_arithmetic_mean = round(arithmetic_mean(ind), 2)
		
		
		#Cria uma lista xi-x
		for i, xi in enumerate(_list[ind]):
			_xi_x.append(round(abs(xi - _arithmetic_mean), 4))
			print(f"x{i+1}: {xi} - {_arithmetic_mean} = {round(abs(xi - _arithmetic_mean), 4)}")
		
		#Faz a somatória 
		for  E in _xi_x:
			_sum_xi_x+= E
		print(f"\n\tSomatória: {round(_sum_xi_x, 2)}")
		
		dms = round(_sum_xi_x/len(_list[ind]), 2)
		print(f"Desvio médio simples é {dms}")
		_xi_x = []
		_sum_xi_x = 0
		_arithmetic_mean = 0
		input("...")
	else:
		print("Não foi criado dados ainda.")

# ------------------------------------------------------------------------------
def standard_deviation():
	#Desvio padrão
	global _list
	global _xi_x_2
	global _sum_xi_x_2
	
	if len(_list) > 0:
		print_list()
	
		ind = int(input("Indice: "))
	
		_arithmetic_mean = round(arithmetic_mean(ind), 2)
		
		
		#Cria uma lista xi-x
		for i, xi in enumerate(_list[ind]):
			x = abs(xi - _arithmetic_mean)
			_xi_x_2.append(round(x**2, 2))
			print(f"x{i+1}: ({xi} - {_arithmetic_mean})²= {round(x**2, 2)}")
		
		#Faz a somatória 
		for  E in _xi_x_2:
			_sum_xi_x_2 += E
		_sum_xi_x_2 = round(_sum_xi_x_2, 2)
		
		print(f"\n\tSomatória: {_sum_xi_x_2}")
		a = round(_sum_xi_x_2/len(_list[ind]), 2)
		b = round(a**0.5, 2)
		print(f"\n\tDesvio Padrão é {b}.")
		_sum_xi_x_2 = 0
		_xi_x_2 = []
		
		input("...")
	
	else:
		print("Não foi criado dados ainda.")
	
	

while 1:
	os.system("clear")
	#Apresentação das opções
	for command in commands:
		print(command)
		
	x = str(input_error("Opção: "))
	
	if x == "1":
		input_list()
	elif x == "2":
		total_amplitude()
	elif x == "3":
		simple_mean_deviation()
	elif x == "4":
		standard_deviation()
	elif x == "5":
		pass
	elif x == "6":
		break
	
		
	
	



		
		
