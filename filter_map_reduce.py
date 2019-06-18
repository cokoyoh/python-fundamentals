"""
From the list list_one = [1, 3, 45, 79, 87, 190, 689] filter and remove the values more than 100
"""
list_one = [1, 3, 45, 79, 87, 190, 689]


def filtered_result(numbers: list):
    return filter(lambda number: number < 100, numbers)


print(list(filtered_result(list_one)))


def mapped_result(numbers: list):
    return map(lambda number: number ** 2, numbers)


print(list(mapped_result(list_one)))
