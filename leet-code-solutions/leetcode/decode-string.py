class Solution:
    def decodeString(self, s: str) -> str:
        def isString(s):
            for i in s:
                if i not in "abcdefghijklmnopqrstuvwxyz":
                    return False
            return True

        if isString(s):
            return s
        
        # print(s)
        num = ""
        index = 0
        while index < len(s) and s[index] in "0123456789":
            num += s[index]
            index += 1
        if num:
            res = ""
            count = 1
            for i in range(index + 1, len(s)):
                index += 1
                if s[i] == "]":
                    count -= 1
                elif s[i] == "[":
                    count += 1
                if count == 0:
                    break
                
                res += s[i]
            return int(num) * self.decodeString(res) + self.decodeString(s[index + 1:])
        else:
            res = ""
            index = 0
            while index < len(s) and isString(s[index]):
                res += s[index]
                index += 1
            return res + self.decodeString(s[index:])

