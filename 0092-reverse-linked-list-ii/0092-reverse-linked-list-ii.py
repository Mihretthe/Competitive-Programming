# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        q=head
        a=[]
        while q!=None:
            a.append(q.val)
            q=q.next
        n=list((reversed(a[l-1:r])))
        a=a[:l-1]+n+a[r:]
        a=list(reversed(a))
        p=ListNode(a[-1])
        a=a[:len(a)-1]
        for i in a:
            node=ListNode(i,p.next)
            p.next=node
        return p 
