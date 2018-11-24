#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

""" 							Arquivo Principal
	Esse script foi projetado e testado no terminal termux android
		Não Sei se vai dar problema em outros terminais.
		
		Modo de uso:
			Instale o termux no seu celular
			Codigos a digitar no termux:
					$ pkg install python python-dev coreutils git
					$ pip install terminaltables
					$ git https://github.com/FelipeAlmeid4/dispersion-measure.git
					$ cd dispersion-measure
					$ python main.py
"""

from decimal import Decimal
from func import Basic, Statistic
import os
import time
import sys


is_terminaltables = True

try:
	from terminaltables import AsciiTable
	
except:
	print("Instale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)
	is_terminaltables = False
	

basic = Basic()
statistic = Statistic()

modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------

xmin = 0
xmax = 0

amplitude = 0  # Amplitude da classe
x1= 0			      #Média aritmética

sum_xi_fi = 0
sum_x3 = 0
sum_x4 = 0
sum_xi = 0
sum_fi = 0
sum_fi_x3 = 0
sum_fi_x4 = 0


quant_xi = 0 	   #len(list_xi)
quant_fi = 0       #len(list_fi)

decimal = 2
total_amp = 0   #Amplitude total Xmin da 1°, Xmax da ultima Classe.
initial = 0			#Xmin da primeira classe




list_x2 = []		  #xi - "x-barra"
list_x3 = []		  #|xi - "x-barra"|
list_x4 = []		  #(xi - "x-barra")²
list_xi = []		   # xi
list_fi = []		   # fi
list_xi_fi = []     # xi.fi
list_fi_x3 = []	#fi.|xi - "x-barra"|
list_fi_x4 = []	#fi.(xi - "x-barra")²

# É dados brutos
is_raw_data = False




commands1 = ["[1] - Dados Brutos",\
								"[2] - Dados Agrupados",\
								"[3] - Sobre",\
								"[4] - Informações",\
								"[5] - Configurar Casa Decimal",\
							    "[6] - Sair"]

commands2 = ["[1] - Amplitude total",\
								"[2] - Desvio médio simples",\
								"[3] - Desvio padrão",\
								"[4] - Todos(1, 2, 3)",\
								"[5] - Configurar Casa Decimal",\
								"[6] - Retornar"]



abount = ["Amplitude Total\nDesvio médio simples\nDesvio padrão\n        github: FelipeAlmeid4."]

#--------------------------------------------------------------------

				


def d(x):
	""" Convert float em Decimal."""
	return Decimal(x)


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    #https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return Decimal('.'.join([i, (d+'0'*n)[:n]]))
	
	
def clear_():
	""" Limpa o terminal de acordo com a
		sua plataforma."""
	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
		
# ----------------------------------------------------

def tables(data, ult_borda= False,title= ""):
	""" Recebe a tabela em formatos
			Matriz."""
	tables_terminal = AsciiTable(data)
	tables_terminal.inner_footing_row_border = ult_borda
	tables_terminal.padding_left = 2
	tables_terminal.title = title
	if tables_terminal.ok:
		print(tables_terminal.table)
	else:
		print("Tabela não pode ser visualizada, \n Recua o zoom do terminal e tente novamente.")
	
#------------------------------------------------------
	
def arithmetic_mean(list_, grouped_data=False):
	""" Faz a operação para obter a média 
		aritimética  e guarda na var x1."""
	global x1
	global decimal
	global sum_fi
	global list_fi
	
	total = basic.sum_list(list_)
	
	if grouped_data:
		#Para dados Agrupados
		sum_fi = round(basic.sum_list(list_fi), decimal)
		quantidade = sum_fi
	else:
		quantidade = len(list_)
	x1 = round(total/quantidade, decimal)

# ------------------------------------------------------------------------------

def standard_deviation():
	"""Desvio padrão para dados brutos."""
	global is_terminaltables
	global decimal
	
	global sum_x2
	global sum_xi
	
	global list_xi
	global list_x2
	global list_x3
	global list_x4
	
	
	global quant_xi
	
	
	l = []
	
	#Zerar as listas
	list_x2, list_x3, list_x4 = [], [], []
	
	#Escopo da tabela
	l.append(["xi", "xi-'x-barra'","|xi-'x-barra'|", "(xi-'x-barra')²"])
	
	for x in range(0, quant_xi):
		
		#xi-'x-barra'
		list_x2.append(truncate(truncate(list_xi[x], decimal) - truncate(x1, decimal), decimal))
		# |xi-'x-barra'|
		list_x3.append(truncate(abs(truncate(list_xi[x], decimal) - truncate(x1, decimal)), decimal))
		#(xi-'x-barra')²
		list_x4.append(truncate(truncate(list_x3[x], decimal)**2,decimal))
		
		#True caso o terminaltables foi instalado
		if is_terminaltables:
			l.append([list_xi[x], list_x2[x], list_x3[x], list_x4[x]])
		else:
			pass
		
	#Recebe a soma de todas list
	sum_x3 = round(basic.sum_list(list_x3), decimal)
	sum_x4 = round(basic.sum_list(list_x4), decimal)
	sum_xi = round(basic.sum_list(list_xi), decimal)
	
	if is_terminaltables:
		l.append([sum_xi, "Σ",sum_x3, sum_x4])
		tables(l, True,"Dados brutos - desvio padrão")
	else:
		print("Instale o módulo terminaltables para mais detalhes.\n")
	
	#Recebe o resultado da raiz
	dt = statistic.standard_deviation(sum_x4,list_x4)
		
	print(f"\n\tDesvio padrão é √({sum_x4}/{len(list_x4)}) = {round(dt, decimal)}")

# ---------------------------------------------------------------------

def standard_deviation2():
	"""Desvio padrão para dados Agrupados."""
	global is_terminaltables
	global decimal
	
	global x1
	
	global sum_fi
	global sum_xi
	global sum_xi_fi
	global sum_x2
	global sum_x3
	global sum_x4
	global sum_fi_x4
	
	global list_xi
	global list_fi
	global list_xi_fi
	global list_x2
	global list_x3
	global list_x4
	global list_fi_x4
	
	global quant_fi
	
	
	list_x2, list_x3, list_x4, list_fi_x4 = [], [], [], []
	
	l = []
	#Escopo da tabela
	l.append(["fi", "xi","xi.fi","xi-'x-barra'","(xi-'x-barra')²", "fi.(xi-'x-barra')²"])
	
	
	for x in range(0, quant_fi):
		#xi-'x-barra'
		list_x2.append(truncate(truncate(list_xi[x], decimal) - truncate(x1, decimal), decimal))
		#|xi-'x-barra'|
		list_x3.append(truncate(abs(truncate(list_xi[x], decimal) - truncate(x1, decimal)), decimal))
		#(xi-'x-barra')²
		list_x4.append(truncate(truncate(list_x3[x], decimal)**2, decimal))
		#fi
		list_fi_x4.append(truncate(truncate(list_fi[x], decimal)*truncate(list_x4[x], decimal), decimal))
		
		
		#True caso o terminaltables foi instalado
		if is_terminaltables:
		
			l.append([list_fi[x], list_xi[x], list_xi_fi[x], list_x2[x], list_x4[x], list_fi_x4[x]])
	
	#Recebe as somas das list
	sum_xi = d(basic.sum_list(list_xi))
	sum_fi = d(basic.sum_list(list_fi))
	sum_x3 = d(basic.sum_list(list_x3))
	sum_x4 = d(basic.sum_list(list_x4))
	sum_fi_x4 = d(basic.sum_list(list_fi_x4))
	sum_xi_fi = d(basic.sum_list(list_xi_fi))
	
	if is_terminaltables:
		l.append([sum_fi, sum_xi,sum_xi_fi, "Σ", sum_x4, sum_fi_x4])
		tables(l, True,"Dados Agrupados - desvio padrão")
	else:
		print("Instale o módulo terminaltables para mais detalhes.\n")
		
	#Recebe o resultado da raiz
	dt = sum_fi_x4/sum_fi
	dt = dt**d(0.5)
		
	print(f"\n\tDesvio padrão é √({sum_fi_x4}/{sum_fi}) = {round(dt, decimal)}")
	
# -------------------------------------------------------------------------------

def average_mean_deviation1():
	""" Desvio médio simples dados brutos,
		Apenas imprime ou cria um table."""
		
	global is_terminaltables
	global decimal
	
	global sum_xi
	global sum_x3
	
	global list_x2
	global list_x3
	global list_x4
	
	l = []
	
	#Escopo da tabela
	l.append(["xi", "xi-'x-barra'","|xi-'x-barra'|"])
	
	#Zera as listas
	list_x2, list_x3, list_x4 = [], [], []
	
	for x in range(0, quant_xi):
		#x-'x-barra'
		list_x2.append(round(list_xi[x] - x1, decimal))
		#|x-'x-barra'|
		list_x3.append(abs(round(list_xi[x] - x1, decimal)))
		#(x-'x-barra')²
		list_x4.append(round(list_x3[x]**2, decimal))
		
		#True caso o terminaltables foi instalado
		if is_terminaltables:
			l.append([list_xi[x], list_x2[x], list_x3[x]])
		else:
			pass
	
	#Recebem a somas das list
	sum_x3 = round(basic.sum_list(list_x3), decimal)
	sum_xi = round(basic.sum_list(list_xi), decimal)
	
	
	if is_terminaltables:
		l.append([sum_xi, "    Σ",sum_x3])
		tables(l, True, "Dados Brutos - Desvio médio simples")
	else:
		print("Instale o módulo terminaltables para mais detalhes.\n")
	
	print(f"\n\t Desvio médio simples é ({sum_x3}/{len(list_x3)}) = {round(sum_x3/len(list_x3), decimal)}")
		
# ----------------------------------------------------------------------------

def average_mean_deviation2():
	""" Desvio médio simples dados agrupados."""
	
	global is_terminaltables
	global decimal
	
	global sum_fi
	global sum_xi
	global sum_x2
	global sum_xi_fi
	global sum_fi_x3
	
	global list_fi
	global list_xi
	global list_x3
	global list_xi_fi
	global list_fi_x3
	
	global quant_fi
	
	
	#Zera as listas
	list_fi_x3, list_x2, list_x3, list_xi_fi = [], [], [], []
	
	l = []
	
	#Escopo da tablea
	l.append(["fi", "xi", "xi.fi","|xi-'x-barra'|", "fi.|xi-'x-barra'|"])
	
	for x in range(0, quant_fi):
		#|x-'x-barra'|
		list_x3.append(abs(round(list_xi[x] - x1, decimal)))
		#xi.fi
		list_xi_fi.append(round(list_xi[x]*list_fi[x], decimal))
		#fi. |x-'x-barra'|
		list_fi_x3.append(round(list_fi[x]*list_x3[x], decimal))
		
		#True caso o terminaltables foi instalado
		if is_terminaltables:
			l.append([list_fi[x], list_xi[x], list_xi_fi[x], list_x3[x], list_fi_x3[x]])
		else:
			pass
	
	#Recebem as somas das listas
	sum_fi = round(basic.sum_list(list_fi), decimal)
	sum_xi = round(basic.sum_list(list_xi), decimal)
	sum_xi_fi = round(basic.sum_list(list_xi_fi), decimal)
	sum_x3 = round(basic.sum_list(list_x3), decimal)
	sum_fi_x3 = round(basic.sum_list(list_fi_x3), decimal)
	
	if is_terminaltables:
		l.append([sum_fi, sum_xi, sum_xi_fi, sum_x3, sum_fi_x3])
		tables(l, True,"Dados Agrupados - Desvio médio simples")
	else:
		print("Instale o módulo terminaltables para mais detalhes.\n")
		
	print(f"\n\t Desvio médio simples é ({sum_fi_x3}/{sum_fi}) = {round(sum_fi_x3/sum_fi, decimal)}")
# ------------------------------------------------------------------------------------------


def casa_decimal():
	""" Atualiza a casa decimal."""
	global decimal
	try:
		decimal = int(input("Digite entre 1 a 5: "))
		if decimal > 5 or decimal < 1:
			decimal = 2
			basic.decimal = 2
		else:
			basic.decimal = decimal
	except:
		pass

# ------------------------------------------------------------------------------------------

def new_xi(initial, amplitude_class, amount_class):
	""" Faz a list_xi com base na entrada. """
	global decimal
	
	list_ = []
	
	for x in range(0, amount_class):
		if str(initial+(amplitude_class/2)).endswith(".0"):
			list_.append(round(initial+(amplitude_class/2)))
			initial += amplitude_class
		else:
			list_.append(round(initial+(amplitude_class/2), decimal))
			initial += amplitude_class
		
	return list_

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

def data_entry(raw_data):
	""" Onde colhe os dados Dados brutos e Agrupados."""
	global amplitude
	
	global list_xi
	global list_fi
	global list_xi_fi
	
	global initial
	global quant_fi
	global quant_xi
	
	#Para dados brutos
	if raw_data == True:
		
		print("Exemplo de Entrada:\n\txi: 14,15,63,10,52,10,59\n")
		
		string_xi = str(input("xi: ")).replace(" ","")
		list_xi = basic.dismemberment(string_xi)
		quant_xi = len(list_xi)
		
		if len(list_xi) == 0:
			return
			
		else:
			clear_()
			print(f"xi = {list_xi}")
			input("...")
			
# --------#### Dados Agrupados #####--------------------------------------------------------------------
	
	# Pede os dados e faz o pré- processamento das variáveis necessarias para funções em seguida
	else:
		#Demostração de entrada 
		print("Exemplo de Entradas:\n\tfi: 18,31,15,10,7,5,4 \n\txi:\n\t  Xmin da 1° Classe:500\n\t  Amplitude_classe:200\n")
		
		string_fi = str(input("fi: ")).replace(" ", "")
		try:
			
			initial= float(input("Xmin da 1° Classe "))
			amplitude= float(input("Amplitude da classe: "))
			
			#Recebe a lista fi desmembrada 
			list_fi = basic.dismemberment(string_fi)
			
			#Calcula a quantidade de classes com base na list_fi
			quant_fi = len(list_fi)
			
			quant_xi = len(list_xi)
			
			#Calcula o xi com base nos dados de entrada e return uma lista
			list_xi = new_xi(initial, amplitude, quant_fi)
			
			#Cria a lista nova xi.fi
			for x in range(0, len(list_fi)):
				list_xi_fi.append(round(list_xi[x]*list_fi[x], 2)) #xi.fi
			#Pegando a soma das listas
			sum_xi = basic.sum_list(list_xi)
			sum_fi = basic.sum_list(list_fi)
		except:
			pass
		
		if len(list_xi) == 0 or list_fi == 0 or len(list_xi ) != len(list_fi):
			return
			
		else:
			print(f"xi = {list_xi}")
			print(f"fi = {list_fi}")
			input("...")

def dados_brutos_while():
	""" While dos dados brutos. """
	global is_raw_data
	global x1
	global list_xi
	global list_x3
	global modo_1
	global total_amp
	global commands2
	global sum_x3
	
	while 1:
		is_raw_data = True
		clear_()
		print(basic.terminal_size(modo_1, "="))
		print(basic.terminal_size(f"xi:{list_xi}", " "))
				
		# Calcula a média aritmética
		arithmetic_mean(list_xi)
		total_amp = statistic.total_amplitude1(list_xi)
		print("\n")
				
		for command in commands2:
			print(command)
				
		res2 = input("Opção: ")
				
		if res2 == "1":
			#Amplitude total
			print(f"\n\t Amplitude Total:{total_amp}\n")
			input("...")
			#Corta o loop e evita de aparecer o print do final
			continue
					
					
		elif res2 == "2":
			# Desvio médio simples
			average_mean_deviation1()
				
				
		elif res2 == "3":
			# Desvio Padrão
			standard_deviation()
				
				
		elif res2 == "4":
			#Todos(1,2,3) - Amplitude total - Desvio médio simples - Desvio Padrão
			print(f"\n\t Amplitude Total:{total_amp}\n")
			average_mean_deviation1()
			standard_deviation()
					
				
				
		elif res2 == "5":
			casa_decimal()
			#Corta o loop e evita de aparecer o print do final
			continue
					
		elif res2 == "6":
			#Sair
			break
		else:
			#Corta o loop e evita de aparecer o print do final
				continue
					
		print(f"\tCalculando Média aritmética:{sum_x3}/{len(list_x3)} = {x1}\n")
		input("...")


def dados_agrupados_while():
	""" While dos dados agrupados. """
	global modo_2
	global list_fi
	global list_xi
	global list_xi_fi
	global commands2
	global total_amp
	global xi
	global sum_xi_fi
	global sum_fi
	
	while 1:
		clear_()
		
		#Escopo do menu Dados agrupados
		print(basic.terminal_size(modo_2, "="))
		print(basic.terminal_size(f"fi:{list_fi}", " "))
		print(basic.terminal_size(f"xi:{list_xi}", " "))
		print("\n")
				
		for command in commands2:
			print(command)
					
		res2 = input("Opção: ")
				
		if res2 =="1":
			#Amplitude total - Dados Agrupados
			print(f"\n\t Amplitude Total:{total_amp}\n")
			input("...")
			continue
					
		elif res2 == "2":
			#Desvio médio simples - Dados Agrupados
			average_mean_deviation2()
			
		elif res2 == "3":
			standard_deviation2()
				
		elif res2 == "4":
			total_amp = statistic.total_amplitude2(initial, amplitude, quant_fi)
			average_mean_deviation2()
			standard_deviation2()
				
		elif res2 == "5":
			casa_decimal()
			continue
				
		elif res2 == "6":
			#exit do submenu dos dados agrupados
			break
		else:
			continue
				
		print(f"\tCalculando Média aritmética:{sum_xi_fi}/{len(list_xi_fi)} = {x1}\n")
		input("...")
		
# ------------------------------------------------------------------------------------------
# ------------------------------- while principal do script ---------------------
# ------------------------------------------------------------------------------------------

while 1:
	clear_()
	
	#Escopo do While principal
	print(basic.terminal_size(" Medida de dispersão ", "+"))
	print(f"\t\t   Decimal:  {decimal}\n")
	
	for command in commands1:
		print(command)
	res1 = input("Opção: ")
	
	if res1 == "1":
		#Dados brutos
		data_entry(True)
		if len(list_xi) > 1:
			
			#Ler a soma da list_xi
			sum_xi = basic.sum_list(list_xi)
			
			#ler a quantidade de dados list_xi
			quant_xi = len(list_xi)
			
			#While dos dados brutos
			dados_brutos_while()
		else:
			print("Dados Inválidos.")
			time.sleep(1)
			
			
			
			
	elif res1 == "2":
		#Dados Agrupados
		data_entry(False)
		
		#Verifica se a algo errado com os dados
		if len(list_xi) > 1 and len(list_fi) > 1 and len(list_xi) == len(list_fi):
			#Calcula a média aritmética
			arithmetic_mean(list_xi_fi, True)
			total_amp = statistic.total_amplitude2(initial, amplitude, quant_fi)
			
			#while dos dados agrupados
			dados_agrupados_while()
					
		else:
			print("Dados Inválidos.")
			time.sleep(1)
	
	
	
	elif res1 == "3":
		if is_terminaltables:
			l = [["Sobre"], abount]
			tables(l)
		else:
			print(f"\nSobre:\n\t{abount[0]}")
		input("...")
	
	
	elif res1 == "4":
		print("ATENÇÃO:\n\tQuanto mais casas decimais, mais chances\ndo o resultado ser absoluto.\n")
		print("  \tXmin é o número menor da 1° classe Agrupada.\n")
		print("  \tAmplitude da classe é a distância de um Xmin ao Xmax da \n\t  mesma classe. Ex: 500|----700 --> 200")
		input("...")
			
		
	elif res1 == "5":
		casa_decimal()
			
		
	elif res1 == "6":
		#Sai do script
		print(":)")
		break
		
	
		
		




