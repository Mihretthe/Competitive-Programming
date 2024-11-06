class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = []
        for ind in nums:
            arr.append(bin(ind)[2:].count('1'))
        
        sub = arr[0]
        last = 0
        cp = 1
        fin = []
        print(arr)
        for ind in range(1, len(arr)):
            if arr[ind] == sub:
                cp +=1
            else:
                tmp = nums[last:last+cp]
                tmp.sort()
                fin.extend(tmp)
                last  = ind
                cp =  1
                sub = arr[ind]
                # print("yum", tmp)
        
        print(last,cp)
        tmp = nums[last:last+cp]
        tmp.sort()
        fin.extend(tmp)
        print(fin)
        x = sorted(fin)
        print(x)
        if fin == x:
            return True
        return False





        