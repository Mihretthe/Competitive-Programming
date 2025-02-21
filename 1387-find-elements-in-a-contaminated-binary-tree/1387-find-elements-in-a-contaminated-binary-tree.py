# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        deck = deque([root])
        root.val = 0
        self.collect = set([0])

        while deck:
            
            node = deck.popleft() 
            if node.left:
                self.collect.add(2 * node.val + 1)
                node.left.val = 2 * node.val + 1
                deck.append((node.left))
            if node.right:
                self.collect.add(2 * node.val + 2)
                node.right.val = 2 * node.val + 2
                deck.append((node.right))
        # print(root)
            

    def find(self, target: int) -> bool:
        return target in self.collect
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)