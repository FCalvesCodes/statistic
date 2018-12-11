#! data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-


from mod.modo_audit import ModoAudit
from collections import defaultdict
from mod.func2 import Process
from mod.func import Statistic
from decimal import Decimal, Context
from mod import terminal 
from mod import func2
import decimal
import time
import math
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
	print("\nInstale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)
	
	
statistic = Statistic()
process =  Process()

math_decimal = Context()

#Para fazer auditoria das variáveis(Em Desenvolvimento)
#modoaudit = ModoAudit(process)

#Var para confirgurar entre dados brutos e dados agruapdos
modo_agrupados = None


modo_1 = "Modo Dados Brutos"
modo_2 = "Modo Dados Agrupados"

# -------------- Variáveis em geral ------------------


commands1 = ["[1] - Dados Brutos",\
								"[2] - Dados Agrupados",\
								"[3] - Sobre",\
								"[4] - Informações",\
								"[5] - Configurações",\
							    "[6] - Sair"]

commands2_agr = ["[1]  -  Amplitude Total",\
								"[2]  -  Desvio Médio Simples",\
								"[3]  -  Desvio Padrão",\
								"[4]  -  Variância",\
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
								"[6]  -  Moda",\
								"[6.1] - Mediana",\
								"[6.2] - Erro Padrão (Em desenvolvimento)",\
								"[6.3] - Adicionar (fi)", \
								"[7]  -  Configurações",\
								"[8]  -  Retornar"]

#Indice proibidos de ser exibidos antes de adicionar (fi)
command_no_authorized = [5]

commands3 = ["[1] - Ajustar Casa Decimal",\
							"[2] - Ativar/Desativar - Amostra",\
							"[3] - Ativar/Desativar - População",\
							"[4] - Ativar/Desativar - Freq. Relativa (fri%)",\
							"[5] - Ativar/Desativar - Freq. Absoluta Acumulada (Fi)",\
							"[6] - Ativar/Desativar - Freq. Relativa Acumulada (Fri%)",\
							"[7] - Ativar/Desativar - Ponto Médio (xi)",\
							"[8] - Retornar"]
							
abount = ["Esse script foi feito para fins didáticos,\n está bem estável pelo termux.\n              github: FelipeAlmeid4."]

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
			
# ------------------------------------------------------------------------------

def truncate(f, n):
    '''Truncates/pads a float f to n process.decimal places without rounding'''
    #https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return Decimal('{0:.{1}f}'.format(f, n))
    i, p, d = s.partition('.')
    return Decimal('.'.join([i, (d+'0'*n)[:n]]))

# ------------------------------------------------------------------------------

def zero():
	process.lmo = statistic.tr(process.lmo)
	process.value = statistic.tr(process.value)
	process.ffant = statistic.tr(process.ffant)
	process.fpost = statistic.tr(process.fpost)
	process.delta_2 =  statistic.tr(process.delta_2)
	process.delta_1 = statistic.tr(process.delta_1)
	process.amplitude = statistic.tr(process.amplitude)

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
	global modo_agrupados
	#Variância amostral e populacional
	if modo_agrupados == False:
		#Para dados brutos
		process.gerar_matriz_table((["i","xi", "xi-ㄡ", "|xi-ㄡ"]), False, 3)
		if process.sample:
			n = math_decimal.divide(process.sum_x4, process.quant_xi-1)
			print(f"\nAmostra:↴\nVariância é ({process.sum_x4}/{process.quant_xi-1}) = {round(n, process.decimal)}\n")
		if process.populational:
			n = math_decimal.divide(process.sum_x4, process.quant_xi)
			print(f"\nPopulação:↴\nVariância é ({process.sum_x4}/{process.quant_xi}) = {round(n,  process.decimal)}\n")
	else:
		#para dados Agrupados
		
		process.gerar_matriz_table((["i","fi", "xi","xi.fi", "xi-ㄡ", "(xi-ㄡ)²","fi.(xi-ㄡ)²"]) , True, 3)
		if process.sample:
			n = math_decimal.divide(process.sum_fi_x4, process.sum_fi-1)
			print(f"\nAmostra:↴\nVariância é ({process.sum_fi_x4}/{process.sum_fi-1}) = {round(n, process.decimal)}\n")
		if process.populational:
			n = math_decimal.divide(process.sum_fi_x4, process.quant_xi)
			print(f"\nPopulação:↴\nVariância é ({process.sum_fi_x4}/{process.sum_fi}) = {round(n, process.decimal)}\n")
		
#------------------------------------------------------------------------------
	
def arithmetic_mean(list_):
	""" Faz a operação para obter a média aritimética  e guarda na var x1."""
	global modo_agrupados
	total = func2.sum_list(list_)
	
	if modo_agrupados:
		#Para dados Agrupados
		process.sum_fi = func2.sum_list(process.list_fi)
		quantidade = process.sum_fi
	else:
		quantidade = len(list_)
		
	#process.x1 = truncate(total/quantidade, 5)
	process.x1 = truncate(math_decimal.divide(total, quantidade), process.decimal)
def error_padr():
	""" Erro padrão dados brutos"""
	pass

# ------------------------------------------------------------------------------

def standard_deviation():
	"""Desvio padrão para dados brutos."""
	
	#Escopo da tabela
	escopo = (["i", "xi", "xi-ㄡ","|xi-ㄡ|", "(xi-ㄡ)²"])
	
	process.gerar_matriz_table(escopo, False, 2)
	
	if process.sample:
		dt = Decimal(f"{process.sum_x4}")/Decimal(f"{process.quant_xi-1}")
		dt = math.sqrt(dt)
		print(f"\nAmostra:↴\nDesvio padrão é √({process.sum_x4}/{process.quant_xi-1}) = {round(dt, process.decimal)}")
	if process.populational:
		dt1 = Decimal(f" {process.sum_x4}")/Decimal(f"{process.quant_xi}")
		dt1 = math.sqrt(dt1)
		print(f"\nPopulação:↴\nDesvio padrão é √({process.sum_x4}/{process.quant_xi}) = {round(dt1, process.decimal)}")
	
# ------------------------------------------------------------------------------

def moda1():
	"""Verifica qual os números que mais se repete."""
	#https://pt.stackoverflow.com/questions/216413/identificar-elementos-repetidos-em-lista-com-python
	global modo_agrupados
	
	clear_()
	n = 1
	m = []
		
	if modo_agrupados:
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
	
	if modo_agrupados:
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
	
	if modo_agrupados:
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
	
	if modo_agrupados:
		pass
	else:
		print(f"\n\t {m} -- {process.modal[len(m)]}")

# ------------------------------------------------------------------------------
		
def moda2():
	""" Localiza  a classe modal."""
	
	zero()
	
	#Reconfigura a lista de config para tabela
	copy = process.list_config
	process.list_config = [False, False, False, False, False]
	escopo = ["i", "Dados", "fi"]
	process.gerar_matriz_table(escopo, True, 4)
	process.list_config = copy
	
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
		delta_down = Decimal(f"{process.delta_1[x]}")+Decimal(f"{process.delta_2[x]}")
		delta_up = Decimal(f"{process.delta_1[x]}")
		lmo = Decimal(f"{process.lmo[x]}")
		c = Decimal(f"{process.amplitude}")
	
		base = Decimal(f"{delta_up}")/Decimal(f"{delta_down}")
		base = Decimal(f"{base}")*Decimal(f"{c}")
		base = Decimal(f"{lmo}")+Decimal(f"{base}")
		
		tables(data=l, separar_linhas=True)
		
		print(f"\n\t{n} - Moda é {round(base, process.decimal)}")
		
		n+=1
		
# ------------------------------------------------------------------------------

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
		
# -------------------------------------------------------------------------------------
	
def standard_deviation2():
	"""Desvio padrão para dados Agrupados."""
	
	#Escopo da tabela
	escopo = (["i", "fi", "xi","xi.fi","xi-ㄡ","(xi-ㄡ)²", "fi.(xi-ㄡ)²"])
	process.gerar_matriz_table(escopo, True, 2)
	
	if process.sample:
		dt = Decimal(f" {process.sum_fi_x4}")/Decimal(f"{process.sum_fi-1}")
		dt = dt**Decimal("0.5")
		print(f"\nAmostra:↴\nDesvio padrão é √({process.sum_fi_x4}/{process.sum_fi-1}) = {round(dt, process.decimal)}")
	if process.populational:
		dt = Decimal(f"{process.sum_fi_x4}")/Decimal(f"{process.sum_fi}")
		dt = dt**Decimal("0.5")
		print(f"\nPopulação:↴\nDesvio padrão é √({process.sum_fi_x4}/{process.sum_fi}) = {round(dt, process.decimal)}")
# ----------------------------------------------------------------------------

def average_mean_deviation():
	""" Desvio médio simples dados agrupados e dados brutos."""
	global modo_agrupados
	
	if modo_agrupados:
		"""Dados Agrupados."""
		#Escopo da tabela
		escopo = (["i", "fi", "xi", "xi.fi","|xi-ㄡ|", "fi.|xi-ㄡ|'"])
		process.gerar_matriz_table(escopo, True, 1)
		if process.sample:
			print(f"\nAmostra:↴\nDesvio médio simples é ({process.sum_fi_x3}/{process.sum_fi-1}) = {round(Decimal(process.sum_fi_x3)/Decimal(process.sum_fi-1), process.decimal)}")
		if process.populational:
			print(f"\nPopulação:↴\nDesvio médio simples é ({process.sum_fi_x3}/{process.sum_fi}) = {round(Decimal(process.sum_fi_x3)/Decimal(process.sum_fi), process.decimal)}")
	else:
		""" Dados brutos."""
		#Escopo da tabela
		escopo = (["i", "xi", "xi-ㄡ","|xi-ㄡ|"])
		process.gerar_matriz_table(escopo, False, 1)
		if process.sample:
			print(f"\nAmostra:↴\nDesvio médio simples é ({process.sum_x3}/{len(process.list_x3)-1}) = {round(process.sum_x3/len(process.list_x3)-1, process.decimal)}")
		if process.populational:
			print(f"\nPopulação:↴\nDesvio médio simples é ({process.sum_x3}/{len(process.list_x3)}) = {round(process.sum_x3/len(process.list_x3), process.decimal)}")
	
# ------------------------------------------------------------------------------------------


def casa_decimal():
	""" Atualiza a casa process.decimal."""
	try:
		process.decimal = int(input("Digite entre 1 a 5: "))
		if process.decimal > 5 or process.decimal < 1:
			process.decimal = 2
			basic.process.decimal = 2
		else:
			process.decimal = process.decimal
	except:
		pass


def localizar_moda():
	""" Moda para dados Agrupados"""
	process.lmo = []
	process.indice, process.value = moda1() #Recebe o numero maior e seu indice
	
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

# ------------------------------------------------------------------------------
	
def mediana2():
	""" Media para dados agrupados"""
	zero()
	#Elemento mediano 
	emd = Decimal(f"{process.sum_fi}")/Decimal("2")
	
	#Extrai os dados (emd, fant, fmd, indice)
	for i, x in enumerate(process.list_Fi):
		if x >= emd:
			if i == 0:
				fant = 0
			else:
				fant = process.list_Fi[i-1]
			indice, fmd = i, process.list_fi[i]
			break
		
	xmin = statistic.tr(process.initial)
	amp = statistic.tr(process.amplitude)
	
	for x in range(0, len(process.list_fi)):
		if x == indice:
			lmd = xmin
		else:
			xmin += amp
	
	
	#Reconfigura a lista de config para tabela
	copy = process.list_config
	process.list_config = [False, True, False, False, False]
	escopo = ["i", "Dados", "fi"]
	process.gerar_matriz_table(escopo, True, 4)
	process.list_config = copy
	
	for x in range(0, len(process.indice)):
		l = []
		l.append([f"     Mediana  - Classe Mediana é {indice+1}°", "Valores"])
		l.append(["Limite inferior da classe mediana (lmd)", f"{lmd}"])
		l.append(["Elemento Mediano (emd)", f"{emd}"])
		l.append(["Freq. Absoluta Acumulada Classe Anterior (fant)", f"{fant}"])
		l.append(["Freq. Absoluta Simples da Classe meidana (fmd)" , f"{fmd}"])
		l.append(["Amplitude da Classe Modal (c)", f"{process.amplitude}"])
	
	base = Decimal(f"{emd-fant}")/Decimal(f"{fmd}")
	base = Decimal(f"{process.amplitude}")*Decimal(f"{base}")
	base = Decimal(f"{base}")+Decimal(f"{lmd}")
	tables(data=l, separar_linhas=True)
	print(f"\n\tMediana  é {round(base, process.decimal)}")
	
# ------------------------------------------------------------------------------------------

def new_xi(initial, amplitude_class, amount_class):
	"""Cria Dados xi em process.list_xi com base na entrada. """
	
	list_ = []
	for x in range(0, amount_class):
		if str(initial+(amplitude_class/2)):
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

def weighted_average():
	"""Média aritmética ponderada"""
	#Cria a lista nova xi.fi
	process.list_fi_xi = []
	for x in range(0, len(process.list_fi)):
		process.list_fi_xi.append(truncate(process.list_xi[x]*process.list_fi[x], 2)) #xi.fi
	#Pegando a soma das listas
	process.sum_fi = func2.sum_list(process.list_fi)
	process.sum_fi_xi= func2.sum_list(process.list_fi_xi)
	if len(process.list_fi) > 0:
		copy = process.list_config
		process.list_config = [False, False, False, False, True]
		escopo = ["i", "xi", "fi"]
		process.gerar_matriz_table(escopo, True, 4, True)
		x1_p = process.sum_fi_xi/process.sum_fi
		print(f"\n\tMédia aritmética ponderada: ({process.sum_fi_xi}/{process.sum_fi}) = {round(x1_p, process.decimal)}\n")
		process.list_config = copy
	else:
		print("Erro no processo.")
	


def adc_fi():
	""" adiciona o fi para dados brutos """
	global command_no_authorized
	
	try:
		string_fi = str(input("fi: ")).replace(" ","")
		process.list_fi = func2.dismemberment(string_fi)
	except:
		print("Dados inválidos!")
	
	if len(process.list_fi) == len(process.list_xi):
		pass
	else:
		process.list_fi = []
		print(" Dados faltando !")
		
		
# -------------------------------------------------------------------------------

def data_entry(raw_data):
	""" Onde colhe os dados Dados brutos e Agrupados."""
	
	#Para dados brutos
	if raw_data == True:
		process.list_fi_xi = []
		print("\nExemplo de Entrada:\n\txi: ", end= "")
		print_c("14,15,19,20,20,21,22\n", "red")
		
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
			process.list_xi = statistic.tr(process.list_xi)
			
			#Calcula a quantidade de classes com base na process.list_xi
			process.quant_xi = len(process.list_xi)
			process.list_fi_xi = []
			
			#Cria a lista nova xi.fi para média aritmetica dados agrupados
			for x in range(0, len(process.list_fi)):
				process.list_fi_xi.append(Decimal(f"{process.list_xi[x]}")*Decimal(f"{process.list_fi[x]}")) #xi.fi
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
			escopo = ["i", "  Dados", "fi", "xi"]
			process.gerar_matriz_table(escopo, True, 4)
			input("...")

# ------------------------------------------------------------------------------

def dados_brutos_while():
	""" While dos dados brutos. """
	global modo_1
	global commands2
	global modo_agrupados
	
	modo_agrupados = False
	process.modo_agrupados = False
	process.list_fi = []
	
	while 1:
		
		# Calcula a média aritmética
		arithmetic_mean(process.list_xi)
		process.total_amplitude = statistic.total_amplitude1(process.list_xi)
		process.start(modo_agrupados)
		clear_()
		
		print(terminal.terminal_size(modo_1, "="))
		print(terminal.terminal_size(f" Amostra: {process.sample} ", "-"))
		print(terminal.terminal_size(f" População: {process.populational} ", "-"))
		print(terminal.terminal_size(f"xi:{process.list_xi}", " "))
		if len(process.list_fi) == len(process.list_xi):
			print_c(terminal.terminal_size(f"fi:{process.list_fi}", " "), "yellow")
		print("\n")
		
		
		for indice, command in enumerate(commands2):
			if len(process.list_fi) > 0 and indice in command_no_authorized:
				print_c(command, "yellow")
			else:
				if not indice in command_no_authorized:
					print(command)
			
		try:
			res2 = input("Opção: ")
		except:
			pass
				
		if res2 == "1":
			#Amplitude total
			print(f"\n\t Amplitude Total ({statistic.xmax} - {statistic.xmin}): {process.total_amplitude}\n")
					
		elif res2 == "2":
			# Desvio médio simples
			average_mean_deviation()
				
				
		elif res2 == "3":
			# Desvio Padrão
			standard_deviation()
		
		elif res2 == "4":
			#Variância
			variance()
			
		elif res2 == "5":
			print(f"\n\tMédia aritmética: ({process.sum_xi}/{len(process.list_xi)}) = {truncate(process.x1, process.decimal)}\n")
		
		elif res2 == "5.1"and len(process.list_fi) == len(process.list_xi):
			weighted_average()
					
		elif res2 == "6":
			moda1()
		
		elif res2 == "6.1":
			mediana1()
			
		elif res2 == "6.2":
			pass
		
		elif res2 == "6.3":
			adc_fi()
			if len(process.list_fi) == len(process.list_xi):
				continue
			
		elif res2 == "7":
			#Configurações
			config()
			continue
			
			
		elif res2 == "8":
			#Sair
			break
		else:
			continue
			
		input("...")

# ------------------------------------------------------------------------------
		
def dados_agrupados_while():
	""" While dos dados agrupados. """
	global modo_2
	global commands2_agr
	global modo_agrupados
	
	modo_agrupados = True
	process.modo_agrupados = True
	
	#Ajuda alocalizar a classe modal e já antecipa os dados
	localizar_moda()
	
	while 1:
		#Calcula a média aritmética
		arithmetic_mean(process.list_fi_xi)
		process.total_amplitude = statistic.total_amplitude2(process.initial, process.amplitude, process.quant_fi)
		process.start(modo_agrupados)
		clear_()
	
		#Escopo do menu Dados agrupados
		print(terminal.terminal_size(modo_2, "="))
		print(terminal.terminal_size(f" Amostra: {process.sample} ", "-"))
		print(terminal.terminal_size(f" População: {process.populational} ", "-"))
		print(terminal.terminal_size(f"fi:{process.list_fi}", " "))
		print(terminal.terminal_size(f"xi:{process.list_xi}", " "))
		print("\n")
				
		for command in commands2_agr:
			print(command)
		
		try:
			res2 = input("Opção: ")
		except:
			pass
			
		if res2 =="1":
			#Amplitude total - Dados Agrupados
			print(f"\n\t Amplitude Total ({statistic.xmax} - {statistic.xmin}): {process.total_amplitude}\n")
					
		elif res2 == "2":
			#Desvio médio simples - Dados Agrupados
			average_mean_deviation()
			
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
			print(f"\n\tMédia aritmética: ({process.sum_fi_xi}/{process.sum_fi}) = {truncate(process.x1, process.decimal)}\n")
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
		
	try:
		res1 = input("Opção: ")
	except EOFError:
		pass

	
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
		
	
		
		




