def insertion_sort(arr):
    """Insertion sort is a sort that starts as a smaller sub-list of the target list, starting at one element. It takes in the target list one at a time, inputting the new incoming element into its correct index before moving on with the sort."""

    for i in range(1, len(arr)):
        cur = i
        j = i-1
        # while cur value is higher than everything below it
        while arr[cur] < arr[j] and j >= 0:
            # swap
            temp = arr[cur]
            arr[cur] = arr[j]
            arr[j] = temp
            # keep track of the element as it moves down
            cur = j
            # decrement j
            j = j - 1

    return arr


def selection_sort(arr):
    """Selection sort is a sort that starts by looking for the smallest value in a list, and making that the first element in the list. Then it'll use a primary iterative loop through the array to keep track of which index (and thus next smallest number). Then it will also use a secondary loop to check for the smallest number again in the rest of the list. Once it finds the smallest number, it'll swap to its correct place (the current index) and then restart the process again.

    It's time complexity is at worst is O(n squared).
    """
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if(arr[j] < arr[smallest_index]):
                smallest_index = j
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


def bubble_sort(arr):
    # set the outer loop, size of where numbers get bubbled
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            # check if the left is bigger than the right
            if arr[j] > arr[j+1]:
                # if yes, move it to the right
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def bubble_sort2(arr):
    swapped = True
    while swapped:
        swapped = False
        # loop through the array, and if at least once swap happens, do it again
        for i in range(0, len(arr)-1):
            # if the element is larger, swap it to the right
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i+1] = temp
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
