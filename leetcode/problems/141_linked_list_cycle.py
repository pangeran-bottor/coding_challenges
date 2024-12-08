from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slowp, fastp = head, head.next
        while slowp and fastp:
            if slowp == fastp:
                return True

            slowp = slowp.next
            fastp = fastp.next.next if fastp.next else None
        return False
