# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = l1
        second = l2
        carry = 0
        last = l1
        while first and second:
            first_val = first.val
            second_val = second.val

            if first_val + second_val + carry > 9:
                first.val = (first_val + second_val + carry) % 10
                carry = 1
            else:
                first.val += second_val + carry
                carry = 0
            last = first
            first = first.next
            second = second.next
        while first:
            # print(first, carry)    
            if (first.val + carry) > 9:
                first.val = (first.val + carry) % 10
                carry = 1
            else:
                first.val += carry
                carry = 0
                
            last = first  
            first = first.next
        # print(l1, carry)

        if second:
            last.next = second

        while second:
            # print("second")
            if second.val + carry > 9:
                second.val = (second.val + carry) % 10
                carry = 1
            else:
                second.val += carry
                carry = 0
            last = second
            second = second.next
                

        if carry:
            last.next = ListNode(1)
            last = last.next
        
        
        
        return l1