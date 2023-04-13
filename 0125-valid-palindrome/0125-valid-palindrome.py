class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        a=""
        for i in s:
            if i.isalnum():
                a+=i.lower()
            else:
                continue
        b=a[::-1]
        if a==b:
            return True
        else:
            return False