import time

expensive_cache = {}


def expensive_function(number):
    if number in expensive_cache:
        return expensive_cache[number]

    print('Computing {}'.format(number))
    time.sleep(1)

    result = number ** 2
    expensive_cache[number] = result

    return result


print(expensive_function(4))
print(expensive_function(10))
print(expensive_function(4))
print(expensive_function(10))
