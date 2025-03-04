# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # collect k nodes, revert them, add them to the next
        dummy = ListNode(0, head)
        def reverseList(node):
            current = node
            prev = None
            tail =  node

            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return [prev, tail]

        
        current = head
        point = dummy

        while current:
            node = current
            index = 0
            while index < k - 1 and current:
                current = current.next
                index += 1
            if current:
                temp = current.next
                current.next = None
                prev = node
                node, last = reverseList(node)   
                last.next = temp
                point.next = node  
                point = last         
                current = temp
                prev.next = current
                
        
        return dummy.next