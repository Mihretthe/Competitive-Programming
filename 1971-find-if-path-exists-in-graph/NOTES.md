visited = [source]
def dfs(i, visited):
if visited[-1] == destination:
return True
# if i + 1 > len(visited):
#     return False
print(visited)
for j in range(i,len(edges)):
a, b = edges[j]
if a == source:
visited.append(b)
dfs(j + 1, visited)
elif b == source:
visited.append(a)
dfs(j + 1, visited)
​
return False
return dfs(0, visited)