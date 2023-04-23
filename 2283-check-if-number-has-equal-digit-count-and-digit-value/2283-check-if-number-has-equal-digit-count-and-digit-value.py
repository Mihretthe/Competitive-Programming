class Solution:
    def digitCount(self, num: str) -> bool:
        for i in num:
            if num.count(str(num.index(i)))==int(i):
                continue
            else:
                return False
        return True