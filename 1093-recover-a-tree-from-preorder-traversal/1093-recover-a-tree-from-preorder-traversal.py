# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # A list of tuples with their value and depth
        tree = []

        index = 0
        length = len(traversal)
        num = []
        while index < length and traversal[index] in "0123456789":
            num.append(traversal[index])
            index += 1
            
        num = int("".join(num))
        root = TreeNode(num)
        
        traversal = traversal[index:]
        index = 0
        length = len(traversal)
        while index < length:
            count = 0
            num = []
            while index < length and traversal[index] == "-":
                count += 1
                index += 1
            while index < length and traversal[index] in "0123456789":
                num.append(traversal[index])
                index += 1
            num = int("".join(num))
            tree.append((num, count))

       

        index = 0
        hashmap = defaultdict(TreeNode)
        hashmap[1] = (root)

        while index < len(tree):
            val, depth = tree[index]
            node = hashmap[depth]
            
            new_node = TreeNode(val)

            if node.left:
                node.right = new_node
                hashmap[depth + 1]=(new_node)

            else:
                node.left = new_node
                hashmap[depth + 1]=(new_node)
               

            index += 1

       
            
        return root


    