class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        b=list()
        a=["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or tokens[i][0]=="-" and len(tokens[i])>1:
                b.append(tokens[i])
            elif tokens[i] is a[0]:
                b.append(int(b.pop(-2))+int(b.pop(-1)))
            elif tokens[i] is a[1]:
                b.append(int(b.pop(-2))-int(b.pop(-1)))
            elif tokens[i] is a[2] and b!=[]:
                b.append(int(b.pop(-2))*int(b.pop(-1)))
            elif tokens[i] is a[3] and b[-1]!=0:
                if int(b[-2])//int(b[-1])>=0:
                    b.append(int(b.pop(-2))//int(b.pop(-1)))
                else:
                    b.append(ceil(int(b.pop(-2))/int(b.pop(-1))))
        return int(b[0])