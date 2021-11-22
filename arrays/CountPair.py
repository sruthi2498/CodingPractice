# Python 3 implementation of simple method
# to find count of pairs with given sum.
import sys

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def getPairsCount(arr, n, sum):

    arr= list(set(arr))
    n = len(arr)
    m = [0] * 1000

	# Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
    twice_count = 0
    for i in range(0, n):
        twice_count += m[sum - arr[i]]
		# if (arr[i], arr[i]) pair satisfies the
		# condition, then we need to ensure that
		# the count is decreased by one such
		# that the (arr[i], arr[i]) pair is not
		# considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

	# return the half of twice_count
    return int(twice_count / 2)


# Driver function
arr = [1, 2,3,4,46,1]
n = len(arr)
sum = 47

print(arr,sum,getPairsCount(arr,n, sum))


