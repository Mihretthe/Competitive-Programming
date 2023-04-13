# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q=head
        a=[]
        while q:
            a.append(q.val)
            q=q.next
        if a==a[::-1]:
            return True
        else:
            return False