# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None

        track = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            current = track.next
            track.next = prev
            prev = track
            track = current
            
            
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
