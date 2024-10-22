# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        deck = deque([(-1, root)])
        parent_sum = defaultdict(int)

        while deck:
            parent, node = deck.popleft()

            parent_sum[parent] += node.val

            if node.left:
                deck.append((node, node.left))
            
            if node.right:
                deck.append((node, node.right))
        
        # print(parent_sum.values())

        deck = deque([(-1, root)])

        while deck:
            total = 0
            nodes = []
            # print(deck)
            for i in range(len(deck)):
                parent, node = deck.popleft()
                total += node.val
                nodes.append((parent, node))
                
                if node.left:
                    deck.append((node, node.left))
                
                if node.right:
                    deck.append((node, node.right))
            for p, n in nodes:
                n.val = total - parent_sum[p]

        return root



        