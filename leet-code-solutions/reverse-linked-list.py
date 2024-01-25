# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        tracker = head
        prev = None

        while tracker:
            current = tracker.next
            tracker.next = prev
            prev = tracker
            tracker = current
        
        return prev