# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = head
            even = head.next
            tail = even

            while tail and tail.next:
                odd.next = tail.next
                odd = tail.next
                tail.next = odd.next
                tail = odd.next
            odd.next = even

            return head
        

