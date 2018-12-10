# -*- coding: utf-8 -*-


from mod.func import Statistic
from decimal import Decimal
from mod import terminal
import string
import sys
import time

statistic = Statistic()

try:
	from termcolor import colored
	install_termcolor = True
except:
	install_termcolor = False


def truncate(f, n):
	'''Truncates/pads a float f to n decimal places without rounding'''
	#https://pt.stackoverflow.com/questions/176243/como-limitar-números-decimais-em-python
	s = '{}'.format(f)
	if 'e' in s or 'E' in s:
		return Decimal('{0:.{1}f}'.format(f, n))
	i, p, d = s.partition('.')
	return Decimal('.'.join([i, (d+'0'*n)[:n]]))
	

def dismemberment(string):
		""" Pega uma string com números separados por vírgula e retorna lista com os números  separados. """
		list_ = []
		text = ""
			
		for i, letter in enumerate(string):
			if letter == "," or i == len(string)-1:
				if i == len(string)-1:
					text += letter
				try:
					list_.append(int(text))
					text = ""
				except:
					print("Error ao verificar dados.")
					return []
			else:
				text += letter
		return list_
		

def sum_list(list_):
	""" Faz a soma de uma lista com números."""
	if len(list_) < 2:
		return 0
	sum = 0
	for n in list_:
		sum += Decimal(str(n))
	return sum

	
	

class Process(object):
	def __init__(self):
		#Variáveis de entrada de dados
		self.amplitude = 0	# Amplitude da classe
		self.initial = 0			#xmin da classe
		
		self.xmin = 0				# Valor Minimo
		self.xmax = 0			   # Valor maximo
		
		self.x1= 0			        # Média aritmética
		
		
		self.sum_xi = 0		  # Σxi
		self.sum_fi = 0	  	 # Σfi
		self.sum_fi_xi = 0	  # Σxi.fi
		self.sum_x3 = 0		 # Σ|xi - "x-barra"|
		self.sum_x4 = 0		 # Σ(xi - "x-barra")²
		self.sum_fi_x3 = 0     # Σfi.|xi - "x-barra"|
		self.sum_fi_x4 = 0	 # Σfi.(xi - "x-barra")²
		
		
		self.quant_xi = 0 	   #quantidade de dados em list_fi
		self.quant_fi = 0        #quantidade de dados em list_fi
		
		self.decimal = 2		# Casas decimais padrão
		self.total_amplitude = 0    # Amplitude total xmax-xmin
		self.initial = 0			#xmin da primeira classe
		
		
		self.list_xi = []		   # xi
		self.list_fi = []		   # fi
		self.list_fi_xi = []      # xi.fi
		self.list_x2 = []		 # xi - "x-barra"
		self.list_x3 = []		  # |xi - "x-barra"|
		self.list_x4 = []		  # (xi - "x-barra")²
		self.list_fi_x3 = [] 	# fi.|xi - "x-barra"|
		self.list_fi_x4 = [] 	# fi.(xi - "x-barra")²
		self.list_fri = []         # fri% - Freq. Relativa %
		self.list_Fi = []          # Fi  - Freq. Absoluta Acumulado
		self.list_Fri = []        # Fri - Freq. Relativa Acumulada %
		
		#Amostral e populacional
		self.sample = False
		self.populational = True

		#Dados Agrupados - Moda
		self.lmo = []			# Limite inferior da classe modal
		self.indice = []		# Onde está localizada a classe modal
		self.value = 0  	   # fmo
		self.ffant =[]		   #
		self.fpost= []		  #
		self.delta_2 = []	 #
		self.delta_1 = []	 #
		self.amplitude	   # c
		self.modal = ["Amodal", "Unimodal", "Bimodal", "Trimodal", "Quadrimodal"]
		
		#Configurações para visualizar tabela de frequencia
		#0 - fri%     1- Fi        2 - Fri%     3 - xi     4 - xi.fi
		self.list_config = [False, False, False, True, False]
		
		#Configura os dados do menu configurações
		self.modo_agrupados = None
		
	def f_c(self, string):
		if sys.platform == "linux":
			try:
				if string == True:
					return colored(str(string), "green")
				elif string == False:
					return colored(str(string), "red")
			except:
					return string
		else:
			return string
	
	def start(self, grouped):
		""" Faz todo procedimento de calcular e guarda nas variáveis"""
		
		#Reset as listas
		self.list_x2, self.list_x3, self.list_x4,self.list_fi_x3, self.list_fi_x4, self.list_fri, self.list_Fri, self.list_Fi = [],[],[],[],[],[],[],[]
		
		n = 0 #Auxilia a criação da lista Fi
		b = 0 #Auxilia na criação da lista Fri
	
		for x in range(0, len(self.list_xi)):
			
			self.list_x2.append(truncate(Decimal(str(self.list_xi[x])) - self.x1, self.decimal)) #xi-ㄡ
			self.list_x3.append(abs(self.list_x2[x])) #|xi-ㄡ|
			self.list_x4.append(truncate(Decimal(str(self.list_x3[x]))**2, self.decimal)) #(xi-ㄡ)²
			
			if grouped == True:
				
				self.list_fi_x3.append(truncate(self.list_fi[x]*Decimal(str(self.list_x3[x])), self.decimal)) #fi.|xi-ㄡ|
				self.list_fi_x4.append(truncate(self.list_fi[x]*Decimal(str(self.list_x4[x])), self.decimal)) #fi.(xi-ㄡ)²
				
				base = self.list_fi[x]*100
				self.list_fri.append(round(Decimal(str(base))/self.sum_fi)) #fri%
				
				n += self.list_fi[x]
				self.list_Fi.append(n) #Fi
				
				base = self.list_fi[x]*100
				b += round(Decimal(str(base))/self.sum_fi)
				self.list_Fri.append(b) #Fri%
			
			#Recebe as somas
			self.sum_xi = sum_list(self.list_xi)
			self.sum_fi = sum_list(self.list_fi)
			self.sum_x3 = sum_list(self.list_x3)
			self.sum_x4 = sum_list(self.list_x4)
			self.sum_fi_x4 = sum_list(self.list_fi_x4)
			self.sum_fi_x3 = sum_list(self.list_fi_x3)
			self.sum_fi_xi = sum_list(self.list_fi_xi)
		
	def gerar_matriz_table(self, escopo, grouped, modo, is_weighted=False ):
		""" Cria uma matriz para terminaltables"""
		
		#Passa o valor para classe (True ou False)
		self.install_terminaltables = terminal.status()
		
		#Adiciona ao escopo mais conteúdo
		if grouped == True and modo == 4:
			if self.list_config[0] == True and self.modo_agrupados:
				escopo.append("fri %")
			if self.list_config[1] == True and self.modo_agrupados:
				escopo.append("Fi")
			if self.list_config[2] == True and self.modo_agrupados:
				escopo.append("Fri %")
			if self.list_config[3] == True and self.modo_agrupados:
				escopo.append("xi")
			if self.list_config[-1] == True: #Reservado para um proposito
				escopo.append("xi.fi")
		
		#Será a manipulação de xmin|-------xmin+amplitude
		xmin = statistic.tr(self.initial)
		amplitude = statistic.tr(self.amplitude)
		
		tabela = []  # matriz
		tabela.append(escopo)	#Titulo da tabela
		
		
		ind = 0	#Indice para configurar a tabela
		
		#Tabela de configurações - lista  em constante atualização
		self.list_config2 = [["Casa Decimal",f"{self.decimal}"], ["Amostra", self.f_c(self.sample)], ["População", self.f_c(self.populational)], ["fri %", self.f_c(self.list_config[0])], ["Fi", self.f_c(self.list_config[1])], ["Fri %", self.f_c(self.list_config[2])], ["xi", self.f_c(self.list_config[3])]]
		
		#Gerar uma matriz para configurações
		if grouped == None and modo == 5:
			for x in range(0, len(self.list_config2)):
				if self.modo_agrupados:
					tabela.append(self.list_config2[x])
				else:
					if x < 3:
						tabela.append(self.list_config2[x])
			terminal.tables(tabela, True," " , True)
			tabela = []
			return

############## Dados Brutos ##############
		#Monta as matriz
		for x in range(0, len(self.list_xi)):

			if grouped == False and modo == 1:
				#Dados Brutos - Desvio médio simples
				tabela.append([x+1, truncate(self.list_xi[x], self.decimal), truncate(self.list_x2[x],self.decimal), truncate(self.list_x3[x], self.decimal)])
				
			elif grouped == False and modo == 2:
				#Dados Brutos - Desvio Padrão
				tabela.append([x+1, truncate(self.list_xi[x], self.decimal), truncate(self.list_x2[x],self.decimal), truncate(self.list_x3[x], self.decimal), truncate(self.list_x4[x], self.decimal)])
			
			elif grouped == False and modo == 3:
				#Dados Brutos - Variância
				tabela.append([x+1, truncate(self.list_xi[x], self.decimal), truncate(self.list_x2[x],self.decimal), truncate(self.list_x4[x], self.decimal)])

############# Dados Agrupados #################
			
			elif grouped == True and modo == 1:
				#Dados Agrupados - Desvio médio simples
				tabela.append([x+1, self.list_fi[x], truncate(self.list_xi[x], self.decimal), truncate(self.list_fi_xi[x], self.decimal), truncate(self.list_x3[x], self.decimal), truncate(self.list_fi_x3[x], self.decimal)])
		
			elif grouped == True and modo == 2:
				#Dados Agrupados - Desvio padrão
				tabela.append([x+1, truncate(self.list_fi[x], self.decimal), truncate(self.list_xi[x], self.decimal), truncate(self.list_fi_xi[x], self.decimal), truncate(self.list_x2[x],self.decimal), truncate(self.list_x4[x], self.decimal), truncate(self.list_fi_x4[x], self.decimal)])
				
			elif grouped == True and modo == 3:
				#Dados Agrupados - Variância
				tabela.append([x+1, truncate(self.list_fi[x], self.decimal), truncate(self.list_xi[x], self.decimal), truncate(self.list_fi_xi[x],self.decimal), truncate(self.list_x2[x],self.decimal), truncate(self.list_x4[x], self.decimal), truncate(self.list_fi_x4[x], self.decimal)])
				
			elif grouped == True and modo == 4:
				#Dados Agrupados - Tabela de frêquencia
				if is_weighted:
					tabela.append([x+1, truncate(self.list_xi[x], self.decimal), truncate(self.list_fi[x], self.decimal)])
				else:
					xmin += amplitude
					tabela.append([x+1, f"{xmin-amplitude}|-----{xmin}", self.list_fi[x]])
				
				if self.list_config[0] == True:
					#Adicionar os dados
					tabela[x+1].append(self.list_fri[x])
				
				if self.list_config[1] == True:
					tabela[x+1].append(self.list_Fi[x])
		
				if self.list_config[2] == True:
					tabela[x+1].append(self.list_Fri[x])
				
				if self.list_config[3] == True:
					tabela[x+1].append(truncate(self.list_xi[x], self.decimal))
				
				if self.list_config[-1] == True:
					tabela[x+1].append(self.list_fi_xi[x])
				
			
		
		
	
		if grouped == False and modo == 1 and self.install_terminaltables:
			#Dados Brutos - Desvio médio simples
			tabela.append([" ", self.sum_xi, "    Σ", self.sum_x3])
			terminal.tables(tabela, True, "Dados Brutos - Desvio médio simples")
			
		elif grouped == False and modo == 2 and self.install_terminaltables:
			#Dados brutos - Desvio padrão
			tabela.append([" ", self.sum_xi, "Σ",self.sum_x3, self.sum_x4])
			terminal.tables(tabela, True,"Dados brutos - desvio padrão")
			
		elif grouped == False and modo == 3 and self.install_terminaltables:
			#Dados brutos - Variância
			tabela.append([" ", self.sum_xi, "Σ", self.sum_x4])
			terminal.tables(tabela, True,"Dados brutos - Variância")
			
		elif grouped == True and modo == 1 and self.install_terminaltables:
			#Dados agrupados - Desvio médio  simples
			tabela.append([" ", self.sum_fi, self.sum_xi, self.sum_fi_xi, self.sum_x3, self.sum_fi_x3])
			terminal.tables(tabela, True,"Dados Agrupados - Desvio médio simples")
			
		elif grouped == True and modo == 2 and self.install_terminaltables:
			#Dados agrupados - Desvio padrão
			tabela.append([" ", self.sum_fi, self.sum_xi,self.sum_fi_xi, "Σ", self.sum_x4, self.sum_fi_x4])
			terminal.tables(tabela, True,"Dados Agrupados - desvio padrão")
			
		elif grouped == True and modo == 3 and self.install_terminaltables:
			tabela.append([" ", self.sum_fi, self.sum_xi, self.sum_fi_xi, "Σ", self.sum_x4, self.sum_fi_x4])
			terminal.tables(tabela, True,"Dados Agrupados - Variância")
			
		elif grouped == True and modo == 4 and self.install_terminaltables:
			#Dados Agrupados - Tabela de frêquencia
			if is_weighted:
				#Caso seja para média ponderada
				tabela.append([" ", self.sum_xi, self.sum_fi])
			else:
				tabela.append([" ", " Σ ", self.sum_fi])
			
			if self.list_config[0] == True:
				#Adicionar os dados
				tabela[-1].append(" ")
				
			if self.list_config[1] == True:
				tabela[-1].append(" ")
		
			if self.list_config[2] == True:
				tabela[-1].append(" ")
				
			if self.list_config[3] == True:
				tabela[-1].append(self.sum_xi)
				
			if self.list_config[-1] == True:
				tabela[-1].append(self.sum_fi_xi)
				
			terminal.tables(tabela, True,"Tabela de frequência")
		elif install_terminaltables == False:
			print("Instale o módulo terminaltables para mais detalhes.\n")
	
	
		