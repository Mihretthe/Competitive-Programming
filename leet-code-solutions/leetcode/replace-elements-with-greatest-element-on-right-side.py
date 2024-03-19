class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        maxi = -1
        ans = []

        for i in range(length - 1, -1, -1):
            if maxi > arr[i]:
                ans.append(maxi)
            else:
                ans.append(maxi)
                maxi = arr[i]
                
        
        return ans[::-1]

