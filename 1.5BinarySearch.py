def binarySearch(n, S, x):
    low = 1
    high = n
    location = 0
    while low <= high and location == 0:
        mid = (low + high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return location


S = [-1, 5, 7, 8, 10, 11, 13]
x = 2
location = binarySearch(len(S) - 1, S, x)
print(S)
print(x)
print(location)