import random
import time
import SortingAlgorithms

# Sorting algorithms and time they take to sort array of size ARRAY_SIZE
ARRAY_SIZE = 5000

# Merge Sort
merge_sort_list = []
for x in range(0, ARRAY_SIZE):
    merge_sort_list.append(random.randint(0, ARRAY_SIZE))
print("Merge sort:")
start_time_merge = time.process_time()
SortingAlgorithms.merge_sort(merge_sort_list)
print("Time elapsed: " + str(time.process_time() - start_time_merge) + " seconds")
print()


# BUBBLE SORT
bubble_sort_list = []
for x in range(0, ARRAY_SIZE):
    bubble_sort_list.append(random.randint(0, ARRAY_SIZE))
print("Bubble sort:")
start_time_bubble = time.process_time()
SortingAlgorithms.bubble_sort(bubble_sort_list)
print("Time elapsed: " + str(time.process_time() - start_time_bubble) + " seconds")
print()
