# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        stack 1 the first list
        stack 2 the second list 
        the traversing listnode starts from the s.d. 
        so store it to the stack 
        the add it to the pop 
        if the number of the sum of the digit is more than one then add the s.d to the next value of the stack then continue that until the stack is empty after 
        if the stack of one is empty and the stack of the other is not empty add zero to it
        """
        stack1 = []
        stack2 = []
        first_list = l1
        second_list = l2
        answer = ListNode()
        answer = answer.next
        while first_list or second_list:
            if second_list == None and first_list != None:
                stack2.insert(0,0)
                stack1.append(first_list.val)
                first_list = first_list.next  
            elif second_list != None and first_list == None:
                stack1.insert(0,0)
                stack2.append(second_list.val)
                second_list = second_list.next
            else:
                stack1.append(first_list.val)    
                stack2.append(second_list.val)
                first_list = first_list.next   
                second_list = second_list.next
        while stack1 and stack2:
            if (stack1[-1] + stack2[-1]) // 10 < 1:
                node = ListNode(stack1.pop()+stack2.pop())
                if answer:
                    node.next=answer
                    answer = node
                else:
                    answer = node
            else:
                val = stack1.pop()+stack2.pop()
                
                node = ListNode(val%10)
                if stack1:
                    stack1[-1]+=val//10
                else:
                    stack1.append(val//10)
                    stack2.append(0)
                if answer:
                    node.next=answer
                    answer = node
                else:
                    answer = node
                
        return answer
