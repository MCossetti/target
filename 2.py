def fibonacci_sequence(limit):
    fib_seq = [0, 1]
    while fib_seq[-1] < limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def is_in_fibonacci(number):
    fib_seq = fibonacci_sequence(number)
    if number in fib_seq:
        return True
    return False

# Número a ser verificado
num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando se o número pertence à sequência
if is_in_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
