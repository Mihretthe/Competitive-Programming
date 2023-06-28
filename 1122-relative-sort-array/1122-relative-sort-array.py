class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        counting sort
        
        """
        ans=[]
        for i in arr2:
            a=[i for j in range(arr1.count(i))]
            ans+=a
        a=[i for i in arr1 if i not in ans]
        a.sort()
        ans+=a
        return ans