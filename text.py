# Leetcode Coding Chalenge
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict


class Solution:
    def groupAnagrams(strs):
        res = defaultdict(list) # A dictionary that doesn't return keyError
        for str in strs:
            count = [0] * 26 # 26 zeros in an array to represent alphabet a - z
            for c in str:
                count[ord(c) - ord("a")] += 1 # matches each given string
            res[tuple(count)].append(str)
        return res.values() # return only the values in the hashmap

# Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])


jump = [0] * 26

jump[0] += 1
jump[12] += 1
jump[18] += 1

print(jump)
res = {
    1: "love",
    2: "koboko",
    "dh": "pol"
}
res[1]
# print(res.values())
