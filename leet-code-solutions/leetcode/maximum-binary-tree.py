# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        """

        have the maximum index
        create a root node with it

        if len(sliced nums) == 1:
            return TreeNode of the value

        left = recursively call the left maximum
        right = recursively call the minimum

        root.left = left
        root.right = right

        return root
        """
        def makeMBT(nums):
            if not nums:
                return 

            max_value = max(nums)
            max_index = nums.index(max_value)
            
            root = TreeNode(max_value)

            left = makeMBT(nums[:max_index])
            right = makeMBT(nums[max_index + 1:])

            root.left = left
            root.right = right 

            return root

        return makeMBT(nums)
