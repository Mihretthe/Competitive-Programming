class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
    
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
        self.hashmap['tail'] = [self.tail, self.dummy]
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node, prev = self.hashmap[key]
            prev.next = prev.next.next
            temp = prev.next
            if temp == self.tail:
                self.hashmap['tail'][1] = prev 
            else:
                self.hashmap[temp.key][1] = prev 
            
            previous = self.hashmap['tail'][1]
            node.next = None
            previous.next = node
            node.next = self.tail
            self.hashmap['tail'][1] = node
            self.hashmap[key] = [node, previous]

           
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            node, prev = self.hashmap[key]
            node.val = value
            prev.next = prev.next.next
            temp = prev.next
            if temp == self.tail:
                self.hashmap['tail'][1] = prev 
            else:
                self.hashmap[temp.key][1] = prev 
            
            previous = self.hashmap['tail'][1]
            node.next = None
            previous.next = node
            node.next = self.tail
            self.hashmap['tail'][1] = node
            self.hashmap[key] = [node, previous]

            
            return node.val
            
        else:
            if len(self.hashmap) - 1 == self.capacity:
                node = self.dummy.next
                nextt = node.next
                if nextt == self.tail:
                    self.hashmap['tail'][1] = self.dummy
                else:
                    self.hashmap[nextt.key][1] = self.dummy
                del self.hashmap[node.key]
                self.dummy.next = self.dummy.next.next

            new_node = ListNode(key, value)
            previous = self.hashmap['tail'][1]
            new_node.next = None
            previous.next = new_node
            new_node.next = self.tail
            self.hashmap['tail'][1] = new_node
            self.hashmap[key] = [new_node, previous]

   
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)