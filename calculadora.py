def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    while True:
        print("Selecione uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Sair")

        choice = input("Digite 1, 2 ou 3: ")

        if choice == '3':
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print("Resultado:", add(num1, num2))
        elif choice == '2':
            print("Resultado:", subtract(num1, num2))