def fibonacci_check(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


if __name__ == '__main__':
    numero = int(input("Informe um número: "))

    if fibonacci_check(numero):
        print("O número pertence à sequência de Fibonacci.")
    else:
        print("O número não pertence à sequência de Fibonacci.")
