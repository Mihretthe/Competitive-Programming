class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a=arr[-1]-arr[-2]
        for i in range(0,len(arr)-2):
            if arr[i+1]-arr[i]!=a:
                return False
        return True
        