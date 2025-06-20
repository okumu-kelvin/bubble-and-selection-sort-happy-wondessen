def selection_sort(arr):
    # TODO: Implement selection sort

    for i in range(len(arr)):
        min = i
        for j in range (i+1, len(arr)):
            if arr[j] < arr[i]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr

arr = [5, 3, 8, 4, 2]
print(selection_sort(arr))

