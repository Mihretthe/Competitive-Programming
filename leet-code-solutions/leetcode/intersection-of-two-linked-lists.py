# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visit = set()

        a = headA
        b = headB

        la = 0
        lb = 0

        while a:
            la += 1
            a = a.next
        
        while b:
            lb += 1
            b = b.next

        a = headA
        b = headB

        while la > lb:
            a = a.next
            la -= 1

        while lb > la:
            b = b.next
            lb -= 1

        while a and b:
            if a == b:
                return a

            a = a.next
            b = b.next

                
        return None
            