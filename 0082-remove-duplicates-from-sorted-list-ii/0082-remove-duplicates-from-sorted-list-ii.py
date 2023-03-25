# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=[]
        if head!=None:
            q=head
            while q!=None:
                c.append(q.val)
                q=q.next
            a=[]
            for i in c:
                f=c.count(i)
                if f==1:
                    a.append(i)
            if len(a)==0:
                return None
            rehead=ListNode()
            a.sort(reverse=True)
            rehead.val=a[-1]
            for i in range(len(a)-1):
                node=ListNode(a[i],rehead.next)
                rehead.next=node
            return rehead
        else:
            return None
                    
            