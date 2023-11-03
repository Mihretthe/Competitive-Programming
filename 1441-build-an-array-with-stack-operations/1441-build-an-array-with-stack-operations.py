class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        r = list(range(1,n + 1))
        stack = []
        j = 0        
        a = target[j]
        for i in r:
            
            if i == a:
                stack.append("Push")
                j += 1
                if j < len(target):
                    a = target[j]
                else:
                    break
            elif i != a:
                stack.append("Push")
                stack.append("Pop")
        return stack
            