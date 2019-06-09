def display():
    num_in_sequence = input('How many fibonacci numbers do you need? ')

    final_list = []

    for number in range(int(num_in_sequence)):
        fib = fibonacci(number)
        final_list.append(fib)

    print(final_list)


def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


display()
