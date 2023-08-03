# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root, result):
            if root:
                inOrder(root.left, result)
                result.append(root.val)
                inOrder(root.right, result)
            return result
        ans = inOrder(root, [])
        s = sorted(list(set(ans)))
        return ans == s