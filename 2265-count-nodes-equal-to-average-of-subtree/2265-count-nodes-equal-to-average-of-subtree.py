# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def trav(root):
            nonlocal count
            if not root:
                return (0,0)
            left, suml = trav(root.left)   
            right, sumr = trav(root.right)
            totalc = left + right + 1
            totalsum = root.val + suml + sumr
            ave = totalsum // totalc
            if ave == root.val:
                count+=1
            return (totalc, totalsum)
        trav(root)
        return count