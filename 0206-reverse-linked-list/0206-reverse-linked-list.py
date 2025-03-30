# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to reverse the linked list
        # meaning every next pointer should point in opposite direction

        #  to start of the first node should point to None and the second node should point to the first and so on

        prev = None
        # Algorithm
        # 1. point to the previous node
        # 2. assign the current node to the previous 
        # 3. do this until there is no more node left

        current = head

        while current:
            temp = current.next # temporarily holding what is the next
            current.next = prev # this is the reverse part
            prev = current
            current = temp

        # at the end prev is going to have our linked list head

        return prev
