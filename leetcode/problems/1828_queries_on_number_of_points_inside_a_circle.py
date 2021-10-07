from typing import List


class Solution:
    def countPoints(self, points: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        def get_lower_bound(points, x_center, radius):
            low = 0
            high = len(points)-1
            lb = len(points) - 1

            while low <= high:
                mid = (low + high) // 2
                x = points[mid][0]

                if (x_center - x <= radius):
                    high = mid-1
                    lb = mid
                else:
                    low = mid + 1
            return lb

        points.sort()  # by default, this will be sorted based on x
        answer = []
        for cx, cy, cr in queries:
            count = 0
            lb = get_lower_bound(points, cx, cr)

            for px, py in points[lb:]:
                if px - cx > cr:
                    break
                if (px-cx)**2 + (py-cy)**2 <= cr*cr:
                    count += 1
            answer.append(count)
        return answer
