# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix) -> int:
        def get_idx(row, left, right, binary_matrix, n):
            if left >= n or right < 0 or left > right:
                return -1

            mid = (left + right) // 2
            if binary_matrix.get(row, mid) == 0:
                return get_idx(row, mid + 1, right, binary_matrix, n)

            if (mid - 1 < 0) or (binary_matrix.get(row, mid - 1) == 0):
                return mid

            return get_idx(row, left, mid - 1, binary_matrix, n)

        r, c = binaryMatrix.dimensions()

        left_most = c
        for row in range(r):
            cur_idx = get_idx(row, 0, left_most - 1, binaryMatrix, c)
            if cur_idx > -1:
                left_most = min(left_most, cur_idx)

        return left_most if left_most != c else -1
