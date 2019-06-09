def odd_or_event():
    number = input('Please enter a number ')

    print(type(number))

    while not number.isdigit():
        number = input('Please enter a number, an integer in this case ')

    number = int(number)

    if number % 2 == 0 and number % 4 == 0:
        print('Number is both divisible by 2 and 4')
    elif number % 2 == 0:
        print('Number is divisible by 2')
    else:
        print('Does not meet any criteria')


odd_or_event()
