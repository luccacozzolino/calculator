def soma(x, y):
    return x + y


def subtrai(x, y):
    return x - y


def multiplica(x, y):
    return x * y


def divide(x, y):
    return x / y


print("python calculator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exit")

escolha = input("Choose which operation you want to do: 1/2/3/4 ")
num1 = int(input("number 1: "))
num2 = int(input("number 2:"))

if escolha == '1':
    print(num1, '+', num2, "=", soma(num1, num2))

elif escolha == '2':
    print(num1, '-', num2, "=", subtrai(num1, num2))

elif escolha == '3':
    multiplica(num1, num2)
    print(num1, '*', num2, "=", multiplica(num1, num2))
elif escolha == '4':
    print(num1, '/', num2, "=", divide(num1, num2))
