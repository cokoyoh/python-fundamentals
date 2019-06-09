import sys
sys.setrecursionlimit(20000)


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


#Simple Santa Clause gift delivery problem recurively solved

houses = ["Mike's House", "Charles's House", "Erick's House", "White House", "Benta's House"]


def deliver_gifts_to_houses(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering gifts to ", house)

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        deliver_gifts_to_houses(first_half)
        deliver_gifts_to_houses(second_half)


deliver_gifts_to_houses(houses)