from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head

        while n:
            p2 = p2.next
            n -= 1

        if not p2:
            head = p1.next
            return head

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return head
