# https://leetcode.com/contest/weekly-contest-192/problems/the-k-strongest-values-in-an-array/


class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        new_list = []
        median = arr[(len(arr)-1)//2]
        for el in arr:
            new_list.append((el, abs(el-median)))
        new_list.sort(key=lambda x: (-x[1], -x[0]))
        ans = [el[0] for el in new_list[:k]]
        return ans