# def minimum_swaps(ratings):
#     no_of_swaps = 0
#     sorted_list = sorted(ratings, reverse=True)
#     sorted_count = 0
#
#     # if set(ratings) and set(sorted_list):
#     #     return no_of_swaps
#
#     for index in range(len(ratings) - 1):
#         if ratings[index + 1] < ratings[index]:
#             no_of_swaps += 1
#             ratings[index + 1], ratings[index] = ratings[index], ratings[index + 1]
#
#     return no_of_swaps

# for index, value in enumerate(ratings):
#     if ratings[index] == sorted_list[sorted_count]:
#         sorted_count += 1
#     else:
#         no_of_swaps += 1
#
# return no_of_swaps
#
# sorted_list = sorted(ratings, reverse=True)
# sorted_count = 0
# for value in ratings:
#     if value == sorted_list[sorted_count]:
#         sorted_count += 1
#
# return len(ratings) - sorted_count


# def minimum_swaps(ratings):
#     no_of_swaps = 0
#     sorted_list = sorted(ratings, reverse=True)
#     sorted_count = 0
#
#     for index in range(len(ratings) - 1):
#         if ratings[index] == sorted_list[sorted_count]:
#             sorted_count += 1
#         else:
#             no_of_swaps += 1
#
#     return no_of_swaps
def minimum_swaps(ratings):
    no_of_swaps = 0
    for index, value in enumerate(ratings):
        selected_inner_index = None
        selected_inner_value = None
        for inner_index, inner_value in enumerate(ratings):
            if (value < inner_value and inner_index > index):
                if selected_inner_value == None or selected_inner_value < inner_value:
                    selected_inner_value = inner_value
                    selected_inner_index = inner_index

        if selected_inner_index != None:
            ratings[selected_inner_index] = value
            ratings[index] = selected_inner_value
            no_of_swaps += 1

    print(no_of_swaps)

    # for index, value in enumerate(ratings):
    #     selected_inner_index = None
    #     selected_inner_value = None
    #
    #     for inner_index, inner_value in enumerate(ratings):
    #         if value < inner_value and inner_index > index:
    #             if selected_inner_value is None or selected_inner_value < inner_value:
    #                 selected_inner_value = inner_value
    #
    #     if selected_inner_index is not None:
    #         ratings[selected_inner_index] = value
    #         ratings[index] = selected_inner_value
    #         no_of_swaps += 1
    #
    # print(no_of_swaps)


minimum_swaps([3, 1, 2])
minimum_swaps([3,1,2,4])
minimum_swaps([1])
minimum_swaps([3,1,2,4, 5])


