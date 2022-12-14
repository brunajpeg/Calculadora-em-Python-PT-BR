def welcome():
	print(''' 
Bem vindo a calculadora
''')

def calculate():
	operation = input(''' 
Por favor escolha a operação de matemática que você gostaria de fazer:
+ para adição
- para subtração
* para multiplicação
/ para divisão
% para porcentagem
''')


number_1 = int(input ("Digite o primeiro número:"))
number_2 = int(input ("Digite o segundo número:"))

# Adição
if operation == '+':
   	print('{} + {} = '.format(number_1, number_2))
   	print(number_1 + number_2)

# Subtração
elif operation == '-':
   	print('{} - {} = '.format(number_1, number_2))
   	print(number_1 - number_2)

# Multiplicação
elif operation == '*':
	print('{} * {} = '.format (number_1, number_2))
	print(number_1 * number_2)

# Divisão
elif operation == '/':
	print('{} / {} = '.format(number_1, number_2))
	print(number_1 / number_2)

else:
	print('Voce não digitou um número válido, por favor execute o programa novamente')

# Ative a calculadora fora da funcao
again()

# Defina again() funcao para perguntar ao usuário se ele deseja usar a calculadora novamente
def again():

	#input do user
	calc_again = input(''' Você quer fazer um novo cálculo? Digite S para SIM ou N para NÃO''')

	# Se o usuário digitar S, execute a calculate() função
	if calc_again.upper() == 'Y':
		calculate()

	#Se o usuário digitar N, diga tchau ao usuário e feche o programa
	elif calc_again.upper() == 'N':
		print('Te vejo mais tarde.')

	# Se o usuário digitar outra letra, execute a função novamente
	else:
		again()

#Execute calculate() fora da função
calculate ()