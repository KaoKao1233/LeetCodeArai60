# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        node = dummy_head
        
        while node.next is not None and node.next.next is not None:
            if node.next.val != node.next.next.val:
                node = node.next
                continue
            duplicate_val = node.next.val
            while node.next is not None and node.next.val == duplicate_val:
                node.next = node.next.next
            
        return dummy_head.next