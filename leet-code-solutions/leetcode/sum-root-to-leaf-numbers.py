# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, digit):
            if not root:
                return 0

            if root and not root.left and not root.right:
                return digit * 10 + root.val

            left = traverse(root.left, digit * 10 + root.val)
            right = traverse(root.right, digit * 10 + root.val)

            return left + right

        return traverse(root, 0) 

            

    