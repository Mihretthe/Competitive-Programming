class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        check = []
        for i in range(len(arr) - 1):
            if not check:
                if arr[i] > arr[i  + 1]:
                    check.append(1)
                elif arr[i] < arr[i  + 1]:
                    check.append(-1)
            else:
                checker = 0
                if arr[i] > arr[i  + 1]:
                    checker = 1
                elif arr[i] < arr[i  + 1]:
                    checker = -1
                else:
                    checker = 0
                
                if check[-1] == checker:
                    ans = max(len(check) + 1, ans)
                    check = [checker]
                else:
                    if checker != 0:
                        check.append(checker)
                        
                    else:
                        ans = max(len(check)+1, ans)
                        check = []
            # print(check)
        ans = max(len(check)+1, ans)
                    
        return ans
                
        
        