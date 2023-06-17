# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def trav(root: Optional[TreeNode],a)-> List[int]:
            if  root:
                a.append(root.val)
                trav(root.left,a)
                trav(root.right,a)
            return a
        n=[i for i in trav(root,[]) if low<=i<=high]
        
        return sum(n)
                
            