class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i=="../":
                if c==0:
                    continue
                else:
                    c-=1
            elif i=="./":
                c+=0
            else:
                c+=1
        return c