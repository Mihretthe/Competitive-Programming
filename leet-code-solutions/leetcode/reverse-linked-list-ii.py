# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_ptr = head
        right_ptr = head

        def reverse(head):
            prev = None
            curr = head
            tracker = head

            while tracker:
                curr = tracker.next
                tracker.next = prev
                prev = tracker
                tracker = curr

            return prev

        before = head

        for _ in range(left - 1):
            if _ < left - 2:
                before = before.next
            left_ptr = left_ptr.next
        
        start = None
        if left_ptr:
            start = left_ptr

        
        for _ in range(right - 1):
            right_ptr = right_ptr.next

        last = None
        if right_ptr:
            last = right_ptr.next
            right_ptr.next = None
        if left > 1:
            before.next = reverse(start)
        else:
            s = reverse(start)
            start.next = head
            head = s

        start.next = last
        return head
        
        

        