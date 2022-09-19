from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        seats.sort()
        students.sort()
        N = len(seats)
        for i in range(N):
            ans += abs(seats[i] - students[i])
        return ans
