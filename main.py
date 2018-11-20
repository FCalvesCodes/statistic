#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-


#Arquivo principal
#Medida de dispersão

from func import Basic, Statistic
import os
import time
import sys


is_terminaltables = True

try:
	from terminaltables import AsciiTable
	it_broke = False
except:
	print("Instale o módulo terminaltables.")
	time.sleep(2)
	is_terminaltables = False
	
	
basic = Basic()
statistic = Statistic()

modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------

xmin = 0
xmax = 0
amplitude = 0
x1= 0				 #Média aritmética
sum_x3 = 0
sum_x4 = 0
sum_xi = 0
quant_xi = 0 	 #len(list_xi)
quant_fi = 0       #len(list_fi)
decimal = 2
total_amp = 0


list_x2 = []		  #xi - "x-barra"
list_x3 = []		  #|xi - "x-barra"|
list_x4 = []		  #(xi - "x-barra")^2
list_xi = []		   # xi
list_fi = []		   # fi

is_raw_data = False




commands1 = ["[1] - Dados Brutos",\
								"[2] - Dados Agrupados",\
								"[3] - Sobre",\
								"[4] - Configurar casa decimal",\
							    "[5] - Sair"]

commands2 = ["[1] - Amplitude total",\
								"[2] - Desvio médio simples",\
								"[3] - Desvio padrão",\
								"[4] - Todos(1, 2, 3)",\
								"[5] - Retornar"]

abount = ["Script desenvolvido para auxiliar em\n Medida de dispersão.\n        github: FelipeAlmeid4."]

def clear_():
	""" Limpa o terminal de acordo com
		sua plataforma."""
	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
		
	
def tables(data, ult_borda= False):
	""" Cria a tabela e imprime ela. """
	global it_broke
	
	tables_terminal = AsciiTable(data)
	tables_terminal.inner_footing_row_border = ult_borda
	tables_terminal.padding_left = 2
	if tables_terminal.ok:
		print(tables_terminal.table)
	else:
		it_broke = True
		print("Tabela não pode ser visualizada, \n Reduza o zoom do terminal e tente novamente")
	
	
def arithmetic_mean1(list_):
	""" Faz a operação para obter a média 
		aritimética  e guarda na var x1."""
	global x1
	global quant_xi
	global list_xi
	global decimal
	global it_broke
	
	#Média aritmética adc em x1
	total = basic.sum_list(list_)
	quantidade = len(list_)
	x1 = round(total/quantidade, decimal)
	try:
		if it_broke == False:
			print(f"\n\tCalculando Média aritmética: {x1}\n")
	except:
		print(f"\n\tCalculando Média aritmética: {x1}\n")
# ------------------------------------------------------------------------------

def standard_deviation():
	#Desvio padrão
	global decimal
	global sum_x2
	global is_terminaltables
	global list_x4
	global it_broke
	
	l = []
	l.append(["xi", "xi-'x-barra'","|xi-'x-barra'|","(xi-'x-barra')²"])
	
	for x in range(0, quant_xi):
		list_x2.append(round(list_xi[x] - x1, decimal))
		list_x3.append(abs(round(list_xi[x] - x1, decimal)))
		list_x4.append(round(list_x3[x]**2, decimal))
		if is_terminaltables:
			l.append([list_xi[x], list_x2[x], list_x3[x], list_x4[x]])
		else:
			print(f"{list_xi[x]} - {x1} = {list_x2[x]} > |{list_x3[x]}| > {list_x4[x]}")
	sum_x3 = round(basic.sum_list(list_x3), decimal)
	sum_x4 = round(basic.sum_list(list_x4), decimal)
	if is_terminaltables:
		l.append([" ", "Σ",sum_x3, sum_x4])
		tables(l, True)
		dt = sum_x4/len(list_x4)
		dt = dt**0.5
		try:
			if it_broke == False:
				print(f"\n\tDesvio padrão é √({sum_x4}/{len(list_x4)}) = {round(dt, decimal)}")
		except:
			print(f"\n\tDesvio padrão é √({sum_x4}/{len(list_x4)}) = {round(dt, decimal)}")
	else:
		print(f"\n\t    Σ {sum_x3} - ({sum_x4})² ")
	
	
	
def average_mean_deviation1():
	#Desvio médio simples
	global decimal
	global sum_x2
	global is_terminaltables
	global list_x4
	global it_broke
	
	l = []
	l.append(["xi", "xi-'x-barra'","|xi-'x-barra'|"])
	for x in range(0, quant_xi):
		list_x2.append(round(list_xi[x] - x1, decimal))
		list_x3.append(abs(round(list_xi[x] - x1, decimal)))
		list_x4.append(round(list_x3[x]**2, decimal))
		if is_terminaltables:
			l.append([list_xi[x], list_x2[x], list_x3[x]])
		else:
			print(f"{list_xi[x]} - {x1} = {list_x2[x]} > |{list_x3[x]}|")
	sum_x3 = round(basic.sum_list(list_x3), decimal)
	if is_terminaltables:
		l.append([" ", "Σ",sum_x3])
		tables(l, True)
		
		try:
			if it_broke == False:
				print(f"\n\t Desvio médio simples é ({sum_x3}/{len(list_x3)}) = {round(sum_x3/len(list_x3), decimal)}")
		except:
			print(f"\n\t Desvio médio simples é ({sum_x3}/{len(list_x3)}) = {round(sum_x3/len(list_x3), decimal)}")
			
	else:
		print(f"\n\t    Σ {sum_x3}")
		
	
# ------------------------------------------------------------------------------------------

def total_amplitude(at_):
	#Amplitude total
	global total_amp
	total_amp = at_
	print(f"\n\t Amplitude Total:{total_amp}\n")

# ------------------------------------------------------------------------------------------

def new_xi(initial, amplitude_class, amount_class):
	#Cria o xi baseado na entrada
	list_ = []
	
	for x in range(0, amount_class):
		list_.append(initial+(amplitude_class/2))
		initial += amplitude_class
	return list_

# -------------------------------------------------------------------------------

def reset_var():
	global list_x2
	global list_x3
	global list_x4
	
	list_x2, list_x3, list_x4 = [], [], []

# -------------------------------------------------------------------------------

def data_entry(raw_data):
	#raw_data - bool
	global list_xi
	global list_fi
	global is_error
	
	if raw_data == True:
		print("Exemplo de Entrada:\n\txi: 14,15,63,10,52,10,59\n")
		string_xi = str(input("xi: ")).replace(" ","")
		list_xi = basic.dismemberment(string_xi)
		
		if len(list_xi) == 0:
			return
		else:
			clear_()
			print(f"xi = {list_xi}")
			input("...")
			
			
	else:
		print("Exemplo de Entradas:\n\tfi: 14,15,63,10,52,10,59\n\txi:\n\t  Inicial:\n\t  Amplitude_classe:\n")
		
		string_fi = str(input("fi: ")).replace(" ", "")
		try:
			initial= float(input("Xmin da 1° Classe "))
			amplitude= float(input("Amplitude da classe: "))
			list_fi = basic.dismemberment(string_fi)
			quant_fi = len(list_fi)
			list_xi = new_xi(initial, amplitude, quant_fi)
		except:
			pass
		
		
		
		
		
		
		if len(list_xi) == 0 or list_fi == 0 or len(list_xi ) != len(list_fi):
			return
		else:
			print(f"xi = {list_xi}")
			print(f"fi = {list_fi}")
			input("...")
			
# ------------------------------------------------------------------------------------------
# -------------------- while principal do script --------------------------------
# ------------------------------------------------------------------------------------------

while 1:
	clear_()
	
	print(basic.terminal_size("Medida de dispersão", "+"))
	print(f"\t\t   Decimal:  {decimal}\n")
	
	for command in commands1:
		print(command)
	
	res1 = input("Opção: ")
	
	if res1 == "1":
		#Dados brutos
		data_entry(True)
		if len(list_xi) > 2:
			
			#Ler a soma da list_xi
			sum_xi = basic.sum_list(list_xi)
			
			#ler a quantidade de dados list_xi
			quant_xi = len(list_xi)
			
			
			# ------------------------------------------------------------------------------------------
		    # -------------------- while Dados brutos --------------------------------------
            # ------------------------------------------------------------------------------------------
			while 1:
				reset_var()
				is_raw_data = True
				clear_()
				print(basic.terminal_size(modo_1, "="))
				print(basic.terminal_size(f"xi:{list_xi}", " "))
				print("\n")
				
				for command in commands2:
					print(command)
				
				res2 = input("Opção: ")
				
				if res2 == "1":
					#Amplitude total
					total_amplitude(statistic.total_amplitude1(statistic.rol_raw_data(list_xi)))
					input("...")
				elif res2 == "2":
					arithmetic_mean1(list_xi)
					average_mean_deviation1()
					input("...")
				
				elif res2 == "3":
					arithmetic_mean1(list_xi)
					standard_deviation()
					input("...")
				
				elif res2 == "4":
					#Todos(1,2,3)
					total_amplitude(statistic.total_amplitude1(statistic.rol_raw_data(list_xi)))
					arithmetic_mean1(list_xi)
					average_mean_deviation1()
					reset_var()
					standard_deviation()
					input("...")
					
				elif res2 == "5":
					#sair
					break
					
					
		else:
			print("Dados Inválidos.")
			time.sleep(1)
			
			
			
			
	elif res1 == "2":
		#Dados Agrupados
		data_entry(False)
		if len(list_xi) > 1 and len(list_fi) > 1 and len(list_xi) == len(list_fi):
			
			# ------------------------------------------------------------------------------------------
		    # -------------------- while Dados Agrupados  --------------------------
            # ------------------------------------------------------------------------------------------
			
			while 1:
				reset_var()
				clear_()
				print(basic.terminal_size(modo_2, "="))
				
				for command in commands2:
					print(command)
					
				res2 = input("Opção: ")
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
		decimal = int(input("Digite entre 1 a 5: "))
		if decimal > 5 or decimal < 1:
			decimal = 2
			
		
	elif res1 == "5":
		print("exit :)")
		break
		
	
		
		




