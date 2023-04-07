# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        n=head
        c=0
        while n:
            c+=1
            n=n.next
        k=k%c
        while k>0:
            q=head
            while q.next.next!=None:
                q=q.next
            p=q.next
            q.next=p.next
            p.next=head
            head=p
            k-=1
        return head