def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            print(customList[j], customList[j+1])
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    return customList


keyy = [2, 3, 9, 2, 1, 5, 7, 3, 4, 6]
# print(bubbleSort(keyy))
print("fsf" * -300)
