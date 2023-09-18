# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def trav(root, ans):
            if root:
                ans.append(root.val)
                trav(root.left, ans)
                trav(root.right, ans)
            return ans
        return len(trav(root, []))