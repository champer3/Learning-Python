from array import *
import numpy as np

twoArray = np.array([[22, 1, 2, 33], [12, 13, 17, 18], [
                    22, 12, 15, 14], [21, 17, 11, 12]])
print(twoArray)
arr = array('i', [1, 2, 3, 4, 5, 6])

arr.insert(0, 0)
# print(arr)


def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Value not in the array"


# print(searchInArray(arr, 3))
