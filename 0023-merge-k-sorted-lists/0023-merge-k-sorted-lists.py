# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        if len(lists)==0:
            return None
        for i in lists:
            q=i
            while q:
                a.append(q.val)
                q=q.next
        a.sort(reverse=True)
        if a:
            p=ListNode(a[-1])
            a=a[:len(a)-1]
            for i in a:
                node=ListNode(i,p.next)
                p.next=node
            return p
        else:
            return None