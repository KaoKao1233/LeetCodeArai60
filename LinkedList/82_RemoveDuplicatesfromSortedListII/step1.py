from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### ボツ

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        node = head
        is_repeated = False
        latest_number = node.val
        last_number_node = head
        
        while node.next is not None:
            
            if not is_repeated:
                if node.val == latest_number:
                    is_repeated = True
                elif node.val != latest_number:
                    latest_number = node.val
                    last_number_node = node
            elif is_repeated:
                if node.val == latest_number:
                    node = node.next
                    continue
                elif node.val != latest_number:
                    is_repeated = False
                    latest_number = node.val
                    last_number_node.next = node
            node = node.next


### dummyheadを用いる/今と次のノードの比較に方針変更

# Definition for singly-linked list.
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
            repeated_number = node.next.val
            while node.next is not None and node.next.val == repeated_number:
                node.next = node.next.next

        return dummy_head.next