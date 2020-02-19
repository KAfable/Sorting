
def merge(arrA, arrB):
    """Takes two sorted arrays and combines them into a sorted array."""
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # start with the lower, and
    for i in range(len(merged_arr)):
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr


def merge_sort(arr):
    """Sorting algorithm that recursively separates the original array into single elements, and then applies sorting logic as it recombines the arrays together. """
    if(len(arr) < 2):
        return arr
    middle = len(arr)//2
    arr1 = arr[0:middle]
    arr2 = arr[middle:]
    return merge(merge_sort(arr1), merge_sort(arr2))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
