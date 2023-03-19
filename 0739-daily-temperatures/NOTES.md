class Solution:
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
stack, temp = [], temperatures
for i in range(len(temp)):
while stack and temp[i] > temp[stack[-1]]:
j = stack.pop()
temp[j] = i - j
stack.append(i)
for _ in range(len(stack)):
temp[stack.pop()] = 0
return temp
class Solution:
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
ans=list()
c=max(temperatures)
for i in range(len(temperatures)-1):
if temperatures[i]<temperatures[i+1]:
ans.append(1)
elif temperatures[i] == c:
ans.append(0)
elif temperatures[i]>=temperatures[i+1]:
x=int()
for j in range(i+1,len(temperatures)):
if temperatures[j]>temperatures[i]:
x=j
break
ans.append(x-i) if x-i>0 else ans.append(0)
ans.append(0)
return ans