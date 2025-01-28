# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        array = []

        for linked_list in lists:
            nums = []
            temp = linked_list
            while temp:
                nums.append(temp.val)
                temp = temp.next
            array.extend(nums[:])
        
        array.sort()

        if not array:
            return None


        dummy = ListNode(-1, ListNode(array[0]))
        temp = dummy.next

        for num in array[1:]:
            node = ListNode(num)
            temp.next = node
            temp = temp.next          
            


        return dummy.next