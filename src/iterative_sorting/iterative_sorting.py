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


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
