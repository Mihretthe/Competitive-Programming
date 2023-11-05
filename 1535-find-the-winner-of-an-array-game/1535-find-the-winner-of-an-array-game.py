class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        a = 0
        m = max(arr)
        while a < k:
            if m == arr[0]:
                break
            if arr[0] > arr[1]:
                a += 1
                
                arr.append(arr[1])
                arr.pop(1)
            else:
                a = 1
                arr = arr[1:] + [arr[0]]
        return arr[0]