class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        num=[i for i in num]
        num.sort()
        return int("".join([num[0],num[-1]]))+int("".join([num[1],num[2]]))
        
        