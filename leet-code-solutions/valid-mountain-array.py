class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        flag = False
        for i in range(len(arr) - 1):

            if flag:
                if arr[i + 1] >= arr[i]:
                    return False
            else: 
                if i > 0 and arr[i] > arr[i + 1]:
                    flag = True
                elif i == 0 and arr[i] > arr[i + 1]:
                    return False              
                elif arr[i] == arr[i + 1]:
                    return False

        if flag:
            return True

        return False
                
