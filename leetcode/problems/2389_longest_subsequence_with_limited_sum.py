from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def find_num(arr, num):
            tmp = float("-inf")
            idx = -1
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] == num:
                    return mid
                elif arr[mid] < num:
                    if arr[mid] > tmp:
                        tmp = arr[mid]
                        idx = mid

                        l = mid + 1
                    else:
                        return idx
                else:
                    r = mid - 1

            return idx


        n = len(nums)
        nums.sort()
        for i in range(1, n):
            nums[i] += nums[i-1]

        ans = []
        for q in queries:
            idx = find_num(nums, q)
            ans.append(idx+1)
        return ans
