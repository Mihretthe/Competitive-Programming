class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix_common_array = []
        i=1
        n=len(A)
        while i<=n:
            prefix_common_array.append(len([j for j in A[:i] if j in B[:i]]))
            i+=1
        return prefix_common_array
            