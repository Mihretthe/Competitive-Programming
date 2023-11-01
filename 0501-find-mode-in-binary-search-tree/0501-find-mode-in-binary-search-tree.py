# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def trav(root, ans):
            if root:
                ans.append(root.val)
                trav(root.left,ans)    
                trav(root.right,ans)
            return ans
        trav = trav(root, [])
        ans = []
        counter = Counter(trav)
        m = max(list(counter.values()))
        for i in set(trav):
            if counter[i] == m:
                ans.append(i)
        return ans