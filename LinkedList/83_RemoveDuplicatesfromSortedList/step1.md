# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        node = head
        
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
        
        return head

=== 上記TLEのため、書き直し ===

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        node = head

        while node is not None:
            while node is not None and node.next is not None and node.val == node.next.val:
                node.next = node.next.next
        
        return head

=== 再度、上記がTLEになるため恐らくどこかで無限ループしているため見直し ===

# nodeを前に一歩も進めていなかった...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return
        
        node = head

        while node is not None:
            while node is not None and node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
                
        return head