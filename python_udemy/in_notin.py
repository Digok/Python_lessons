name = input("Type your name:")
encontrar = input("What do you wanna search?")

if encontrar in name:
    print(f'{encontrar} está em {name}')
else:
    print(f'{encontrar} não está em {name}')
