# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        o = odd
        e = even

        q = head
        t = 1
        while q:
            if t % 2 == 1:
                o.next = ListNode(q.val)
                o = o.next
            else:
                e.next = ListNode(q.val)
                e = e.next
            t += 1
            q = q.next
        o.next = even.next

        return odd.next