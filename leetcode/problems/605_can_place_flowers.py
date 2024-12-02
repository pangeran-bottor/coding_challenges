from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        for idx in range(1, len(flowerbed) - 1):
            if flowerbed[idx] == 1:
                continue

            if flowerbed[idx - 1] == flowerbed[idx + 1] == 0:
                n -= 1
                flowerbed[idx] = 1

            if n == 0:
                return True

        return False
