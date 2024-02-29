# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def traverse(root, level):
            if root:
                if len(ans) > level:
                    if level % 2 == 1:
                        ans[level].appendleft(root.val)
                    else:
                        ans[level].append(root.val)
                else:
                    ans.append(deque([root.val]))
                level += 1
                traverse(root.left, level)
                traverse(root.right, level)
        
        traverse(root, 0)

        return ans