def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    for i in range(len(unsorted_list)):
        for j in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j + 1] = temp
    return unsorted_list

unsorted_list = [5, 3, 8, 4, 2]
print(bubble_sort(unsorted_list))