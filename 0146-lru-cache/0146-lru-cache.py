class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
    def __str__(self):
        temp = self.next
        ans = [f"({self.key},{self.val})"]
        while temp:
            ans.append(f"({temp.key},{temp.val})")
            temp = temp.next
        
        return " -> ".join(ans)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = ListNode()
        self.hashmap = {}
        self.tail = ListNode()
        self.dummy.next = self.tail
        self.tail.prev = self.dummy

    def replace(self, node, prev):
        prev.next = prev.next.next
        temp = prev.next
        if temp == self.tail:
            self.tail.prev = prev 
        else:
            temp.prev = prev         
        previous = self.tail.prev
        node.next = None
        previous.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = previous  


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]   
            prev = node.prev         
            self.replace(node, prev)           
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            node = self.hashmap[key]
            prev = node.prev 
            node.val = value
            self.replace(node, prev)            
            
        else:
            if len(self.hashmap) == self.capacity:
                node = self.dummy.next
                nextt = node.next
                nextt.prev = self.dummy
                del self.hashmap[node.key]
                self.dummy.next = self.dummy.next.next

            new_node = ListNode(key, value)
            previous = self.tail.prev
            new_node.next = None
            previous.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
            new_node.prev = previous
            self.hashmap[key] = new_node

   
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)