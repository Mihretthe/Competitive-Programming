class Solution:
    def discountPrices(self, s: str, d: int) -> str:
        a=s.split(" ")
        for i in range(len(a)):
            if a[i][0]=="$" and "e" not in a[i] and a[i].count("$")==1 and len(a[i])>1 and a[i][1:].isnumeric():
                c=float(a[i][1:])
                if d==100:
                    a[i]="$0.00"
                else:
                    c-=(c*d/100)
                    a[i]="$"+"%.2f"%c
            else:
                continue
        return " ".join(a)
            
            