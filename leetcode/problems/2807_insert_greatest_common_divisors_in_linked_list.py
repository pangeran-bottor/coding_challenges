# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def _gcd(a: int, b: int) -> int:
            if a < b:
                return _gcd(b, a)

            if b == 0:
                return a
            return _gcd(a % b, b)

        prev = head
        while prev and prev.next:
            gcd_node = ListNode(_gcd(prev.val, prev.next.val))
            gcd_node.next = prev.next
            prev.next = gcd_node

            prev = gcd_node.next

        return head
