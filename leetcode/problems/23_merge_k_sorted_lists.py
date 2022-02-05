from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l is not None]
        if len(lists) == 0:
            return None
        
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        arr.sort()
        
        result = pointer = ListNode(0)
        for a in arr:
            pointer.next = ListNode(a)
            pointer = pointer.next
        return result.next
