# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(result, root):
            if root:
                inorder(result, root.left)
                result.append(root.val)
                inorder(result, root.right)
            return result
        return inorder([], root)