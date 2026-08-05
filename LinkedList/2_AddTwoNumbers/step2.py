# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            value_l1 = l1.val if l1 is not None else 0
            value_l2 = l2.val if l2 is not None else 0
            total = value_l1 + value_l2 + carry
            carry,digit = divmod(total,10)

            node.next = ListNode(val = digit)
            node = node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return dummy.next