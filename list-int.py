# Question 1 - Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Solution 1 - BRUTE FORCE
from collections import Counter


def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Solution 2 - Hashmap (Refactored)


def containsDuplicate1(nums):
    num_dic = {}
    for i in nums:
        if i in num_dic:
            return True
        else:
            num_dic[i] = i
    return False


# Example nums1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], [1, 2, 3, 1], [1,2,3,4]
nums1 = [1, 2, 3, 1]
print(containsDuplicate1(nums1))

# Question 2 - Given two strings s and t, return true if t is an anagram of s, and false otherwise

# Solution 1 - Array o(n)


def isAnagram(s, t):
    slist = []
    tlist = []
    for c in s:
        slist.append(c)
    for c in t:
        tlist.append(c)
    print(slist)
    print(tlist)
    if len(s) != len(t):
        return False
    for el in slist:
        if el in tlist:
            tlist.remove(el)
        else:
            return False
    return True

# Solution 3 - Hashmap o(n)


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for c in s:
        countS[c] = 1 + countS.get(c, 0)
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    for key in countS:
        if countS[key] != countT.get(key, 0):
            return False
    return True

    print(countS)

# Solution 4 - Python3 Builtin Hasmap o(n)


def isAnagram1(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
print(sorted(s))
isAnagram1(s, t)


# Solution 2 - SORT ALGORITHM o(nlogn)

def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    if t == s:
        return True
    else:
        return False
