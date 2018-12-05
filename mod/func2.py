# -*- coding: utf-8 -*-

import string
from decimal import Decimal
import sys



try:
	from termcolor import colored
	color = True
except:
	color = False



try:
	from terminaltables import AsciiTable
	is_terminaltables = True
except:
	is_terminaltables = False
	print("Instale o módulo terminaltables para visualizar\n a tabela detalhada.")
	time.sleep(2)


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
		base = ""
			
		for i, letter in enumerate(string):
			if letter == "," or i == len(string)-1:
				if i == len(string)-1:
					base += letter
				try:
					list_.append(int(base))
					base = ""
				except:
					print("Error ao verificar dados.")
					return []
			else:
				base += letter
		return list_
		

def sum_list(list_):
	""" Faz a soma de uma lista com números."""
	if len(list_) < 2:
		return 0
	sum = Decimal('0')
	for n in list_:
		sum += Decimal(str(n))
	return sum

	
	

class Process(object):
	
	def __init__(self):
		
		# -------------- Variáveis em geral ------------------

		self.xmin = 0
		self.xmax = 0
		
		self.amplitude = 0  # Amplitude da classe
		self.x1= 0			      #Média aritmética
		
		self.sum_fi_xi = 0
		self.sum_x3 = 0
		self.sum_x4 = 0
		self.sum_xi = 0
		self.sum_fi = 0
		self.sum_fi_x3 = 0
		self.sum_fi_x4 = 0
		
		
		self.quant_xi = 0 	   #len(list_xi)
		self.quant_fi = 0       #len(list_fi)
		
		self.decimal = 2
		self.total_amp = 0   #Amplitude total Xmin da 1°, Xmax da ultima Classe.
		self.initial = 0			#Xmin da primeira classe
		
		self.list_x2 = []		  #xi - "x-barra"
		self.list_x3 = []		  #|xi - "x-barra"|
		self.list_x4 = []		  #(xi - "x-barra")²
		self.list_xi = []		   # xi
		self.list_fi = []		   # fi
		self.list_fi_xi = []     # xi.fi
		self.list_fi_x3 = []	#fi.|xi - "x-barra"|
		self.list_fi_x4 = []	#fi.(xi - "x-barra")²
		self.list_fri = []         #fri% - Freq. Relativa %
		self.list_Fi = []          #Fi  - Freq. Absoluta Acumulado
		self.list_Fri = []        #Fri - Freq. Relativa Acumulada %
		
		#Amostral e populacional
		self.sample = False
		self.populational = True
		
		self.total_amplitude = 0
		
		#Para Moda de dados agrupados
		self.lmo = []
		self.indice = []
		self.value = 0  # self.value == self.fmo
		self.ffant =[]
		self.fpost= []
		self.delta_2 = []
		self.delta_1 = []
		self.modal = ["Amodal", "Unimodal", "Bimodal", "Trimodal"]
		#self.c == self.amplitude
		
		#Configurações para visualizar tabela de frequencia
		# indice    0 - fri%     1- Fi        2 - Fri%     3- xi
		self.list_config = [False, False, False, True]

		
		#Variáveis de entrada de dados
		self.amplitude = 0
		self.initial = 0
		
		self.xmin = 0
		self.xmax = 0
		
		self.is_terminaltables = is_terminaltables
		
		
	def tables(self, data, ult_borda= False,title= "", separar_colunas=True, separar_linhas=False):
		""" Recebe a tabela em formatos Matriz."""
		self.tables_terminal = AsciiTable(data)
		self.tables_terminal.inner_footing_row_border = ult_borda
		self.tables_terminal.inner_column_border = separar_colunas
		self.tables_terminal.inner_row_border = separar_linhas
		self.tables_terminal.title = title
		if self.tables_terminal.ok:
			print(self.tables_terminal.table)
		else:
			print("Tabela não pode ser visualizada, \n Recua o zoom do terminal e tente novamente.")
		
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
		
		
	def gerar_matriz_table(self, escopo, grouped, modo):
		"""  grouped = True - Dados agrupados
		   	 grouped = False - Dados Brutos
				modo = 1 - Desvio médio simples
				modo = 2 - Desvio padrão
				modo = 3 - Variância
		"""
		
		#Usados para construir a tabela de entrada de dados
		xmin = self.initial
		amp = self.amplitude
		
		l = []
		
		if grouped == True and modo == 4:
			if self.list_config[0] == True:
				escopo.append("fri %")
			if self.list_config[1] == True:
				escopo.append("Fi")
			if self.list_config[2] == True:
				escopo.append("Fri %")
			if self.list_config[3] == True:
				escopo.append("xi")
				
		l.append(escopo)
		
		#Auxilia a criação da lista Fi
		n = 0
		#Auxilia na criação da lista Fri
		b = 0
		
		#Indice para configurar a tabela
		ind = 0
		self.list_config2 = [["Casa Decimal",f"{self.decimal}"], ["Amostra", self.f_c(self.sample)], ["População", self.f_c(self.populational)], ["fri %", self.f_c(self.list_config[0])], ["Fi", self.f_c(self.list_config[1])], ["Fri %", self.f_c(self.list_config[2])], ["xi", self.f_c(self.list_config[3])]]
		self.list_x2, self.list_x3, self.list_x4,self.list_fi_x3, self.list_fi_x4, self.list_fri, self.list_Fri, self.list_Fi = [],[],[],[],[],[],[],[]
		
		#Gerar uma matriz para configurações
		if grouped == None and modo == 5:
			for x in range(0, len(self.list_config2)):
				l.append(self.list_config2[x])
			self.tables(l, True,"" ,True, True)
			l = []
			return
		
		for x in range(0, len(self.list_xi)):
		
			#xi-ㄡ
			self.list_x2.append(truncate(truncate(self.list_xi[x], self.decimal) - truncate(self.x1, self.decimal), self.decimal))
			#|xi-ㄡ|
			self.list_x3.append(abs(truncate(self.list_x2[x], self.decimal)))
			#(xi-ㄡ)²
			self.list_x4.append(truncate(truncate(self.list_x3[x], self.decimal)**2, self.decimal))
			
			
		
			if grouped == True:
				#fi.|xi-ㄡ|
				self.list_fi_x3.append(truncate(truncate(self.list_fi[x]*self.list_x3[x], self.decimal), self.decimal))
				
				#fi.(xi-ㄡ)²
				self.list_fi_x4.append(truncate(truncate(self.list_fi[x], self.decimal)*truncate(self.list_x4[x], self.decimal), self.decimal))
				
				#fri%
				#Foi usado o Round para casas decimais pois, func truncate não apresentou bons resultados.
				base = Decimal(self.list_fi[x])*100
				self.list_fri.append(round(base/self.sum_fi, self.decimal))
				
				#Fi
				n+=self.list_fi[x]
				self.list_Fi.append(n)
				
				#Fri%
				base = Decimal(self.list_fi[x])*100
				b += round(base/self.sum_fi, self.decimal)
				self.list_Fri.append(b)
				
			#Monta as matrizes
			if grouped == False and modo == 1:
				#Dados brutos - Desvio médio simples
				l.append([x+1, self.list_xi[x], self.list_x2[x], self.list_x3[x]])
			elif grouped == False and modo == 2:
				#Dados Brutos - Desvio Padrão
				l.append([x+1, self.list_xi[x], self.list_x2[x], self.list_x3[x], self.list_x4[x]])
			elif grouped == False and modo == 3:
				#Dados brutos e Agrupados - Variância
				l.append([x+1, self.list_xi[x], self.list_x2[x], self.list_x4[x]])
			
			elif grouped == True and modo == 1:
				#Dados agrupados - Desvio médio simples
				l.append([x+1, self.list_fi[x], self.list_xi[x], self.list_fi_xi[x], self.list_x3[x], self.list_fi_x3[x]])
		
			elif grouped == True and modo == 2:
				#Dados agrupados - Desvio padrão
				l.append([x+1, self.list_fi[x], self.list_xi[x], self.list_fi_xi[x], self.list_x2[x], self.list_x4[x], self.list_fi_x4[x]])
				
			elif grouped == True and modo == 3:
				#Dados agrupados - Variância
				l.append([x+1, self.list_fi[x], self.list_xi[x], self.list_fi_xi[x], self.list_x2[x], self.list_x4[x], self.list_fi_x4[x]])
				
			elif grouped == True and modo == 4:
				#Dados Agrupados - Simples demotração da tabela de frêquencia
				xmin += amp
				l.append([x+1, f"{xmin-amp}|-----{xmin}", self.list_fi[x]])
				
				if self.list_config[0] == True:
					#Adicionar os dados
					l[x+1].append(self.list_fri[x])
				
				if self.list_config[1] == True:
					l[x+1].append(self.list_Fi[x])
		
				if self.list_config[2] == True:
					l[x+1].append(self.list_Fri[x])
				
				if self.list_config[3] == True:
					l[x+1].append(self.list_xi[x])
				
			
		#Recebe as somas
		self.sum_xi = truncate(sum_list(self.list_xi), self.decimal)
		self.sum_fi = truncate(sum_list(self.list_fi), self.decimal)
		self.sum_x3 = truncate(sum_list(self.list_x3), self.decimal)
		self.sum_x4 = truncate(sum_list(self.list_x4), self.decimal)
		self.sum_fi_x4 = truncate(sum_list(self.list_fi_x4), self.decimal)
		self.sum_fi_x3 = truncate(sum_list(self.list_fi_x3), self.decimal)
		self.sum_fi_xi = truncate(sum_list(self.list_fi_xi), self.decimal)
		
	
		if grouped == False and modo == 1 and self.is_terminaltables:
			#Dados Brutos - Desvio médio simples
			l.append([" ", self.sum_xi, "    Σ", self.sum_x3])
			self.tables(l, True, "Dados Brutos - Desvio médio simples")
		elif grouped == False and modo == 2 and self.is_terminaltables:
			#Dados brutos - Desvio padrão
			l.append([" ", self.sum_xi, "Σ",self.sum_x3, self.sum_x4])
			self.tables(l, True,"Dados brutos - desvio padrão")
		elif grouped == False and modo == 3 and self.is_terminaltables:
			#Dados brutos - Variância
			l.append([" ", self.sum_xi, "Σ", self.sum_x4])
			self.tables(l, True,"Dados brutos - Variância")
		elif grouped == True and modo == 1 and self.is_terminaltables:
			#Dados agrupados - Desvio médio  simples
			l.append([" ", self.sum_fi, self.sum_xi, self.sum_fi_xi, self.sum_x3, self.sum_fi_x3])
			self.tables(l, True,"Dados Agrupados - Desvio médio simples")
		elif grouped == True and modo == 2 and self.is_terminaltables:
			#Dados agrupados - Desvio padrão
			l.append([" ", self.sum_fi, self.sum_xi,self.sum_fi_xi, "Σ", self.sum_x4, self.sum_fi_x4])
			self.tables(l, True,"Dados Agrupados - desvio padrão")
		elif grouped == True and modo == 3 and self.is_terminaltables:
			l.append([" ", self.sum_fi, self.sum_xi, self.sum_fi_xi, "Σ", self.sum_x4, self.sum_fi_x4])
			self.tables(l, True,"Dados Agrupados - Variância")
		elif grouped == True and modo == 4 and self.is_terminaltables:
			#Dados Agrupados - Simples demotração da tabela de frêquencia
			l.append([" ", " Σ ", self.sum_fi])
			
			if self.list_config[0] == True:
				#Adicionar os dados
				l[-1].append(" ")
				
			if self.list_config[1] == True:
				l[-1].append(" ")
		
			if self.list_config[2] == True:
				l[-1].append(" ")
				
			if self.list_config[3] == True:
				l[-1].append(self.sum_xi)
				
				
			self.tables(l, True,"Tabela de frequência")
		elif is_terminalself.tables == False:
			print("Instale o módulo terminalself.tables para mais detalhes.\n")
	
	
		