# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q=head
        p=head
        i=1
        while q and i<k:
            q=q.next
            i+=1
        c=0
        while p:
            c+=1
            p=p.next
        n=c-k+1
        s=head
        i=1
        while s and i<n:
            s=s.next
            i+=1
        q.val, s.val=s.val,q.val
        return head