from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        first_half_end = self.get_first_half(head)
        reversed_second_half_start = self.reverse(first_half_end)

        left_head, right_head = head, reversed_second_half_start     

        while right_head.next:
            left_head_next = left_head.next
            left_head.next = right_head
            left_head = left_head_next

            right_head_next = right_head.next
            right_head.next = left_head
            right_head = right_head_next

    def get_first_half(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            next_cur = cur.next
            cur.next = prev

            prev = cur
            cur = next_cur
        return prev
