class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        print(s)
        a=s.split(" ")
        print(a)
        return len(a[-1])