class Solution:
    def sortVowels(self, s: str) -> str:
        t = ""
        vowels = "AEIOUaeiou"
        v = [i for i in s if i in vowels]
        v = sorted(v)
        j = 0
        for i in s:
            if i in vowels:
                t += v[j]
                j += 1
            else:
                t += i
        return t