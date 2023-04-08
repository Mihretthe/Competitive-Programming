# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=head
        while q and q.next:
            q.val, q.next.val=q.next.val,q.val
            q=q.next.next
        else:
            return head