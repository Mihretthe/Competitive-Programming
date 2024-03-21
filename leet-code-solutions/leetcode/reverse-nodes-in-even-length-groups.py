# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        tail = head

        while head:
            trailer = head.next
            head.next = pre
            pre = head
            head = trailer
        
        
        
        return [pre, tail]

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        dummy = ListNode(0, ans)
        n = 0
        if head and not head.next:
            return head
        while head: 
            previous = head
            count = 0
            for i in range(n):                
                if head:
                    count += 1
                    head = head.next  

                if not head:
                    count -= 1
                    break 
                
           
            if head:
                trailer = head.next
                head.next = None
            else:
                trailer = None
            

            if count % 2 == 0:
                node = previous
                ans.next = node
                ans = head
            else:
                node, tail = self.reverseList(previous)  

                ans.next = node
                ans = tail
            
            head = trailer
            n += 1

        return dummy.next
                
                
                
            


                

