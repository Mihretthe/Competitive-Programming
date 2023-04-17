class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a=""
            for i in word:
                a+=i
                if a[-1]==ch:
                    break
            b=word[len(a):]
            a=a[::-1]
            return a+b
        else:
            return word