# Some Array and List Interview Questions

# Question 1 - Missing number in an array

#  The idea is - The sum of consecutive numbers in n(n+1)/2

myList = [1, 2, 3, 5, 6, 7, 8, 9]


def findMissing(list, n):
    sum1 = (n * (n+1))/2
    sum2 = sum(list)
    print(sum1-sum2)


findMissing(myList, 9)

# Qouestion 2 - Pair/Two Sum
