# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=head
        if head==None:
            return None
        if head.next==None:
            return head
        c=0
        while q and q.next:
            c+=2
            q.val, q.next.val=q.next.val,q.val
            q=q.next.next
        else:
            return head
        return head