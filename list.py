from random import random

# shoppingList = ["Milk", "Cheese", "Butter"]
# print("Milk" in shoppingList)

# for i in shoppingList:
#     i = i + "+"
#     # print(i)

# arr = [1, 2, 3, 4, 5, 6, 7]

# print(arr[3:0:-1])

# arr.insert(0, 22)
# print(arr)
# newArr = [22, 33, 4, 5, 90]
# arr.extend(newArr)
# print(arr)

# print(arr[0:5])

# nums = list()

# while (True):
#     inp = input("Input a number: ")
#     if inp == "done":
#         break
#     inp = int(inp)
#     nums.append(inp)
#     output = sum(nums)/len(nums)

# print(output)

# a = 'spam spam spam'
# b = a.split()
# delimeter = '-'
# print(delimeter.join(b))

# myList = [1, 24, 5, 3, 8, 7, 11]

# myList.sort()
# print(myList)

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v


# print(fun(data[0]))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::2])


# # numDays = input("How many day's temperature? ")
# numList = []
# for i in range(int(numDays)):
#     num = i+1
#     dayInput = input("What is Day " + str(num) + "'s temperature? ")
#     numList.append(int(dayInput))
# # print(numList)
# average = sum(numList) / len(numList)
# # print(average)
# for temp in numList:
#     if temp < average:
#         day = numList.index(temp) + 1
#         print("Day" + str(day))


print(arr)
