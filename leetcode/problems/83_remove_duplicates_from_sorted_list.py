from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        while prev and prev.next:
            if prev.val == prev.next.val:
                prev.next = prev.next.next
                continue
            prev = prev.next
        return head
