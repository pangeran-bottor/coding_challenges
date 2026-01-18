from typing import List


class BIT:
    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.bit = [0] * (self.N + 1)
        for idx, num in enumerate(nums):
            self.update(idx, num)

    def update(self, i: int, val: int):
        i += 1
        while i <= self.N:
            self.bit[i] += val
            i += i & -i

    def get_sum(self, i: int) -> int:
        i += 1
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(nums)

    def update(self, index: int, val: int) -> None:
        self.bit.update(index, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.get_sum(right) - self.bit.get_sum(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)Ï
