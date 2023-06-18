# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root: Optional[TreeNode], a:List[int])->List[int]:
            if root:
                inorder(root.left,a)
                a.append(root.val)
                inorder(root.right,a)
            return a
        return inorder(root,[])