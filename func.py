import math


def menu():
    print("\nВыберите ряд для вычисления:"
    "\n1. Ряд для косинуса (cos(x))"
    "\n2. Ряд для арктангенса (arctan(x))"
    "\n3. Биномиальное разложение (1 + x)^m"
    "\n4. Выход"
          )


def cos_series(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    return result


def arctan_series(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return result


def main():
    while True:
        menu()
        choice = input("Выберите опцию (1-4): ")

        if choice == "1":
            x = float(input("Введите значение x для cos(x): "))
            terms = int(input("Введите количество членов для приближенного вычисления: "))
            print(f"cos({x}) ≈ {cos_series(x, terms)}")

        elif choice == "2":
            x = float(input("Введите значение x для arctan(x): "))
            terms = int(input("Введите количество членов для приближенного вычисления: "))
            print(f"arctan({x}) ≈ {arctan_series(x, terms)}")


        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите правильный вариант.")



if __name__ == "__main__":
    main()
