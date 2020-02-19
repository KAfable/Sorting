# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while high - low > 1:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # explore left side next
            low = low
            high = mid
        elif arr[mid] < target:
            # explore right side next
            low = mid
            high = high

    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    mid = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid)
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid, high)
