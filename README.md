# Calculadora de estatística (via terminal) #

Esse Script foi feito para fins didáticos, é uma calculadora de estatística que aceita dados brutos e dados agrupados,
 faz os cálculos exibindo uma tabela para orientação do resultado.


### Calcula! ###

 - **Dados Brutos**
   - Amplitude Total
   - Desvio Médio Simples (Amostra e população)
   - Desvio Padrão (Amostra e população)
   - Variância (Amostra e população)
   - Moda
   - Mediana
   - Média Aritmética
 
 - **Dados agrupados**
   - Amplitude Total 
   - Desvio Médio Simples (Amostra e população)
   - Desvio Padrão (Amostra e população)
   - Moda
   - Mediana
   - ~Variância (Amostra e população)~
   - Média Aritmética
   

### Configurações ###
Existe um menu de configurações onde pode alterar (Amostra e população) e definir as casas decimais.


- **Modo de uso:**

 **Obs: Esse script foi feito pelo celular e usando terminal do termux para testes, pode haver erros em terminais diferentes**

Instale o termux no seu celular(google play)

Codigos a digitar no termux:
			
			pkg install python python-dev coreutils git
			
			pip install terminaltables     #Necessário para ver as tabelas
			
			pip install termcolor  			#Apenas para terminal linux
			
			git clone https://github.com/FelipeAlmeid4/statistic.git
			
			cd statistic
			
			python main.py

Atualização, Caso houver, digite dentro do diretório **statistic**
		
			git pull

