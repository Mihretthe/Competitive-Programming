class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        a=""
        for i in range(len(word)):
            if word[i].isnumeric():
                a+=word[i]
            else:
                if a and a[-1]==" ":
                    a+=""
                else:
                    a+=" "
        a=a.strip()
        if a:
            b=set()
            for i in a.split(" "):
                b.add(int(i))
            return len(b)
        else:
            return 0
            