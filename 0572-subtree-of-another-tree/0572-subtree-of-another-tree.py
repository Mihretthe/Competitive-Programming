# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(node):
            deck = deque([node, subRoot])

            while deck:
                forMe =  deck.popleft()
                if not deck:
                    return False
                forSub = deck.popleft()

                if (not forMe.right and forSub.right) or (not forMe.left and forSub.left):
                    return False

                if forMe.val != forSub.val:
                    return False

                if forMe.left:
                    deck.append(forMe.left)
                
                if forSub.left:
                    deck.append(forSub.left)
                
                
                
                if forMe.right:
                    deck.append(forMe.right)
                
                if forSub.right:
                    deck.append(forSub.right)
            
            return True
                
                



        
        deck = deque([root])

        while deck:
            node = deck.popleft()
            if helper(node):
                return True
            
            if node.left:
                deck.append(node.left)
            
            if node.right:
                deck.append(node.right)
        
        return False