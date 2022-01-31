from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        device_counts = []
        for row in bank:
            cur_count = 0
            for ch in row:
                if ch == "1":
                    cur_count += 1
            if cur_count > 0:
                device_counts.append(cur_count)
        if len(device_counts) < 2:
            return 0
        
        result = 0
        for i in range(1, len(device_counts)):
            result += (device_counts[i-1] * device_counts[i])
        return result
