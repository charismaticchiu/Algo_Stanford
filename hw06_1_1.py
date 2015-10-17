import bisect
text_file = open("algo1-programming_prob-2sum.txt", "r")
numbers = [int(i) for i in text_file.readlines()]
 
def two_sum(array):
    """Returns the numbers from [-WIDTH, WIDTH] that can be obtained by
    summing up any two elements in 'array'."""
 
    WIDTH = 10000
    out = set()
    for i in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        upper = bisect.bisect_right(array, WIDTH - i)
        out |= set([i + j for j in array[lower:upper]])
    return out 

out = two_sum(numbers)

print out
print len(out)
