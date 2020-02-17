import random
import time
from iterative_sorting import bubble_sort, bubble_sort2
from statistics import mean


def time_trial_bubble_sort(arr):
    arr_start = time.time()
    bubble_sort(arr)
    arr_end = time.time()
    return arr_end - arr_start


def time_trial_bubble_sort2(arr):
    arr_start = time.time()
    bubble_sort2(arr)
    arr_end = time.time()
    return arr_end - arr_start


arrays = [random.sample(range(2000), 2000) for i in range(10)]
arrays2 = [random.sample(range(2000), 2000) for i in range(10)]

results = [time_trial_bubble_sort(arr) for arr in arrays]
results2 = [time_trial_bubble_sort2(arr) for arr in arrays2]

print(mean(results))
print(mean(results2))
