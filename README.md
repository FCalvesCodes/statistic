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
   - Media Aritmética Ponderada
 
 - **Dados agrupados**
   - Amplitude Total 
   - Desvio Médio Simples (Amostra e população)
   - Desvio Padrão (Amostra e população)
   - Variância (Amostra e população)
   - Moda
   - Média Aritmética
   

### Configurações dados brutos

- Casas decimais (1 até 5)
- **Ativar e Desativar**
	- Amostra
	- População

### Configurações dados agrupados
- Casas decimais (1 até 5)
- **Ativar e Desativar**
	- Amostra
	- População
	- Frequência relativa (fri%) -- (Para vizualizar a tabela na opção 7)
	- Frequência absoluta acumulada (Fi) -- (Para vizualizar a tabela na opção 7)
	- Frequência relativa acomulada (Fri%) -- (Para vizualizar a tabela na opção 7)
	- Ponto médio (xi) -- (Para vizualizar a tabela na opção 7)


**Modo de uso:**

 **Obs: Esse script foi feito pelo celular e usando terminal do termux para testes, pode haver erros em terminais diferentes**

Instale o termux no seu celular(google play)

Codigos a digitar no termux:
			
			pkg install python python-dev coreutils git
			
			pip install terminaltables     #Necessário para ver as tabelas
			
			pip install termcolor  			#Apenas para terminal linux
			
			git clone https://github.com/FelipeAlmeid4/statistic.git

Para execultar o script: 
			
			cd statistic
			
			python main.py

Atualização, Caso houver, digite dentro do diretório **statistic**
		
			git pull

