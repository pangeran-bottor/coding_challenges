from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_map = {}
        for idx, size in enumerate(groupSizes):
            if size not in size_map:
                size_map[size] = []
            size_map[size].append(idx)

        ans = []
        for size, person_list in size_map.items():
            for i in range(0, len(person_list), size):
                ans.append([p for p in person_list[i:i+size]])
        return ans
