def binarySearch(array):
    a, b = 0, n - 1
    while a <= b:
        k = (a + b) // 2
        if array[k] == x:
        # x found at index k
            break
        elif array[k] > x:
            b = k - 1
        else:
            a = k + 1