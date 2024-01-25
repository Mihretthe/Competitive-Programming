# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2

        answer = None
        tail = answer

        while first and second:
            if first.val <= second.val:
                if answer:
                    tail.next = first
                    tail = tail.next
                else:
                    answer = first
                    tail = answer
                first = first.next
            else:
                if answer:
                    tail.next = second
                    tail = tail.next
                else:
                    answer = second
                    tail = answer
                second = second.next
        if second:
            if not answer:
                answer = second
            else:
                tail.next = second
            
        if first:
            if not answer:
                answer = first
            else:
                tail.next = first

        return answer