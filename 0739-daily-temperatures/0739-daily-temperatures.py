class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=list()
        for i in range(len(temperatures)):
            while a and temperatures[i]>temperatures[a[-1]]:
                j=a.pop()
                temperatures[j]=i-j
            a.append(i)
        for i in range(len(a)):
            temperatures[a.pop()]=0
        return temperatures