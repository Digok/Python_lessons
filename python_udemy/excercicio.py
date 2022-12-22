"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input("Whats your name?")
age = input("Whats your age?")
len_name = len(name)


if name and age:
    print(f'Your name is {name}')
    print(f'your name inverted is{name[::-1]}'),
    print("Your name has", len_name, "letters!"),
    print("The first letter of your name is ", name[0], "!"),
    print("The last letter of your name is", name[-1], "!")
else:
    print("Sorry, you left blank spaces. Please fill them.")

if " " in name:
    print("Your name does have spaces"),
else:
    print("Your name does not has spaces")
