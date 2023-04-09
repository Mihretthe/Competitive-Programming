# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=head
        a=[]
        while q:
            a.append(q.val)
            q=q.next
        if a:
            p=ListNode(a[-1])
            a=a[:len(a)-1]
            for i in a:
                node=ListNode(i,p.next)
                p.next=node
            return p
        else:
            return head