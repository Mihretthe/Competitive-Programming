# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root, ans):
            if root:
                ans.append(root.val)
                traverse(root.left, ans)
                traverse(root.right, ans)
            else:
                ans.append(None)

            return ans
        
        def traverser(root, ans):
            
            if root:
                ans.append(root.val)
                traverser(root.right, ans)
                traverser(root.left, ans)                
            else:
                ans.append(None)
            

            return ans

        left = []
        right = []
        
        if root:
            left = traverse(root.left, [])
        if root:
            right = traverser(root.right, [])


        return left == right
        
