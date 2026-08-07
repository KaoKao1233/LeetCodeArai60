from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(next=head)
        node = head
        node_next = node.next
        node.next = None

        while node_next is not None:
            node = node_next
            node_next = node.next
            node.next = dummy.next
            dummy.next = node

        head = dummy.next

        return head