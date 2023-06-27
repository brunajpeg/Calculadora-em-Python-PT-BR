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

    number_1 = int(input("Digite o primeiro número:"))
    number_2 = int(input("Digite o segundo número:"))

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
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    # Divisão
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou uma operação válida, por favor execute o programa novamente')

    # Pergunta se o usuário quer fazer um novo cálculo
    again()

# Define a função again() para perguntar ao usuário se ele deseja usar a calculadora novamente
def again():
    # Input do usuário
    calc_again = input('''Você quer fazer um novo cálculo? Digite S para SIM ou N para NÃO: ''')

    # Se o usuário digitar S, execute a função calculate() novamente
    if calc_again.upper() == 'S':
        calculate()

    # Se o usuário digitar N, diga "tchau" ao usuário e feche o programa
    elif calc_again.upper() == 'N':
        print('Te vejo mais tarde.')

    # Se o usuário digitar outra resposta, execute a função novamente
    else:
        again()

# Chama a função welcome() para exibir a mensagem de boas-vindas
welcome()

# Chama a função calculate() para iniciar a calculadora
calculate()
