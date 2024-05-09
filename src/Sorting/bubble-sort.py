def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

bubbleSort(a)

print(a)