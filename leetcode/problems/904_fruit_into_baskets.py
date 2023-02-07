from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        run_dict = {}
        start_idx = 0
        ans = 0
        for idx, fruit in enumerate(fruits):
            run_dict[fruit] = run_dict.get(fruit, 0) + 1

            while len(run_dict) > 2:
                run_dict[fruits[start_idx]] -= 1

                if run_dict[fruits[start_idx]] == 0:
                    del run_dict[fruits[start_idx]]

                start_idx += 1

            ans = max(ans, idx - start_idx + 1)

        return ans
