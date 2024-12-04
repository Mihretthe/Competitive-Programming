class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        first = 0
        second = 0

        letters = "abcdefghijklmnopqrstuvwxyz"

        length1 = len(str1)
        length2 = len(str2)

        while first < length1 and second < length2:
            if str1[first] == str2[second]:
                first += 1
                second += 1
            else:
                if (letters.index(str1[first]) + 1) %  26 == letters.index(str2[second]):
                    second += 1
                first += 1

        return second == length2