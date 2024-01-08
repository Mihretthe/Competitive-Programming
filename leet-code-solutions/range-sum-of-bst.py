# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def trav(root, ans):
            if root:
                ans.append(root.val)
                trav(root.left, ans)
                trav(root.right, ans)
            return ans
        ans = trav(root, [])
        ans.sort()
        low = ans.index(low)
        high = ans.index(high)

        return sum(ans[low:high + 1])