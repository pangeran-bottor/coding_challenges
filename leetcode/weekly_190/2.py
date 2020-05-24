# https://leetcode.com/contest/weekly-contest-190/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

def max_vowels(s, k):
    vowels = "aiueo"

    pre = [0]
    c = 0
    for ch in s:
        if ch in vowels:
            c += 1
        pre.append(c)

    result = 0
    for i in range(k, len(pre)):
        result = max(result, pre[i]-pre[i-k])
    return result
