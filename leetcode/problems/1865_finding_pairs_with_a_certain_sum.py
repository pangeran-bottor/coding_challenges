from typing import Counter, List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_counts = Counter(nums1)
        self.nums2_counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_counts[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_counts[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num1, count1 in self.nums1_counts.items():
            ans += count1 * self.nums2_counts[tot-num1]
        return ans
