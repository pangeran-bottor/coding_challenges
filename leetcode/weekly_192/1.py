# https://leetcode.com/contest/weekly-contest-192/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
