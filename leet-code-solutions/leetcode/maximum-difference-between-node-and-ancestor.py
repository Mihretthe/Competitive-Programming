# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_value = 0

        def traverse(root):
            nonlocal max_value

            if not root:
                return (inf, -inf)
            
            left = traverse(root.left)
            right = traverse(root.right)
            minimum = min(left[0], right[0])
            maximum = max(left[1], right[1])

            if minimum != inf and maximum != -inf:
                max_value = max(max_value, abs(minimum - root.val) , abs(maximum - root.val))

            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)                

            min_max = (minimum, maximum)
                
            return min_max
                

        
        traverse(root)       

        return max_value