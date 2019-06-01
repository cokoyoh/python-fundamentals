# def solution(A):
#     sorted_A = sorted(A)
#     # print(sorted_A)
#
#     highest = None
#     for i in range(len(sorted_A) - 1):
#         if sorted_A[i] < 0:
#             continue
#         if sorted_A[i+1] - sorted_A[i] > 1:
#             highest = sorted_A[i]
#             break
#
#     if not highest:
#         highest = sorted_A[-1]
#
#     if highest < 0:
#         highest = 0
#
#     print(highest+1)
#
#     return highest + 1


# solution([23, 99, 98, 34, 45, 56])


# Binary Gaps
# def solution(N):
#     binary_value = bin(N)[2:]
#
#     print(binary_value[-5:-1], format(34, 'b')[:-1])
#
#
# solution(34)


def split_integer(num, parts):
    quotient, remainder = divmod(num, parts)

    lower_elements = [quotient for index in range(parts - remainder)]
    higher_elements = [quotient + 1 for index in range(remainder)]
    
    return lower_elements + higher_elements


print(split_integer(20, 5))