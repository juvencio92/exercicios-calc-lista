##################################### Variaveis input mini calculadora #############################

numero1 =input(' Digite o 1º número :')
numero2 = input('Digite o 2º número : ')

numero1=int(numero1)    # Converter os valores para inteiros porque o input devolve string
numero2=int(numero2)

op=input('Que operação deseja fazer ? ') # Escolher a operação

if op == '+':
    print(' O resultado da soma é ', numero1 + numero2)
elif op == '-':
    print(' O resultado da subtração é ', numero1 - numero2)
elif op == '*':
    print(' O resultado da multiplicação é ', numero1 * numero2)
elif op == '/':
    print(' O resultado da divisão é ', numero1 / numero2)
else:
    print('Opção enexistente')

######################### Lista de nomes para uma Festa ######################
'''
EXERCÍCIO : Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa o nome de todas as pessoas e colocar numa lista de convidados.
Imprimir todos os nomes da lista
'''

lista_convidados = [] # Lista de convidados
cont = 0
qtd_convidados = input("Insira a quantidade de convidados : ")
qtd_convidados =int(qtd_convidados)

while cont < qtd_convidados:
    print(' Digite o ', cont + 1, 'º Nome ')
    lista_convidados.append(input())
    cont += 1
print(lista_convidados)