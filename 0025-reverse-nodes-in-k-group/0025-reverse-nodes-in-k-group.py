# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q=head
        a=[]
        if k==1:
            return head
        while q!=None:
            a.append(q.val)
            q=q.next
        n=len(a)
        if n%k!=0:
            n=n-n%k
        else:
            n=len(a)
        i=0
        b=k
        while i<n:         
            a[i:k]=reversed(a[i:k])
            i+=b
            k+=b
        a=list((reversed(a)))
        p=ListNode(a[-1])
        a=a[:len(a)-1]
        for i in a:
            node=ListNode(i,p.next)
            p.next=node
        return p
        