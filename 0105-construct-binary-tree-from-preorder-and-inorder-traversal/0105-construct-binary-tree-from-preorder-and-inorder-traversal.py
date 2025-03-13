# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Intution

        # the first element of the preorder array is the root
        # find that element in the inorder array, this way we are sure it's left elements are in it's left and the right's are in it's right.
        # divide the array as a left and a right and treat it again
        # the first one on the divisions are again the root of it's sub array

        
        if not preorder or not inorder:
            return

        index = inorder.index(preorder[0])

        root = TreeNode(val = inorder[index])
        left = self.buildTree(preorder[1:index + 1], inorder[:index])
        right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        root.left = left
        root.right = right

        return root