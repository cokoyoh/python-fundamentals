def fizz_buzz():
    for index in range(1, 100):
        if index % 5 == 0 and index % 3 == 0:
            print(index, ' - FizzBuzz')

        if index % 5 == 0 and index % 3 != 0:
            print(index, ' - Buzz')

        if index % 5 != 0 and index % 3 == 0:
            print(index, ' - Fizz')


fizz_buzz()