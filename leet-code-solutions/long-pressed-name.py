class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        checker = ""

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                checker += name[i]
                i += 1
                j += 1
            else:
                if i > 0 and typed[j] == name[i - 1]:
                    while j < len(typed) and typed[j] == name[i - 1]:
                        j += 1
                else:
                    return False
        
        
        return typed[j:] == name[-1] * (len(typed) - j) and checker == name
            