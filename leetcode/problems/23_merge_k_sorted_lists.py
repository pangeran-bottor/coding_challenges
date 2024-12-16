import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        new_node = ListNode()
        curr = new_node

        while heap:
            _, idx, next_node = heapq.heappop(heap)
            curr.next = next_node
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, idx, curr.next))

        return new_node.next
