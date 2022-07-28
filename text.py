def groupAnagrams(strs):
    fin_arr = []
    new_arr = []
    for str in strs:
        geg = sorted(str)
        j_arr = "".join(geg)
        new_arr.append(j_arr)
    print(new_arr)
    for new in new_arr:
        if [new] in fin_arr:
            fin_arr[fin_arr.index([new])].append(new)
        else:
            fin_arr.append([new])
    print(fin_arr)



groupAnagrams(["eat","tea","tan","ate","nat","bat"])


jump = [0]

jump[jump.index([1,2,3])].append("bolu")
print(jump[0])

