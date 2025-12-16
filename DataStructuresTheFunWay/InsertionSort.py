""" 
INSERTION SORT 

Chapter 1: Information in Memory, Page 8-10

Pre-requisites 
    1. variables
    2. Arrays
    3. Composite Data Structure

"""

Array = [6, 1, 13, 49, 99, 3]

def insertionSort(Array):
    n = len(Array)
    i = 1
    """starts at the first unsorted element, 
    i = 1 and progresses through each value in
    the unsorted range"""
    while i < n: # OUTER LOOP (i): shifts the current value down into the sorted prefix
        current = Array[i]
        j = i - 1
        while j >= 0 and Array[j] > current: # INNER LOOP (j): with the iterator j shifts the current value down into the sorted prefix by comparing the `current` value to the preceding value in the prefix, index j. If element j is larger than i then the the elements are in the wrong order and must be swapped
            Array[j + 1] = Array[j]
            j = j - 1
        Array[j + 1] = current
        i = i + 1
    return Array

print(Array)
print(insertionSort(Array))