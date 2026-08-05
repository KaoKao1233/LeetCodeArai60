# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_a = l1
        list_b = l2
        sum_list = ListNode(val = 0)
        head = sum_list
        sum_list_runner = head
        is_carrying = False

        while not (list_a.next is None and list_b.next is None):
            if list_a is not None and list_b is not None:
                sum_value = list_a.val + list_b.val
            elif list_a is not None and list_b is None:
                sum_value = list_a.val
            else:
                sum_value = list_b.val
            
            if is_carrying:
                sum_value += 1
            if sum_value > 9:
                is_carrying = True
                sum_value = 0
            else:
                is_carrying = False
            
            sum_list_runner.val = sum_value
            sum_list_runner.next = ListNode()
            sum_list_runner = sum_list_runner.next
        
        sum_list_runner.next = None
        
        return head



### 解法参照後

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
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            total = val1 + val2 + carry
            carry,digit = divmod(total,10)

            node.next = ListNode(val = digit)
            node = node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return dummy.next