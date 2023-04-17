class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        c=s.split(" ")
        a=[]
        b=[]
        for i in c:
            if i.isnumeric():
                a.append(int(i))
        for i in a:
            if a.count(i)==1:
                b.append(i)
        b.sort()
        if a==b:
            return True
        else:
            return False