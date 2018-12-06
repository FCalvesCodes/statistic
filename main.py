#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-


from mod.modo_audit import ModoAudit
from collections import defaultdict
from mod.func2 import Process
from mod.func import Statistic
from decimal import Decimal
from mod import terminal 
from mod import func2
import time
import sys
import os


try:
	from termcolor import colored
	install_termcolor = True
except:
	install_termcolor = False

try:
	from terminaltables import AsciiTable
	install_terminaltables = True
except:
	install_terminaltables = False
	print("Instale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)
	
	
statistic = Statistic()
process =  Process()

#Para fazer auditoria das variáveis(Em Desenvolvimento)
modoaudit = ModoAudit(statistic)

#Retira algumas configurações no modo dados brutos
modo_agrupados = None


modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------


# É dados brutos
is_raw_data = False




commands1 = ["[1] - Dados Brutos",\
								"[2] - Dados Agrupados",\
								"[3] - Sobre",\
								"[4] - Informações",\
								"[5] - Configurações",\
							    "[6] - Sair"]

commands2_agr = ["[1]  -  Amplitude Total",\
								"[2]  -  Desvio Médio Simples",\
								"[3]  -  Desvio Padrão",\
								"[4]  -  Variância (Em desenvolvimento)",\
								"[5]  -  Média Aritmética",\
								"[5.1] - Moda",\
								"[5.2] - Mediana",\
								"[6]  -  Configurações",\
								"[7]  -  Visualizar tabela de frequência",\
								"[8]  -  Retornar"]

commands2 = ["[1]  -  Amplitude total",\
								"[2]  -  Desvio Médio Simples",\
								"[3]  -  Desvio Padrão",\
								"[4]  -  Variância",\
								"[5]  -  Média Aritmética",\
								"[5.1] - Média Aritmética ponderada",\
								"[6] - Moda",\
								"[6.1]  - Mediana",\
								"[7] - Configurações",\
								"[8] - Retornar"]

commands3 = ["[1] - Ajustar Casa Decimal",\
							"[2] - Ativar/Desativar - Amostra",\
							"[3] - Ativar/Desativar - População",\
							"[4] - Ativar/Desativar - Freq. Relativa (fri%)",\
							"[5] - Ativar/Desativar - Freq. Absoluta Acumulada (Fi)",\
							"[6] - Ativar/Desativar - Freq. Relativa Acumulada (Fri%)",\
							"[7] - Ativar/Desativar - Ponto Médio (xi)",\
							"[8] - Retornar"]
							
abount = ["Esse script foi feito para fins didáticos,\nEstá bem estável pelo termux, \ndados inseridos somente dados inteiros\n       github: FelipeAlmeid4."]

def print_c(string, cor):
	""" Coloca cores no terminal"""
	global install_termcolor
	
	if install_termcolor and sys.platform == "linux":
		a = colored(str(string), cor)
		print(a)
	else:
		print(string)



#--------------------------------------------------------------------
def tables(data, ult_borda= False,title= "",separar_linhas=False):
		""" Recebe a tabela em formatos Matriz."""
		tables_terminal = AsciiTable(data)
		tables_terminal.inner_footing_row_border = ult_borda
		tables_terminal.inner_row_border = separar_linhas
		tables_terminal.title = title
		if tables_terminal.ok:
			print(tables_terminal.table)
		else:
			print("Tabela não pode ser visualizada, \n Recua o zoom ou aumente \n a janela do terminal e tente novamente.")


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
		os.system("reset")
		
	elif sys.platform == "win32":
		os.system("mode con cols=110 lines=80")
		os.system("cls")
		
# ----------------------------------------------------

def variance():
	#Variância amostral e populacional
	if len(process.list_fi) == 0:
		#Para dados brutos
		if process.sample:
			process.gerar_matriz_table((["i","xi", "xi-ㄡ", "|xi-ㄡ"]), False, 3)
			print(f"\nAmostra:↴\nVariância é {process.sum_x4}/{process.quant_xi-1} = {round(process.sum_x4/(process.quant_xi-1), process.decimal)}\n")
		if process.populational:
			process.gerar_matriz_table((["i","xi", "xi-ㄡ", "|xi-ㄡ"]) , False, 3)
			print(f"\nPopulação:↴\nVariância é {process.sum_x4}/{process.quant_xi} = {round(process.sum_x4/process.quant_xi,  process.decimal)}\n")
	else:
		#para dados Agrupados
		if process.sample:
			process.gerar_matriz_table((["i","fi", "xi","xi.fi", "xi-ㄡ", "(xi-ㄡ)²","fi.(xi-ㄡ)²"]) , True, 3)
			print(f"\nAmostra:↴\nVariância é {process.sum_fi_x4}/{process.quant_fi-1} = {round(process.sum_fi_x4/(process.quant_fi-1), process.decimal)}\n")
		if process.populational:
			process.gerar_matriz_table((["i", "fi", "xi","xi.fi", "xi-ㄡ", "(xi-ㄡ)²","fi.(xi-ㄡ)²"]), True, 3)
			print(f"\nPopulação:↴\nVariância é {process.sum_fi_x4}/{process.quant_fi} = {round(truncate(process.sum_fi_x4, process.decimal)/process.quant_fi, process.decimal)}\n")
		
#------------------------------------------------------
	
def arithmetic_mean(list_, grouped_data=False):
	""" Faz a operação para obter a média aritimética  e guarda na var x1."""
		
	total = func2.sum_list(list_)
	
	if grouped_data:
		#Para dados Agrupados
		process.sum_fi = round(func2.sum_list(process.list_fi), process.decimal)
		quantidade = process.sum_fi
	else:
		quantidade = len(list_)
		
	#process.x1 = truncate(total/quantidade, 5)
	process.x1 = Decimal(total/quantidade)

# ------------------------------------------------------------------------------

def standard_deviation():
	"""Desvio padrão para dados brutos."""
	
	#Escopo da tabela
	escopo = (["i", "xi", "xi-ㄡ","|xi-ㄡ|", "(xi-ㄡ)²"])
	
	process.gerar_matriz_table(escopo, False, 2)
	
	#Recebe o resultado da raiz
	dt = statistic.standard_deviation(process.sum_x4, process.list_x4)
		
	print(f"\n\tDesvio padrão é √({process.sum_x4}/{len(process.list_x4)}) = {round(dt, process.decimal)}")
	

def moda1(grouped=False):
	"""Verifica qual os números que mais se repete."""
	#https://pt.stackoverflow.com/questions/216413/identificar-elementos-repetidos-em-lista-com-python
	
	clear_()
	n = 1
	m = []
		
	if grouped:
		#Rastreia o número mais repetido
		for x in process.list_fi:
			if x > n:
				n = x
	else:
		#Rastreia o número mais repetido
		for x in process.list_xi:
			if process.list_xi.count(x) > n:
				n = process.list_xi.count(x)
		
		if n == 1:
			#Corrigi um bug quando não há modas em dados brutos
			print(f"\n\t {m} -- {process.modal[len(m)]}")
			return
	

	# Define o objeto que armazenará os índices de cada elemento:
	keys = defaultdict(list);
	
	if grouped:
		# Percorre todos os elementos da lista:
		for key, value in enumerate(process.list_fi):

  		  # Adiciona o índice do valor na lista de índices:
			keys[value].append(key)
	else:
		# Percorre todos os elementos da lista:
		for key, value in enumerate(process.list_xi):
			# Adiciona o índice do valor na lista de índices:
			keys[value].append(key)
			
	
	num = 0
	
	if grouped:
		# Extrai os valores que mais se repete
		for value in keys:
			if value >= num:
				num = value
				ind = keys[value]
		return ind, num
				
	else:
		# Extrai os valores que mais se repete
		for value in keys:
			if len(keys[value]) >= n:
				m.append(value)
	
	if grouped:
		pass
	else:
		print(f"\n\t {m} -- {process.modal[len(m)]}")
			
		
def moda2():
	""" Localiza  a classe modal."""
	
	
	n = 1
	for x in range(0, len(process.indice)):
		l = []
		l.append([f"     Moda  - Classe modal é {process.indice[x]+1}°", "Valores"])
		l.append(["Limite inferior da classe modal (lmo)", f"{process.lmo[x]}"])
		l.append(["Freq. Absoluta Simples Classe modal (fmo)", f"{process.value}"])
		l.append(["Freq. Absoluta Simples Classe Anterior (fant)", f"{process.ffant[x]}"])
		l.append(["Freq. Absoluta Simples Classe Posterior (fpost)" , f"{process.fpost[x]}"])
		l.append(["Amplitude da Classe Modal (c)", f"{process.amplitude}"])
		l.append([" ∆1 = lmo - fant", f"{process.value - process.ffant[x]}"])
		l.append([" ∆2 = lmo - fpost", f"{process.value - process.fpost[x]}"])
		delta_down = truncate(process.delta_1[x], process.decimal)+ truncate(process.delta_2[x], process.decimal)
		delta_up = truncate(process.delta_1[x], process.decimal)
		lmo = truncate(process.lmo[x], process.decimal)
		c = truncate(process.amplitude,process.decimal)
	
		base = delta_up/delta_down
		base = base*c
		base = lmo+base
		tables(data=l, separar_linhas=True)
		
		print(f"\n\t{n} - Moda é {round(base, process.decimal)}")
		
		n+=1
		

def mediana1():
	""" Calcula a mediana de uma lista de dados brutos"""
	#Recebe a lista em ordem crescente
	clear_()
	list_= statistic.rol_raw_data(process.list_xi)
	print(terminal.terminal_size(f" ROL: {list_} ", "━"))
	
	
	quantidade = len(process.list_xi)
	
	
	if quantidade%2==0:
		#Lista Par
		n = (quantidade//2)-1
		mediana = truncate((list_[n] + list_[-(n+1)])/2, process.decimal)
		print(f"\nLista Par:↴\n\tMediana é ({list_[n]} + {list_[-(n+1)]})/2 = {round(mediana, process.decimal)}")
	else:
		#Lista Impar
		n = (quantidade-1)//2
		mediana = list_[n]
		print(f"\nLista Ímpar:↴\n\tMediana é {mediana}")
		
# ---------------------------------------------------------------------
	
def standard_deviation2():
	"""Desvio padrão para dados Agrupados."""
	
	#Escopo da tabela
	escopo = (["i", "fi", "xi","xi.fi","xi-ㄡ","(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
	process.gerar_matriz_table(escopo, True, 2)
	
	if process.sample:
		dt = truncate(process.sum_fi_x4/process.sum_fi-1, process.decimal)
		dt = dt**Decimal("0.5")
		print(f"\nAmostra:↴\nDesvio padrão é √({process.sum_fi_x4}/{process.sum_fi-1}) = {round(dt, process.decimal)}")
	if process.populational:
		dt = truncate(process.sum_fi_x4/process.sum_fi, process.decimal)
		dt = dt**Decimal("0.5")
		print(f"\nPopulação:↴\nDesvio padrão é √({process.sum_fi_x4}/{process.sum_fi}) = {round(dt, process.decimal)}")
# -------------------------------------------------------------------------------

def average_mean_deviation1():
	""" Desvio médio simples dados brutos."""
	
	#Escopo da tabela
	escopo = (["i", "xi", "xi-ㄡ","|xi-ㄡ|"])
	process.gerar_matriz_table(escopo, False, 1)
	if process.sample:
		print(f"\nAmostra:↴\nDesvio médio simples é ({process.sum_x3}/{len(process.list_x3)-1}) = {round(process.sum_x3/len(process.list_x3)-1, process.decimal)}")
	if process.populational:
		print(f"\nPopulação:↴\nDesvio médio simples é ({process.sum_x3}/{len(process.list_x3)}) = {round(process.sum_x3/len(process.list_x3), process.decimal)}")
# ----------------------------------------------------------------------------

def average_mean_deviation2():
	""" Desvio médio simples dados agrupados."""
	
	#Escopo da tabela
	escopo = (["i", "fi", "xi", "xi.fi","|xi-ㄡ|", "fi.|xi-ㄡ|'"])
	process.gerar_matriz_table(escopo, True, 1)
	if process.sample:
		print(f"\nAmostra:↴\nDesvio médio simples é ({process.sum_fi_x3}/{process.sum_fi-1}) = {round(process.sum_fi_x3/process.sum_fi-1, process.decimal)}")
	if process.populational:
		print(f"\nPopulação:↴\nDesvio médio simples é ({process.sum_fi_x3}/{process.sum_fi}) = {round(process.sum_fi_x3/process.sum_fi, process.decimal)}")
	
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


def localizar_moda():
	""" Para Moda Agrupada"""
	process.indice, process.value = moda1(True) #Recebe o numero maior e seu indice
	
	xmin = process.initial
	amp = process.amplitude
	
	
	#Descobre o lmo
	for p in range(0, len(process.list_fi)):
		if p in process.indice:
			process.lmo.append(xmin)
		xmin += amp
	
	process.delta_1 =[]
	process.delta_2 = []
	process.ffant = []
	process.fpost =[]
	for x in range(0, len(process.indice)):
		
		#Cria ∆1
		fmo = process.value
		if process.indice[x] >= 1:
			process.delta_1.append(fmo - process.list_fi[process.indice[x]-1])
			process.ffant.append(process.list_fi[process.indice[x]-1])
		else:
			process.delta_1.append(process.value)
			process.ffant.append(0)
		
		#Cria ∆2
		fpost = []
		if process.indice[x] < len(process.list_fi)-1:
			process.delta_2.append(fmo - process.list_fi[process.indice[x]+1])
			process.fpost.append(process.list_fi[process.indice[x]+1])
		else:
			process.delta_2.append(fmo)
			process.fpost.append(0)
		
		
	
	
def mediana2():
	""" Media para dados agrupados"""
	#Elemento mediano 
	emd = truncate(process.sum_fi/2, process.decimal)
	
	
	#Extrai os dados (emd, fant, fmd, indice)
	for i, x in enumerate(process.list_Fi):
		if x >= emd:
			if i == 0:
				fant = 0
			else:
				fant = process.list_Fi[i-1]
			indice = i
			fmd = process.list_fi[i]
			break
		
	xmin = process.initial
	amp = process.amplitude
	
	for x in range(0, len(process.list_fi)):
		if x == indice:
			lmd = xmin
		else:
			xmin += amp
			
	for x in range(0, len(process.indice)):
		l = []
		l.append([f"     Mediana  - Classe Mediana é {indice+1}°", "Valores"])
		l.append(["Limite inferior da classe mediana (lmd)", f"{lmd}"])
		l.append(["Elemento Mediano (emd)", f"{emd}"])
		l.append(["Freq. Absoluta Acumulada Classe Anterior (fant)", f"{fant}"])
		l.append(["Freq. Absoluta Simples da Classe meidana (fmd)" , f"{fmd}"])
		l.append(["Amplitude da Classe Modal (c)", f"{process.amplitude}"])
	
	base = truncate((emd-fant)/fmd, process.decimal)
	base = truncate(process.amplitude, process.decimal)*truncate(base, process.decimal)
	base = truncate(base, process.decimal)+truncate(lmd, process.decimal)
	tables(data=l, separar_linhas=True)
	print(f"\n\tMediana  é {round(base, process.decimal)}")
	
# ------------------------------------------------------------------------------------------

def new_xi(initial, amplitude_class, amount_class):
	"""Cria Dados xi em process.list_xi com base na entrada. """
	
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
def config():
	"""Menu de configurações."""
	global commands3
	global modo_agrupados
	
	while 1:
		clear_()
		
		#Tabela de configuração
		print("\n")
		escopo = [ "Configurações", " Status"]
		process.gerar_matriz_table(escopo, None, 5)
		print("\n")
		for i, command in enumerate(commands3):
			if modo_agrupados == True:
				print(command)
			else:
				if i < 3 or len(commands3)-1 == i:
					print(command)
		
		resposta = str(input("Opção: "))
		
		if resposta == "1":
			casa_decimal()
			
		elif resposta == "2":
			if process.sample:
				if process.populational == False:
					process.populational = True
				process.sample= False
			else:
				process.sample = True
				
		elif resposta == "3":
			if process.populational:
				if process.sample == False:
					process.sample= True
				process.populational= False
			else:
				process.populational = True
				
		elif resposta == "4":
			if process.list_config[0] == False:
				process.list_config[0] = True
			else:
				process.list_config[0] = False
		
		elif resposta == "5":
			if process.list_config[1] == False:
				process.list_config[1] = True
			else:
				process.list_config[1] = False
		
		elif resposta == "6":
			if process.list_config[2] == False:
				process.list_config[2] = True
			else:
				process.list_config[2] = False
		
		elif resposta == "7":
			if process.list_config[3] == False:
				process.list_config[3] = True
			else:
				process.list_config[3] = False
		
		elif resposta == "8":
			break
		else:
			pass
			
		
		
		
		
# -------------------------------------------------------------------------------

def data_entry(raw_data):
	""" Onde colhe os dados Dados brutos e Agrupados."""
	
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
		print("Exemplo de Entradas:")
		print("\n\tfi:", end=" ")
		print_c( "18,31,15,10,7,5,4","red")
		print("\n\txi:\n\t  Xmin da 1° Classe:", end=" ")
		print_c("500", "red")
		print("\n\t  Amplitude_classe:", end=" ")
		print_c("200", "red")
		print("\n")
		
		string_fi = str(input("fi: ")).replace(" ", "")
		try:
			
			process.initial= float(input("Xmin da 1° Classe: "))
			process.amplitude= float(input("Amplitude da classe: "))
			
			#Recebe a lista fi desmembrada 
			process.list_fi = func2.dismemberment(string_fi)
			
			process.quant_fi = len(process.list_fi)
			
			#Calcula o xi com base nos dados de entrada e return uma lista
			process.list_xi = new_xi(process.initial, process.amplitude, process.quant_fi)
			
			#Calcula a quantidade de classes com base na process.list_xi
			process.quant_xi = len(process.list_xi)
			
			
			
			#Cria a lista nova xi.fi
			for x in range(0, len(process.list_fi)):
				process.list_fi_xi.append(truncate(process.list_xi[x]*process.list_fi[x], 2)) #xi.fi
			#Pegando a soma das listas
			process.sum_xi = func2.sum_list(process.list_xi)
			process.sum_fi = func2.sum_list(process.list_fi)
			process.sum_fi_xi = func2.sum_list(process.list_fi_xi)
			
		except:
			pass
		
		if len(process.list_xi) == 0 or process.list_fi == 0 or len(process.list_xi ) != len(process.list_fi):
			return
			
		else:
			#Gera a tabela de frequência
			clear_()
			print("\n")
			escopo = ["i", "Dados", "fi"]
			process.gerar_matriz_table(escopo, True, 4)
			input("...")



def dados_brutos_while():
	""" While dos dados brutos. """
	
	global is_raw_data
	global modo_1
	global commands2
	global modo_agrupados
	
	modo_agrupados = False
	process.modo_agrupados = False
	
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
			print(f"\n\t Amplitude Total {statistic.xmax} - {statistic.xmin}: {process.total_amplitude}\n")
					
		elif res2 == "2":
			# Desvio médio simples
			average_mean_deviation1()
				
				
		elif res2 == "3":
			# Desvio Padrão
			standard_deviation()
		
		elif res2 == "4":
			#Variância
			variance()
			
		elif res2 == "5":
			print(f"\n\tMédia aritmética: {process.sum_xi}/{len(process.list_xi)} = {truncate(process.x1, process.decimal)}\n")
		
		elif res2 == "5.1":
			error = 0
			while error < 2:
				try:
					string_fi = str(input("fi: ")).replace(" ","")
					process.list_fi = func2.dismemberment(string_fi)
					#Cria a lista nova xi.fi
					for x in range(0, len(process.list_fi)):
						process.list_fi_xi.append(truncate(process.list_xi[x]*process.list_fi[x], 2)) #xi.fi
					#Pegando a soma das listas
					process.sum_fi = func2.sum_list(process.list_fi)
					process.sum_fi_xi = func2.sum_list(process.list_fi_xi)
					error += 1
					if len(process.list_fi) > 0:
						copy = process.list_config
						process.list_config = [False, False, False, False, True]
						escopo = ["i", "xi", "fi"]
						process.gerar_matriz_table(escopo, True, 4, True)
						x1_p = process.sum_fi_xi/process.sum_fi
						print(f"\n\tMédia aritmética ponderada:{process.sum_fi_xi}/{process.sum_fi} = {round(x1_p, process.decimal)}\n")
						process.list_config = copy
						break
					else:
						return
				except:
					error += 1
					
			
		
		
		elif res2 == "6":
			moda1()
		
		elif res2 == "6.1":
			mediana1()
				
		elif res2 == "7":
			#Configurações
			config()
			
			
		elif res2 == "8":
			#Sair
			break
		else:
			continue
			
		input("...")
		
		
def dados_agrupados_while():
	""" While dos dados agrupados. """
	global modo_2
	global commands2_agr
	global modo_agrupados
	
	modo_agrupados = True
	process.modo_agrupados = True
	
	while 1:
		clear_()
		process.lmo = []
		#Ajuda alocalizar a classe modal e já antecipa os dados
		localizar_moda()
	
		
		
		process.total_amplitude = statistic.total_amplitude2(process.initial, process.amplitude, process.quant_fi)
		#Escopo do menu Dados agrupados
		print(terminal.terminal_size(modo_2, "="))
		print(terminal.terminal_size(f" Amostra: {process.sample} ", "-"))
		print(terminal.terminal_size(f" População: {process.populational} ", "-"))
		print(terminal.terminal_size(f"fi:{process.list_fi}", " "))
		print(terminal.terminal_size(f"xi:{process.list_xi}", " "))
		print("\n")
				
		for command in commands2_agr:
			print(command)
					
		res2 = input("Opção: ")
				
		if res2 =="1":
			#Amplitude total - Dados Agrupados
			print(f"\n\t Amplitude Total {statistic.xmax} - {statistic.xmin}: {process.total_amplitude}\n")
					
		elif res2 == "2":
			#Desvio médio simples - Dados Agrupados
			average_mean_deviation2()
			
		elif res2 == "3":
			standard_deviation2()
			
		elif res2 == "4":
			#Variância
			variance()
			
		elif res2 == "5":
			#Média aritmetica
			copy = process.list_config
			process.list_config = [False, False, False, True, True]
			escopo = ["i", "Dados", "fi"]
			process.gerar_matriz_table(escopo, True, 4)
			print(f"\n\tMédia aritmética:{process.sum_fi_xi}/{process.sum_fi} = {truncate(process.x1, process.decimal)}\n")
			process.list_config = copy
		elif res2 == "5.1":
			moda2()
		
		elif res2 == "5.2":
			mediana2()
			
		elif res2 == "6":
			#Configurações
			config()
			continue
		
		elif res2 == "7":
			#Visualizar tabela Dados agrupados
			clear_()
			print("\n")
			escopo = ["i", "Dados", "fi"]
			process.gerar_matriz_table(escopo, True, 4)
			
		elif res2 == "8":
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
	print(terminal.terminal_size(" Estatística ", "+"))
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
		if install_terminaltables:
			l = [["Sobre"], abount]
			tables(l)
		else:
			print(f"\nSobre:\n\t{abount[0]}")
		input("...")
	
	
	elif res1 == "4":
		print_c("\nATENÇÃO:\n", "red")
		print("  Xmin é o número menor da 1° classe P/ Dados Agrupados.\n")
		print("  Amplitude da classe é a distância de um Xmin ao Xmax da \n  mesma classe. Ex: 500|----700 --> 200")
		input("...")
			
		
	elif res1 == "5":
		modo_agrupados = False
		process.modo_agrupados = False
		config()
			
		
	elif res1 == "6":
		#Sai do script
		print(":)")
		break
		
	
		
		




