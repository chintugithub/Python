def sorted_square(array):
    result = [x * x for x in array]
    result.sort()
    return result
print(sorted_square([2,5,7,3,-4]))


