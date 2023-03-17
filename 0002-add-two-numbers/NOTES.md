to append items in a singly linked list
- we should first assign the last element to the head then loop through the list stored until len-1
- create node
- assign or pass the value while initialization of the node
- assign or pass the next as head.next to the node
- then made the head.next=node created
- head=ListNode(x[-1])
for i in range(len(x)-1):
node=ListNode(x[i],head.next)
head.next=node
return head