# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def trav(result, root):
            if root:
                result.append(root.val)
                trav(result, root.left)      
                trav(result, root.right)
            return result
        result = trav([], root)
        resultSet = set(result)
        max_count = 1
        for i in resultSet:
            max_count = max(max_count, result.count(i))
        return [i for i in resultSet if result.count(i) == max_count]