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

from mod.tables import TablesTerminal
from decimal import Decimal
from mod.func import Basic, Statistic
import os
import time
import sys

t = TablesTerminal()
is_terminaltables = t.is_terminal()
	

basic = Basic()
statistic = Statistic()

modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------

xmin = 0
xmax = 0

amplitude = 0  # Amplitude da classe
x1= 0			      #Média aritmética

sum_fi_xi = 0
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
list_fi_xi = []     # xi.fi
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
								"[3.1] - Variância",\
								"[3.2] - Média aritmética",\
								"[4] - Todos(1, 2, 3)",\
								"[5] - Configurar Casa Decimal",\
								"[6] - Retornar"]

commands3 = ["[1] - Amostra",\
							  "[2] - População"]

abount = ["Amplitude Total\nDesvio médio simples\nDesvio padrão\n        github: FelipeAlmeid4."]

#--------------------------------------------------------------------


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    #https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return Decimal('.'.join([i, (d+'0'*n)[:n]]))


def clear_():
	""" Limpa o terminal de acordo com a sua plataforma."""
	if sys.platform == "linux":
		os.system("clear")
		
	elif sys.platform == "win32":
		os.system("mode con cols=110")
		os.system("cls")
		
# ----------------------------------------------------

def gerar_matriz_table(escopo, grouped, modo):
	"""  grouped = True - Dados agrupados
		    grouped = False - Dados Brutos
			modo = 1 - Desvio médio simples
			modo = 2 - Desvio padrão
			modo = 3 - Variância
	"""
	global is_terminaltables
	global list_x2		  #xi - "x-barra"
	global list_x3		  #|xi - "x-barra"|
	global list_x4		  #(xi - "x-barra")²
	global list_xi		   # xi
	global list_fi		   # fi
	global list_fi_xi     # xi.fi
	global list_fi_x3	#fi.|xi - "x-barra"|
	global list_fi_x4	#fi.(xi - "x-barra")²
	global sum_fi_xi
	global sum_x3
	global sum_x4
	global sum_xi
	global sum_fi
	global sum_fi_x3
	global sum_fi_x4 
	global decimal
	global quant_xi
	global quant_fi
	global x1
	
	l = []
	
	l.append(escopo)
	
	list_x2, list_x3, list_x4,list_fi_x3, list_fi_x4 = [],[],[],[],[]
	
	for x in range(0, len(list_xi)):
		
		#xi-ㄡ
		list_x2.append(truncate(truncate(list_xi[x], decimal) - truncate(x1, decimal), decimal))
		#|xi-ㄡ|
		list_x3.append(truncate(abs(truncate(list_xi[x], decimal) - truncate(x1, decimal)), decimal))
		#(xi-ㄡ)²
		list_x4.append(truncate(truncate(list_x3[x], decimal)**2, decimal))
		
		if grouped == True:
			#fi. |xi-ㄡ|
			list_fi_x3.append(truncate(list_fi[x]*list_x3[x], decimal))
			#fi
			list_fi_x4.append(truncate(truncate(list_fi[x], decimal)*truncate(list_x4[x], decimal), decimal))
		
		if grouped == False and modo == 1:
			#Dados brutos - Desvio médio simples
			l.append([list_xi[x], list_x2[x], list_x3[x]])
		elif grouped == False and modo == 2:
			#Dados Brutos - Desvio Padrão
			l.append([list_xi[x], list_x2[x], list_x3[x], list_x4[x]])
		elif grouped == False and modo == 3:
			#Dados brutos e Agrupados - Variância
			if len(list_fi) == 0:
				l.append([list_xi[x], list_x2[x], list_x4[x]])
		elif grouped == True and modo == 1:
			#Dados agrupados - Desvio médio simples
			l.append([list_fi[x], list_xi[x], list_fi_xi[x], list_x3[x], list_fi_x3[x]])
		
		elif grouped == True and modo == 2:
			#Dados agrupados - Desvio padrão
			l.append([list_fi[x], list_xi[x], list_fi_xi[x], list_x2[x], list_x4[x], list_fi_x4[x]])
		elif grouped == True and modo == 3:
			l.append([list_fi[x], list_xi[x], list_fi_xi[x], list_x2[x], list_x4[x], list_fi_x4[x]])
			
	#Recebe as somas
	sum_xi = truncate(basic.sum_list(list_xi), decimal)
	sum_fi = truncate(basic.sum_list(list_fi), decimal)
	sum_x3 = truncate(basic.sum_list(list_x3), decimal)
	sum_x4 = truncate(basic.sum_list(list_x4), decimal)
	sum_fi_x4 = truncate(basic.sum_list(list_fi_x4), decimal)
	sum_fi_x3 = truncate(basic.sum_list(list_fi_x3), decimal)
	sum_fi_xi = truncate(basic.sum_list(list_fi_xi), decimal)
	
	if grouped == False and modo == 1 and is_terminaltables:
		#Dados Brutos - Desvio médio simples
		l.append([sum_xi, "    Σ",sum_x3])
		t.tables(l, True, "Dados Brutos - Desvio médio simples")
	elif grouped == False and modo == 2 and is_terminaltables:
		#Dados brutos - Desvio padrão
		l.append([sum_xi, "Σ",sum_x3, sum_x4])
		t.tables(l, True,"Dados brutos - desvio padrão")
	elif grouped == False and modo == 3 and is_terminaltables:
		#Dados brutos - Variância
		l.append([sum_xi, "Σ",sum_x4])
		t.tables(l, True,"Dados brutos - Variância")
	elif grouped == True and modo == 1 and is_terminaltables:
		#Dados agrupados - Desvio médio  simples
		l.append([sum_fi, sum_xi, sum_fi_xi, sum_x3, sum_fi_x3])
		t.tables(l, True,"Dados Agrupados - Desvio médio simples")
	elif grouped == True and modo == 2 and is_terminaltables:
		#Dados agrupados - Desvio padrão
		l.append([sum_fi, sum_xi,sum_fi_xi, "Σ", sum_x4, sum_fi_x4])
		t.tables(l, True,"Dados Agrupados - desvio padrão")
	elif grouped == True and modo == 3 and is_terminaltables:
		l.append([sum_fi, sum_xi, sum_fi_xi, "Σ", sum_x4, sum_fi_x4])
		t.tables(l, True,"Dados Agrupados - Variância")
	elif is_terminaltables == False:
		print("Instale o módulo terminaltables para mais detalhes.\n")
	
	
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
	x1 = truncate(total/quantidade, 5)

# ------------------------------------------------------------------------------

def standard_deviation():
	"""Desvio padrão para dados brutos."""
	global list_x4
	global sum_x4
	
	
	#Escopo da tabela
	escopo = (["xi", "xi-ㄡ","|xi-ㄡ|", "(xi-ㄡ)²"])
	
	gerar_matriz_table(escopo, False, 2)
	
	#Recebe o resultado da raiz
	dt = statistic.standard_deviation(sum_x4,list_x4)
		
	print(f"\n\tDesvio padrão é √({sum_x4}/{len(list_x4)}) = {truncate(dt, decimal)}")

# ---------------------------------------------------------------------
def variance(amostra):
	#Variância
	global list_x4
	global sum_x4
	global decimal
	global list_fi
	global sum_fi
	global list_fi_x4
	global sum_fi_x4
	global list_fi_xi
	
	if len(list_fi) == 0 and amostra:
		#Amostra
		escopo = (["xi", "xi-ㄡ", "(xi-ㄡ)²"])
		gerar_matriz_table(escopo, False, 3)
		print(f"\n\tVariância amostral é {sum_x4}/{len(list_x4)-1} = {truncate(sum_x4/(len(list_x4)-1), decimal)}")
	elif len(list_fi) == 0 and amostra == False:
		#população
		escopo = (["xi", "x - ㄡ'", "(xi-ㄡ)²"])
		gerar_matriz_table(escopo, False, 3)
		print(f"\n\tVariância populacional é {sum_x4}/{len(list_x4)} = {truncate(sum_x4/(len(list_xi)), decimal)}")
	else:
		if amostra:
			escopo = (["fi", "xi", "fi.xi", "xi-ㄡ", "(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
			gerar_matriz_table(escopo, True, 3)
			print(f"\n\tVariância amostral é {sum_fi_x4}/{sum_fi-1} = {truncate(sum_fi_x4/(sum_fi-1), decimal)}")
		elif amostra == False:
			escopo = (["fi", "xi", "fi.xi", "xi-ㄡ", "(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
			gerar_matriz_table(escopo, True, 3)
			print(f"\n\tVariância amostral é {sum_fi_x4}/{sum_fi} = {truncate(sum_fi_x4/sum_fi, decimal)}")
			
			
		
	
	
	
def standard_deviation2():
	"""Desvio padrão para dados Agrupados."""
	global decimal
	global sum_fi
	global sum_fi_x4
	
	#Escopo da tabela
	escopo = (["fi", "xi","xi.fi","xi-ㄡ","(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
	gerar_matriz_table(escopo, True, 2)
	
	#Recebe o resultado da raiz
	dt = truncate(sum_fi_x4/sum_fi, decimal)
	dt = dt**Decimal("0.5")
	print(f"\n\tDesvio padrão é √({sum_fi_x4}/{sum_fi}) = {truncate(dt, decimal)}")
	
# -------------------------------------------------------------------------------

def average_mean_deviation1():
	""" Desvio médio simples dados brutos."""
	global decimal
	global sum_x3
	global list_x3
	
	#Escopo da tabela
	escopo = (["xi", "xi-ㄡ","|xi-ㄡ|"])
	gerar_matriz_table(escopo, False, 1)
	
	print(f"\n\t Desvio médio simples é ({sum_x3}/{len(list_x3)}) = {truncate(sum_x3/len(list_x3), decimal)}")
		
# ----------------------------------------------------------------------------

def average_mean_deviation2():
	""" Desvio médio simples dados agrupados."""
	global decimal
	global sum_fi
	global sum_fi_x3
	
	#Escopo da tabela
	escopo = (["fi", "xi", "xi.fi","|xi-ㄡ|", "fi.|x-'barra|'"])
	gerar_matriz_table(escopo, True, 1)
	
	print(f"\n\t Desvio médio simples é ({sum_fi_x3}/{sum_fi}) = {truncate(sum_fi_x3/sum_fi, decimal)}")
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
			list_.append(truncate(initial+(amplitude_class/2), decimal))
			initial += amplitude_class
		
	return list_

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

def data_entry(raw_data):
	""" Onde colhe os dados Dados brutos e Agrupados."""
	global amplitude
	
	global list_xi
	global list_fi
	global list_fi_xi
	
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
				list_fi_xi.append(truncate(list_xi[x]*list_fi[x], 2)) #xi.fi
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
	global sum_xi
	
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
					
		elif res2 == "2":
			# Desvio médio simples
			average_mean_deviation1()
				
				
		elif res2 == "3":
			# Desvio Padrão
			standard_deviation()
		
		elif res2 == "3.1":
			#Variância
			while 1:
				
				for command in commands3:
					print(command)
				res3 = input("Opção: ")
				
				if res3 == "1":
					variance(True)
					break
				elif res3 == "2":
					variance(False)
					break
				else:
					pass
			
				input("...")
		elif res2 == "3.2":
			print(f"\tCalculando Média aritmética:{sum_xi}/{len(list_xi)} = {truncate(x1, decimal)}\n")
				
				
		elif res2 == "4":
			#Todos(1,2,3) - Amplitude total - Desvio médio simples - Desvio Padrão
			print(f"\n\t Amplitude Total:{total_amp}\n")
			average_mean_deviation1()
			standard_deviation()
					
				
				
		elif res2 == "5":
			casa_decimal()
					
		elif res2 == "6":
			#Sair
			break
		else:
			pass
			
		input("...")
def dados_agrupados_while():
	""" While dos dados agrupados. """
	global modo_2
	global list_fi
	global list_xi
	global list_fi_xi
	global commands2
	global total_amp
	global xi
	global sum_fi_xi
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
					
		elif res2 == "2":
			#Desvio médio simples - Dados Agrupados
			average_mean_deviation2()
			
		elif res2 == "3":
			standard_deviation2()
			
		elif res2 == "3.1":
			#Variância
			while 1:
				
				for command in commands3:
					print(command)
				res3 = input("Opção: ")
				
				if res3 == "1":
					variance(True)
					break
				elif res3 == "2":
					variance(False)
					break
				else:
					pass
			
		elif res2 == "3.2":
			print(f"\tCalculando Média aritmética:{sum_fi_xi}/{len(list_fi_xi)} = {truncate(x1, decimal)}\n")
			
				
		elif res2 == "4":
			total_amp = statistic.total_amplitude2(initial, amplitude, quant_fi)
			average_mean_deviation2()
			standard_deviation2()
				
		elif res2 == "5":
			casa_decimal()
			print("Configurado para {decimal}.")
				
		elif res2 == "6":
			#exit do submenu dos dados agrupados
			break
		else:
			pass
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
			arithmetic_mean(list_fi_xi, True)
			total_amp = statistic.total_amplitude2(initial, amplitude, quant_fi)
			
			#while dos dados agrupados
			dados_agrupados_while()
					
		else:
			print("Dados Inválidos.")
			time.sleep(1)
	
	
	
	elif res1 == "3":
		if is_terminaltables:
			l = [["Sobre"], abount]
			t.tables(l)
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
		
	
		
		




