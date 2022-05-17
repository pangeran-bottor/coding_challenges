from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        pos = 0
        while start <= end:
            mid = start + (end-start)//2
            if ord(letters[mid]) <= ord(target):
                start = mid + 1
            else:
                pos = mid
                end = mid - 1
            
        return letters[pos]
