import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = []
        for idx, (e_time, p_time) in enumerate(tasks):
            indexed_tasks.append((e_time, p_time, idx))
        indexed_tasks.sort()

        available_tasks = []
        heapq.heapify(available_tasks)

        n = len(tasks)
        task_idx = 0
        cur_time = 0
        ans = []

        while task_idx < n or len(available_tasks) > 0:
            if len(available_tasks) == 0 and cur_time < indexed_tasks[task_idx][0]:
                cur_time = indexed_tasks[task_idx][0]

            while task_idx < n and cur_time >= indexed_tasks[task_idx][0]:
                _, p_time, initial_idx = indexed_tasks[task_idx]
                heapq.heappush(available_tasks, (p_time, initial_idx))
                task_idx += 1

            p_time, initial_idx = heapq.heappop(available_tasks)
            ans.append(initial_idx)
            cur_time += p_time

        return ans
