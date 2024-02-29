# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        
        def smallest(root):
            nonlocal k, ans
            if not root:
                return root
            smallest(root.left)
            k -= 1
            if k == 0:
                ans = root
                return    
            smallest(root.right)
            
        smallest(root)
        return ans.val
                

