first_value = input("Digite um valor:")
second_value = input("Digite outro:")

if first_value > second_value:
    print("First value is bigger!")
elif second_value > first_value:
    print("The second value is bigger")
elif second_value == first_value:
    print("They have the same value")    
else:
    print("Something is wrong, check your values again!")


