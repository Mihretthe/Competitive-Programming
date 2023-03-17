# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        a=list()
        while list1!=None:
            a.append(list1.val)
            list1=list1.next
        while list2!=None:
            a.append(list2.val)
            list2=list2.next
        a.sort(reverse=True)
        
        if len(a)<1:
            return None
        head=ListNode(a[-1])
        for i in range(len(a)-1):
            node=ListNode(a[i],head.next)
            head.next=node
        print(a)
        return head