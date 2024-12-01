from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_set = set()
        for num in arr:
            if (num * 2 in num_set) or (num // 2 in num_set and num % (num // 2) == 0):
                return True
            num_set.add(num)
        return False
