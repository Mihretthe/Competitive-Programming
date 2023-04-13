# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        q=head
        a=[]
        while q:
            a.append(q.val)
            q=q.next
        l=0
        r=len(a)-1
        b=[]
        while l<r:
            b.append(a[l]+a[r])
            l+=1
            r-=1
        return max(b)
            