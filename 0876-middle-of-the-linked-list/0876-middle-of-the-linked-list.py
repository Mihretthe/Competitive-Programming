# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=head
        c=0
        while q!=None:
            c+=1
            q=q.next
        if c%2!=0:
            for i in range(1,ceil(c/2)):
                head=head.next
        else:
            for i in range(c//2):
                head=head.next
        return head