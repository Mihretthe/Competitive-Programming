# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(root, ans):
            if root:
                ans.append(root.val)
                traverse(root.left, ans)
                traverse(root.right, ans)

            return ans
        
        counter = Counter(traverse(root, []))
        maxi = max(counter.values())
        answer = []

        for key, value in counter.items():
            if value == maxi:
                answer.append(key)        

        return answer

