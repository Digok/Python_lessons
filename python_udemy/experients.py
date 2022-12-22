"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''
RESOLUÇÃO


int_1 = int(input("Escreva um número inteiro: (número sem ',' e '.') "))
int_int_check = int_1 is int
verdade = int_1 % 2 == 0

if int_int_check is True:
    print('Por favor digite um núnero')
    break

if verdade:
    print("Este número é par")
else:
    print('esse numero é impar')    
'''






"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
"""
RESOLUCAO
question1 = int(input("Me informe qual a sua hora neste exato momento (apenas 0 até 24, sem os minutos) :"))


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')





if question1 < 12:
    print("Bom dia")
elif question1 > 11 and question1 < 19:
    print("Boa tarde")
else:
    print("Boa noite")
"""









"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
# RESOLUÇÃO

q1 = input("Qual o seu nome? ")
q1_fixed = str(q1)

if q1_fixed is True:
    print("Por favor digite sem números ou . e ,")
    break

if len(q1_fixed) <= 4:
    print("Seu none é curto")
elif len(q1_fixed) <7 and len(q1_fixed) > 4:
    print("Seu nome é médio")
else:
    print("Seu nome é longo")
"""