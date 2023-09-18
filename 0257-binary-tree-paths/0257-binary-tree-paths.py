# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def isLeaf(root):
            return root and root.left == None and root.right == None
        def trav(root, ans, final):
            if root:
                ans.append(str(root.val))
                if isLeaf(root):
                    final.append("->".join(ans))
                    ans = []
                
                trav(root.left, ans[:], final)
                trav(root.right, ans[:], final)
            return final
        return trav(root, [], [])
                