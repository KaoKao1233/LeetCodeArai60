# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        visited = set()
        while current.next is not None:
            if current not in visited:
                visited.add(current)
                current = current.next
            else:
                return current
                
        return None