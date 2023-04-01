# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=head
        p=ListNode()
        a=[]
        while q!=None:
            if a and q.val in a:
                q=q.next
            else:
                a.append(q.val)
                q=q.next
        if a==[]:
            return None
        a.sort(reverse=True)
        p.val=a[-1]
        for i in a[:len(a)-1]:
            node=ListNode(i,p.next)
            p.next=node
            
        return p
        