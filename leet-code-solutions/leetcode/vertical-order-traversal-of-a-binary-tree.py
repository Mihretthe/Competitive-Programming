# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        def traverse(root, level, depth):
            if root:
                hashmap[level].append((depth, root.val))

                depth += 1     
                traverse(root.left,level - 1, depth)                
                traverse(root.right, level + 1, depth)
        
        
        traverse(root,0,0)
        
        keys = list(hashmap.keys())
        keys.sort()
        

        for key in keys:
            hashmap[key].sort()
            answer = []
            for k, v in hashmap[key]:
                answer.append(v)
            yield answer


            