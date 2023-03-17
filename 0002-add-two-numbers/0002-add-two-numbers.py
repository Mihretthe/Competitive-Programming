# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         string , then revert , int ,add, revert, extend
        b=list()
        c=list()
        a=ListNode(0,None)
        while l1!=None:
            b.append(str(l1.val))
            l1=l1.next
        while l2!=None:
            c.append(str(l2.val))
            l2=l2.next
        s="".join(b)
        s=s[::-1]
        v="".join(c)
        v=v[::-1]
        n=int(s)
        n2=int(v)
        z=n+n2
        f=str(z)
        # f=f[::-1]
        x=list()
        x.extend(f)
        i=0
        if len(x)<1:
            return None
        head=ListNode(x[-1])
        for i in range(len(x)-1):
            node=ListNode(x[i],head.next)
            head.next=node
        return head
        # while i < len(x):
        #     node = ListNode(0)
        #     if a:
        #         a.next = node
        #         a.val=int(x[i])
        #         a= node
        #     i+= 1
        #     return a.next