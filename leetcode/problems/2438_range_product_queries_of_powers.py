from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power = 0
        pre_powers = [1]
        while n:
            if n % 2 == 1:
                pre_powers.append(pre_powers[-1] * 2**power)
            power += 1
            n //= 2
        # print(pre_powers)
        answers = []
        for l, r in queries:
            answers.append((pre_powers[r + 1] // pre_powers[l]) % (10**9 + 7))
        return answers
