# adiciona 
def add(x, y):
    return x + y

# subtrai
def subtract(x, y):
    return x - y

# multiplica
def multiply(x, y):
    return x * y

# divide
def divide(x, y):
    return x / y


print("Operação.")
print("1.Add")
print("2.Subtração")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # entrada
    choice = input("Escolha(1/2/3/4): ")

    # checa se escolheu uma das opçoes
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Primeiro numero: "))
            num2 = float(input("segundo numero: "))
        except ValueError:
            print("VAlor invalido.tente novamente")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # checa se quer algo mais
        # quebra o loop se não
        next_calculation = input("Algo mais? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")