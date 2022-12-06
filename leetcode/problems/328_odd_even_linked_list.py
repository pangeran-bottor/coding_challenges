# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd_p = head
        even_head = head.next
        even_p  = even_head

        while even_p and even_p.next:
            odd_p.next = even_p.next
            odd_p = odd_p.next

            even_p.next = odd_p.next
            even_p = even_p.next

        odd_p.next = even_head
        return head
