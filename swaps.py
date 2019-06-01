def minimum_swaps(ratings):
    no_of_swaps = 0

    sorted_ratings = sorted(ratings)

    # compare unsorted ratingsay with the sorted one
    for index in range(len(ratings)):
        if ratings[index] != sorted_ratings[index]:
          no_of_swaps += 1
          current_rating_value = ratings[index]
          ratings[ratings.index(sorted_ratings[index])] = current_rating_value
          ratings[index] = sorted_ratings[index]

    return no_of_swaps


print(minimum_swaps([3,1,2,4]))
print(minimum_swaps([3,1,2]))