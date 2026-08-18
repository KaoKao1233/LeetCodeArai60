from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node = head
        stack = []
        
        while node is not None:
            stack.append(node)
            node = node.next

        head = stack.pop()
        node = head

        while stack:
            node.next = stack.pop()
            node = node.next

        node.next = None

        return head