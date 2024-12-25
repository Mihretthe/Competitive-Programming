# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        deck = deque()
        if root:
            deck.append(root)

        answer = []

        while deck:
            maxi = -inf
            for _ in range(len(deck)):
                node = deck.popleft()
                if node.left:
                    deck.append(node.left)
                
                if node.right:
                    deck.append(node.right)
                maxi = max(maxi, node.val)
            answer.append(maxi)
        
        return answer