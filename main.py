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
					$ git clone https://github.com/FelipeAlmeid4/statistic.git
					$ cd statistic
					$ python main.py
"""

from decimal import Decimal
from mod.func import Statistic
from mod import func2
from mod.func2 import Process
from mod import terminal 
import os
import time
import sys

is_terminaltables = True

try:
	from terminaltables import AsciiTable
except:
	is_terminaltables = False
	print("Instale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)
	
	
statistic = Statistic()
process =  Process()


modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------


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
								"[5] - Configurar Casa decimal",\
								"[5.1] - Ativar/Desativar  Amostra",\
								"[5.2] - Ativa/Desativar População",\
								"[6] - Retornar"]

commands3 = ["[1] - Amostra",\
							  "[2] - População"]

abount = ["Esse script foi feito para fins didáticos,\nEstá bem estável pelo termux, \ndados inseridos somente dados inteiros\n       github: FelipeAlmeid4."]

#--------------------------------------------------------------------
def tables(data, ult_borda= False,title= ""):
		""" Recebe a tabela em formatos Matriz."""
		tables_terminal = AsciiTable(data)
		tables_terminal.inner_footing_row_border = ult_borda
		tables_terminal.padding_left = 2
		tables_terminal.title = title
		if tables_terminal.ok:
			print(tables_terminal.table)
		else:
			print("Tabela não pode ser visualizada, \n Recua o zoom do terminal e tente novamente.")

def truncate(f, n):
    '''Truncates/pads a float f to n process.decimal places without rounding'''
    #https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return Decimal('{0:.{1}f}'.format(f, n))
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

def variance():
	#Variância amostral e populacional
	if len(process.list_fi) == 0:
		#Para dados brutos
		if process.sample:
			process.gerar_matriz_table((["i","xi", "xi-ㄡ", "|xi-ㄡ"]), False, 3)
			print(f"\n\tVariância amostral é {process.sum_x4}/{process.quant_xi-1} = {truncate(process.sum_x4/(process.quant_xi-1), process.decimal)}\n")
		if process.populational:
			process.gerar_matriz_table((["i","xi", "xi-ㄡ", "|xi-ㄡ"]) , False, 3)
			print(f"\n\tVariância populacional é {process.sum_x4}/{process.quant_xi} = {truncate(process.sum_x4/process.quant_xi,  process.decimal)}\n")
	else:
		#para dados Agrupados
		if process.sample:
			process.gerar_matriz_table((["i","fi", "xi","xi.fi", "xi-ㄡ", "(xi-ㄡ)²","fi.(xi-ㄡ)²"]) , True, 3)
			print(f"\n\tVariância amostral é {process.sum_fi_x4}/{process.quant_xi-1} = {truncate(process.sum_fi_x4/(process.quant_xi-1), process.decimal)}\n")
		if process.populational:
			process.gerar_matriz_table((["i", "fi", "xi","xi.fi", "xi-ㄡ", "(xi-ㄡ)²","fi.(xi-ㄡ)²"]), False, 3)
			print(f"\n\tVariância populacional é {process.sum_fi_x4}/{process.quant_xi} = {truncate(process.sum_fi_x4/process.quant_xi, process.decimal)}\n")
		


#------------------------------------------------------
	
def arithmetic_mean(list_, grouped_data=False):
	""" Faz a operação para obter a média 
		aritimética  e guarda na var x1."""
		
	total = func2.sum_list(list_)
	
	if grouped_data:
		#Para dados Agrupados
		process.sum_fi = round(func2.sum_list(process.list_fi), process.decimal)
		quantidade = process.sum_fi
	else:
		quantidade = len(list_)
	process.x1 = truncate(total/quantidade, process.decimal)

# ------------------------------------------------------------------------------

def standard_deviation():
	"""Desvio padrão para dados brutos."""
	
	#Escopo da tabela
	escopo = (["xi", "xi-ㄡ","|xi-ㄡ|", "(xi-ㄡ)²"])
	
	process.gerar_matriz_table(escopo, False, 2)
	
	#Recebe o resultado da raiz
	dt = statistic.standard_deviation(process.sum_x4, process.list_x4)
		
	print(f"\n\tDesvio padrão é √({process.sum_x4}/{len(process.list_x4)}) = {truncate(dt, process.decimal)}")

# ---------------------------------------------------------------------
	
def standard_deviation2():
	"""Desvio padrão para dados Agrupados."""
	
	#Escopo da tabela
	escopo = (["fi", "xi","xi.fi","xi-ㄡ","(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
	process.gerar_matriz_table(escopo, True, 2)
	
	#Recebe o resultado da raiz
	dt = truncate(process.sum_fi_x4/process.sum_fi, process.decimal)
	dt = dt**Decimal("0.5")
	print(f"\n\tDesvio padrão é √({process.sum_fi_x4}/{process.sum_fi}) = {truncate(dt, process.decimal)}")
	
# -------------------------------------------------------------------------------

def average_mean_deviation1():
	""" Desvio médio simples dados brutos."""
	
	#Escopo da tabela
	escopo = ([" i", "xi", "xi-ㄡ","|xi-ㄡ|"])
	process.gerar_matriz_table(escopo, False, 1)
	
	print(f"\n\t Desvio médio simples é ({process.sum_x3}/{len(process.list_x3)}) = {truncate(process.sum_x3/len(process.list_x3), process.decimal)}")
		
# ----------------------------------------------------------------------------

def average_mean_deviation2():
	""" Desvio médio simples dados agrupados."""
	
	#Escopo da tabela
	escopo = (["fi", "xi", "xi.fi","|xi-ㄡ|", "fi.|x-'barra|'"])
	process.gerar_matriz_table(escopo, True, 1)
	
	print(f"\n\t Desvio médio simples é ({process.sum_fi_x3}/{process.sum_fi}) = {truncate(process.sum_fi_x3/process.sum_fi, process.decimal)}")
# ------------------------------------------------------------------------------------------


def casa_decimal():
	""" Atualiza a casa process.decimal."""
	try:
		process.decimal = int(input("Digite entre 1 a 5: "))
		if process.decimal > 5 or process.decimal < 1:
			process.decimal = 2
			basic.process.decimal = 2
		else:
			basic.process.decimal = process.decimal
	except:
		pass

# ------------------------------------------------------------------------------------------

def new_xi(initial, amplitude_class, amount_class):
	""" Faz a process.list_xi com base na entrada. """
	
	list_ = []
	
	for x in range(0, amount_class):
		if str(initial+(amplitude_class/2)).endswith(".0"):
			list_.append(round(initial+(amplitude_class/2)))
			initial += amplitude_class
		else:
			list_.append(truncate(initial+(amplitude_class/2), process.decimal))
			initial += amplitude_class
		
	return list_

# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

def data_entry(raw_data):
	""" Onde colhe os dados Dados brutos e Agrupados."""
	global amplitude
	global initial
	
	#Para dados brutos
	if raw_data == True:
		
		print("Exemplo de Entrada:\n\txi: 14,15,19,20,20,21,22\n")
		
		string_xi = str(input("xi: ")).replace(" ","")
		process.list_xi = func2.dismemberment(string_xi)
		process.quant_xi = len(process.list_xi)
		
		if len(process.list_xi) == 0:
			return
			
		else:
			clear_()
			print(f"xi = {process.list_xi}")
			input("...")
			
# --------#### Dados Agrupados #####--------------------------------------------------------------------
	
	# Pede os dados e faz o pré- processamento das variáveis necessarias para funções em seguida
	else:
		#Demostração de entrada 
		print("Exemplo de Entradas:\n\tfi: 18,31,15,10,7,5,4 \n\txi:\n\t  Xmin da 1° Classe:500\n\t  Amplitude_classe:200\n")
		
		string_fi = str(input("fi: ")).replace(" ", "")
		try:
			
			initial= float(input("Xmin da 1° Classe: "))
			amplitude= float(input("Amplitude da classe: "))
			
			#Recebe a lista fi desmembrada 
			process.list_fi = func2.dismemberment(string_fi)
			
			#Calcula a quantidade de classes com base na process.list_fi
			process.quant_fi = len(process.list_fi)
			
			process.quant_xi = len(process.list_xi)
			
			#Calcula o xi com base nos dados de entrada e return uma lista
			process.list_xi = new_xi(initial, amplitude, process.quant_fi)
			
			#Cria a lista nova xi.fi
			for x in range(0, len(process.list_fi)):
				process.list_fi_xi.append(truncate(process.list_xi[x]*process.list_fi[x], 2)) #xi.fi
			#Pegando a soma das listas
			process.sum_xi = func2.sum_list(process.list_xi)
			process.sum_fi = func2.sum_list(process.list_fi)
		except:
			pass
		
		if len(process.list_xi) == 0 or process.list_fi == 0 or len(process.list_xi ) != len(process.list_fi):
			return
			
		else:
			print(f"xi = {process.list_xi}")
			print(f"fi = {process.list_fi}")
			input("...")



def dados_brutos_while():
	""" While dos dados brutos. """
	
	global is_raw_data
	global modo_1
	global commands2
	
	while 1:
		is_raw_data = True
		clear_()
		print(terminal.terminal_size(modo_1, "="))
		print(terminal.terminal_size(f" Amostra: {process.sample} ", "-"))
		print(terminal.terminal_size(f" População: {process.populational} ", "-"))
		print(terminal.terminal_size(f"xi:{process.list_xi}", " "))
				
		# Calcula a média aritmética
		arithmetic_mean(process.list_xi)
		process.total_amplitude = statistic.total_amplitude1(process.list_xi)
		print("\n")
				
		for command in commands2:
			print(command)
				
		res2 = input("Opção: ")
				
		if res2 == "1":
			#Amplitude total
			print(f"\n\t Amplitude Total:{process.total_amplitude}\n")
					
		elif res2 == "2":
			# Desvio médio simples
			average_mean_deviation1()
				
				
		elif res2 == "3":
			# Desvio Padrão
			standard_deviation()
		
		elif res2 == "3.1":
			#Variância
			variance()
			
		elif res2 == "3.2":
			print(f"\tCalculando Média aritmética:{process.sum_xi}/{len(process.list_xi)} = {truncate(process.x1, process.decimal)}\n")
				
				
		elif res2 == "4":
			pass
					
				
				
		elif res2 == "5":
			casa_decimal()
			continue
		
		elif res2 == "5.2":
			#Ajustar os dados (Amostral) (Populacional)
			if process.populational:
				if process.sample == False:
					process.sample= True
				process.populational= False
			else:
				process.populational = True
				
			continue
		
		elif res2 == "5.1":
			if process.sample:
				if process.populational == False:
					process.populational = True
				process.sample= False
			else:
				process.sample = True
			continue
					
		elif res2 == "6":
			#Sair
			break
		else:
			continue
			
		input("...")
		
		
def dados_agrupados_while():
	""" While dos dados agrupados. """
	global modo_2
	
	while 1:
		clear_()
		
		process.total_amplitude = statistic.total_amplitude2(initial, amplitude, process.quant_fi)
		#Escopo do menu Dados agrupados
		print(terminal.terminal_size(modo_2, "="))
		print(terminal.terminal_size(f" Amostra: {process.sample} ", "-"))
		print(terminal.terminal_size(f" População: {process.populational} ", "-"))
		print(terminal.terminal_size(f"fi:{process.list_fi}", " "))
		print(terminal.terminal_size(f"xi:{process.list_xi}", " "))
		print("\n")
				
		for command in commands2:
			print(command)
					
		res2 = input("Opção: ")
				
		if res2 =="1":
			#Amplitude total - Dados Agrupados
			print(f"\n\t Amplitude Total:{process.total_amplitude}\n")
					
		elif res2 == "2":
			#Desvio médio simples - Dados Agrupados
			average_mean_deviation2()
			
		elif res2 == "3":
			standard_deviation2()
			
		elif res2 == "3.1":
			#Variância
			variance()
			
		elif res2 == "3.2":
			print(f"\tCalculando Média aritmética:{process.sum_fi_xi}/{len(process.list_fi_xi)} = {truncate(process.x1, process.decimal)}\n")
			
				
		elif res2 == "4":
			pass
				
		elif res2 == "5":
			#Ajustar a casa decimal
			casa_decimal()
			continue
		
		elif res2 == "5.2":
			#Ajustar os dados (Amostral) (Populacional)
			if process.populational:
				if process.sample == False:
					process.sample = True
				process.populational= False
			else:
				process.populational = True
			continue
		
		elif res2 == "5.1":
			if process.sample:
				if process.populational == False:
					process.populational = True
				process.sample= False
			else:
				process.sample = True
			continue
			
				
		elif res2 == "6":
			#exit do submenu dos dados agrupados
			break
		else:
			continue
		input("...")
# ------------------------------------------------------------------------------------------
# ------------------------------- while principal do script ---------------------
# ------------------------------------------------------------------------------------------

while 1:
	clear_()
	
	#Escopo do While principal
	print(terminal.terminal_size(" Medida de dispersão ", "+"))
	print(terminal.terminal_size(f" Casa decimal: {process.decimal} ", " "))
	
	for command in commands1:
		print(command)
	res1 = input("Opção: ")
	
	if res1 == "1":
		#Dados brutos
		data_entry(True)
		if len(process.list_xi) > 1:
			
			#Ler a soma da process.list_xi
			process.sum_xi = func2.sum_list(process.list_xi)
			
			#ler a quantidade de dados process.list_xi
			process.quant_xi = len(process.list_xi)
			
			#While dos dados brutos
			dados_brutos_while()
		else:
			print("Dados Inválidos.")
			time.sleep(1)
			
			
			
			
	elif res1 == "2":
		#Dados Agrupados
		data_entry(False)
		
		#Verifica se a algo errado com os dados
		if len(process.list_xi) > 1 and len(process.list_fi) > 1 and len(process.list_xi) == len(process.list_fi):
			#Calcula a média aritmética
			arithmetic_mean(process.list_fi_xi, True)
			
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
		
	
		
		




