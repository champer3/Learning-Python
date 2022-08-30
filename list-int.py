# Question 1 - Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Solution 1 - BRUTE FORCE
from collections import Counter, defaultdict
from email.policy import default
from numbers import Number
from operator import indexOf


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
# nums1 = [1, 2, 3, 1]
# print(containsDuplicate1(nums1))

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


# Solution 2 - SORT ALGORITHM o(nlogn)

def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    if t == s:
        return True
    else:
        return False

# Question 3 - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

# Solution 1 - BRUTE FORCE


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum(nums, target):
    countNums = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in countNums:
            return [countNums[diff], i]
        else:
            countNums[nums[i]] = i


def camelcase(s):
    # Write your code here
    num = 1
    for c in s:
        if c == c.upper():
            num = num + 1
    return num


def groupAnagrams(strs):
    arr = []
    count = {}
    for el in strs:
        sortt = "".join(sorted(el))
        arr.append(sortt)
    for i in range(len(arr)):
        if arr[i] == "".join(sorted(strs[i])):
            count[strs[i]] = 1 + count.get(strs[i], 0)
    return count

# Question 4 - Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Solution 1 - Hashmap with sort fuction o(m.nlogn)


def groupAnagrams(strs):
    countS = {}
    for s in strs:
        key = "".join(sorted(s))
        if key in countS:
            countS[key].append(s)
        if not key in countS:
            countS[key] = []
            countS[key].append(s)
    return countS.values()


def groupAnagrams1(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs))


# Question 5 - Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Solution 1


def topKFrequent(nums, k):
    freq = defaultdict(int)
    sorted_dict = {}
    for num in nums:
        freq[num] = freq[num] + 1 or 1
    sorted_keys = sorted(freq, key=freq.get, reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = freq[w]
    dict_values = list(sorted_dict.keys())
    return dict_values[0:k]


# Solution 2


def topKFrequent(nums, k):
    freq = defaultdict(int)
    sorted_dict = {}
    for num in nums:
        freq[num] = freq[num] + 1 or 1
    sorted_keys = {k: v for k, v in sorted(
        freq.items(), key=lambda v: v[1], reverse=True)}
    dict_values = list(sorted_keys.keys())
    return dict_values[0:k]


# nums = [1, 2]
# k = 2
# dict1 = topKFrequent(nums, k)
# print(dict1)
# a = 10
# a = 3
# a = a + 2
# print(a)
# print("st" ** 2)
nums = [1, 2, 3, 4]
post = []

nums = nums[::-1]
first = 1
for i in range(len(nums)):
    nums[i] = nums[i] * first
    post.append(nums[i])
    first = nums[i]

print(post)
