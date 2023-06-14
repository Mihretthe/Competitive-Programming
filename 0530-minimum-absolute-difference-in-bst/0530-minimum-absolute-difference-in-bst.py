# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev_val = None
        self.inorder_traversal(root)
        return self.min_diff
    
    def inorder_traversal(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        self.inorder_traversal(node.left)
        if self.prev_val is not None:
            self.min_diff = min(self.min_diff, abs(node.val - self.prev_val))
        self.prev_val = node.val
        self.inorder_traversal(node.right)
        