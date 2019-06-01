def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for number in range(0, 10):
    print(fibonacci(number))