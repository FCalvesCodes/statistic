#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-


#Arquivo principal
#Medida de dispersão

from func import Basic, Statistic
import os
import time

basic = Basic()
statistic = Statistic()

modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------
x1= 0					#Média aritmética
sum_x2 = 0
sum_x3 = 0
sum_x4 = 0
sum_xi = 0
quant_xi = 0 	 #len(xi)

list_x2 = []		  #xi - "x-barra"
list_x3 = []		  #|xi - "x-barra"|
list_x4 = []		  #(xi - "x-barra")^2
list_xi = []		   # xi

list_fi = []
is_raw_data = False
decimal = 2

at = 0

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

sobre = "Script desenvolvido para auxiliar em\n Medida de dispersão.\n\t github: FelipeAlmeid4."

def total_amplitude(at):
	print(f"\n\t Amplitude Total:{at}\n")

# ------------------------------------------------------------------------------------------
def new_xi(initial, amplitude_class, amount_class):
	list_ = []
	
	for x in range(0, amount_class):
		list_.append(initial+(amplitude_class/2))
		initial += amplitude_class
	return list_

# -------------------------------------------------------------------------------

def reset_var():
	global list_xi

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
			os.system("clear")
			print(f"xi = {list_xi}")
			input("...")
			
			
	else:
		print("Exemplo de Entradas:\n\tfi: 14,15,63,10,52,10,59\n\txi:\n\t  Inicial:\n\t  Amplitude_classe:\n")
		
		string_fi = str(input("fi: ")).replace(" ", "")
		initial= float(input("N° inicial: "))
		am_c = float(input("Amplitude das classes: "))
		
		
		list_fi = basic.dismemberment(string_fi)
		
		qu_c = len(list_fi)
		list_xi = new_xi(initial, am_c, qu_c)
		
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
	os.system("clear")
	
	print(basic.terminal_size("Medida de dispersão", "+"))
	print(f"\t\t   Decimal:  {decimal}\n")
	
	for command in commands1:
		print(command)
	
	res1 = input("Opção: ")
	
	if res1 == "1":
		#Dados brutos
		data_entry(True)
		if len(list_xi) > 1:
			
			#Ler soma list
			sum_xi = basic.sum_list(list_xi)
			quant_xi = len(list_xi)
			
			
			# ------------------------------------------------------------------------------------------
		    # -------------------- while principal do submenu --------------------------------
            # ------------------------------------------------------------------------------------------
			while 1:
				is_raw_data = True
				os.system("clear")
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
					
		else:
			print("Dados Inválidos.")
			time.sleep(1)
			
			
			
			
	elif res1 == "2":
		#Dados Agrupados
		data_entry(False)
		if len(list_xi) > 1 and len(list_fi) > 1 and len(list_xi) == len(list_fi):
			
			# ------------------------------------------------------------------------------------------
		    # -------------------- while principal do submenu --------------------------
            # ------------------------------------------------------------------------------------------
			
			while 1:
				os.system("clear")
				print(basic.terminal_size(modo_2, "="))
				
				for command in commands2:
					print(command)
					
				res2 = input("Opção: ")
		else:
			print("Dados Inválidos.")
			time.sleep(1)
	
	
	
	elif res1 == "3":
		print(sobre)
		input("...")
	
	
	elif res1 == "4":
		decimal = int(input("Digite entre 0 á 5: "))
		
	elif res1 == "5":
		print("exit :)")
		break
		
	
		
		




