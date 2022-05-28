# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            l = 0
            while head is not None:
                head = head.next
                l += 1
            return l
        
        len_a = get_length(headA)
        len_b = get_length(headB)
        
        start_a = len_a - min(len_a, len_b)
        start_b = len_b - min(len_a, len_b)
        
        while start_a > 0:
            headA = headA.next
            start_a -= 1
        while start_b > 0:
            headB = headB.next
            start_b -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        if headA == headB:
            return headA
        return None
