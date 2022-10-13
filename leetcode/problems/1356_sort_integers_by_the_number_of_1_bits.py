from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count_map = {}
        for num in arr:
            count = bin(num).count("1")
            if count not in count_map:
                count_map[count] = []
            count_map[count].append(num)
        
        ans = []
        count_list = list(count_map.items())
        count_list.sort(key=lambda x: x[0])
        
        for count, nums in count_list:
            nums.sort()
            for num in nums:
                ans.append(num)
        return ans
