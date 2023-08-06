# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(p, result):
            if p:
                result.append(p.val)
                trav(p.left, result) 
                trav(p.right, result)
            else:
                result.append(None)
            return result
        return trav(p, []) == trav(q, [])
                