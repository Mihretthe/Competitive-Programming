class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                return False
        s=[i for i in password if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        a=[i for i in password if i in "abcdefghijklmnopqrstuvwxyz"]
        return len(password)>=8 and len(s)>0 and len(a)>0 and len([i for i in password if i in "0987654321"])>0 and len([i for i in password if i in "!@#$%^&*()-+"])>0
        