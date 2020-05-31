# https://leetcode.com/contest/weekly-contest-191/problems/maximum-product-of-two-elements-in-an-array/

def maxProduct(nums):
    nums.sort(reverse=True)
    result = (nums[0]-1)*(nums[1]-1)
    return result
