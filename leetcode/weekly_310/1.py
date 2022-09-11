from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num % 2 == 0:
                if num not in counter:
                    counter[num] = 0
                counter[num] += 1
            
        if len(counter) == 0:
            return -1
        
        counter_list = []
        for num, count in counter.items():
            counter_list.append((num, count))
        counter_list.sort(key=lambda x: (-x[1], x[0]))
        
        return counter_list[0][0]
