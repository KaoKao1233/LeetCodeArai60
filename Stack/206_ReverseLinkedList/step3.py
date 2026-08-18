from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return None

#         moved_node = head
#         reversed = None

#         while moved_node.next:
#             next_node = moved_node.next #次に移動させるパイをマーク
#             moved_node.next = reversed  #移動させたパイを山Bの先頭に重ねる
#             reversed = moved_node       #山Bの先頭にマークをつける
#             moved_node = next_node      #移動するパイを掴む

#         return reversed


# v2

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        reversed_head = None
        moved_node = head

        while moved_node is not None:
            node_next = moved_node.next
            moved_node.next = reversed_head
            reversed_head = moved_node
            moved_node = node_next

        return reversed_head