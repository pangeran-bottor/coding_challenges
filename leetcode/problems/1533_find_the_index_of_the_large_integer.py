# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader) -> int:
        def helper(l, r):
            if r - l <= 2:
                c = reader.compareSub(l, l, r, r)
                if c == 1:
                    return l
                if c == -1:
                    return r
                if c == 0:
                    return r - 1

            mid = (l + r) // 2
            odd = (r - l + 1) % 2
            c = reader.compareSub(l, mid - odd, mid + 1, r)
            if c == 1:
                return helper(l, mid - odd)
            if c == -1:
                return helper(mid + 1, r)
            return mid

        n = reader.length()
        ans = helper(0, n - 1)
        return ans
