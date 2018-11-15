#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-


#Arquivo principal
#Medida de dispersão

from func import Basic
import os
import time

basic = Basic()

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

is_error = False


commands1 = ["[1] - Dados brutos",\
								"[2] - Dados Agrupados",\
								"[3] - Sobre",\
								"[4] - Sair"]

commands2 = ["[1] - Amplitude total",\
								"[2] - Desvio médio simples",\
								"[3] - Desvio padrão",\
								"[4] - Todos(1, 2, 3)",\
								"[5] - Retornar"]
								
def data_entry(raw_data):
	#raw_data - "dados brutos"
	global list_xi
	global is_error
	
	if raw_data == True:
		print("Exemplo:\n\txi: 14,15,63,10,52,10,59\n")
		string_xi = str(input("xi: ")).replace(" ","")
		list_xi = basic.dismemberment(string_xi)
		
		if not len(list_xi) > 0:
			is_error = True
			return
		else:
			print(f"xi = {list_xi}")
			input("...")
			
			
	else:
		print("Exemplo:\n\txi: 14,15,63,10,52,10,59\n\tfi: 500,700,900,1100,1300,1500,1700\n")
		
		string_xi = str(input("xi: ")).replace(" ", "")
		string_fi = str(input("fi: ")).replace(" ","")
		
		list_xi = basic.dismemberment(string_xi)
		list_fi = basic.dismemberment(string_fi)
		
		if not len(list_xi) > 0 or len(list_xi) != len(list_fi):
			is_error = True
			return
		else:
			print(f"xi = {list_xi}")
			print(f"fi = {list_fi}")
			input("...")
			

while 1:
	os.system("clear")
	
	for command in commands1:
		print(command)
	
	res1 = input("Opção: ")
	
	if res1 == "1":
		data_entry(True)
		while 1:
			os.system("clear")
			print("===== Modo Dados Brutos =====\n")
			input()
			break
	elif res1 == "2":
		data_entry(False)
		while 1:
			os.system("clear")
			print("===== Modo Dados Agrupados =====\n")
			input()
			break
	elif res1 == "3":
		pass
	elif res1 == "4":
		break
		
	
		
		




