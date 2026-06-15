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

        while current is not None:
            if current in visited:
                return current
            visited.add(current)
            current = current.next

        return None