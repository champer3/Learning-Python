# Some Array and List Interview Questions

from xml.etree.ElementTree import TreeBuilder
import numpy as np

# Question 1 - Missing number in an array

#  The idea is - The sum of consecutive numbers in n(n+1)/2

myList = [1, 2, 3, 5, 6, 7, 8, 9]


def findMissing(list, n):
    sum1 = (n * (n+1))/2
    sum2 = sum(list)
    print(sum1-sum2)


# findMissing(myList, 9)

# Qouestion 2 - Pair/Two Sum


def twoSum(arr, t):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == t:
                print([i, j])


myList = [1, 2, 3, 2, 3, 4, 5, 8]
# twoSum(myList, 6)

# Question 3 - Check if an array contains a number in python

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def findNumber(arr, num):
    for n in arr:
        if n == num:
            return True
    return False


# print(findNumber(myArray, 13))

# Question 4 - Maximum product of two integers in an array
newArray = np.array([21, 24, 63, 41, 25, 16, 27, 38, 91, 10, 33, 21, 99, 53])


def findMaxProduct(arr):
    maxProduct = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] * arr[j]) > maxProduct:
                maxProduct = arr[i] * arr[j]
    return maxProduct


# print(findMaxProduct(myArray))

# Question 4 - Is Unique: Impliment an algorithm to see if a list has all unique characters


def isUnique(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True


# print(isUnique(myArray))

def isUnique1(arr):
    newList = []
    for num in arr:
        if num in newList:
            print(num)
            return False
        else:
            newList.append(num)
    print(newList)
    return True


# print(isUnique1(myArray))

# Question 6 - Permutation

str1 = "rail"
str2 = "liar"

myArr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myArr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def isPermutation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for num in arr1:
        if num not in arr2:
            return False
    return True


def isPermutation1(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False


print(isPermutation1(myArr1, myArr2))
