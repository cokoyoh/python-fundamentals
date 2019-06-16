# import time
#
#
# def factorial(number):
#     if number == 0:
#         return 0
#
#     if number == 1:
#         return 1
#
#     time.sleep(1)
#     return number * factorial(number - 1)
#
#
# print([factorial(number) for number in range(0, 10)])


results_cache = {}


def factorial(number):
    if number == 0 or number == 1:
        return 1
    elif number in results_cache:
        return results_cache[number]
    else:
        result = number * factorial(number - 1)
        results_cache[number] = result
        return result


print([factorial(number) for number in range(0, 10)])

