# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        curr = head
        answer = []
        first = 0
        if length > k:
            first = length % k 


        for i in range(k):
            c = (length//k) - 1
            if first:
                c += 1
                first -= 1
            b = curr
            ans = curr
            while curr and c > 0:
                curr = curr.next
                b = b.next
                c -= 1
            if b:
                curr = curr.next
                b.next = None
                
            answer.append(ans)
            
        return answer
            