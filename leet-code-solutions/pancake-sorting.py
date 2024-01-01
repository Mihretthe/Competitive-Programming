class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []

        def flip(arr,index,n):
            arr = arr[:index + 1][::-1] + arr[index + 1:]
            arr = arr[:n][::-1] + arr[n:]
            return arr

        while n > 1:
            index = arr.index(n)
            ans.append(index + 1)
            arr = flip(arr,index,n)
            ans.append(n)
            n -= 1
        return ans