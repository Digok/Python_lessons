'''
Interpolação basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
name = 'Luiz'
price = 1000.958942
variable = '%s, o preço é R$%.2f' % (name, price)
print(variable)
print(' O hexadecimal de %d é %04x' % (1500, 1500)) # o 'x' minusculo retorna o hexadecimal em minúsculo e vice versa. Para escolher a quantidade precisa coloca o 0 antes da qntd desejada