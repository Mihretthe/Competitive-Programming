# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def makeBST(left, right):
            if left > right:
                return 
            
            if left == right:
                return TreeNode(nums[left])
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            left_bst = makeBST(left, mid - 1)
            right_bst = makeBST(mid + 1, right)

            root.left = left_bst
            root.right = right_bst

            return root

        return makeBST(0, len(nums) - 1)