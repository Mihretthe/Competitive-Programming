# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        placeholder = dummy
        seeker = dummy
        while seeker and seeker.next:
            seeker = seeker.next
            if seeker.val >= x:
                break
            placeholder = placeholder.next

        
        while seeker and seeker.next:
            if seeker.next.val < x:
                temp = seeker.next
                seeker.next = seeker.next.next
                temp.next = placeholder.next 
                placeholder.next = temp
                placeholder = temp
            else:
                seeker = seeker.next

        return dummy.next 