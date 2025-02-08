from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict


lesser_after = defaultdict(int)
greater_before = defaultdict(int)
            
def merge(left, right):
    lenLeft = len(left)
    lenRight = len(right)
    i = 0
    j = 0
    ans = []
    while i < lenLeft or j < lenRight:
        if i == lenLeft:
            ans.append(right[j])
            j += 1
            continue
        if j == lenRight:
            # print("he: ", left[i], lesser_after)
            ans.append(left[i])
            lesser_after[left[i]] += j
            i += 1
            continue

        if left[i] <= right[j]:
            lesser_after[left[i]] += j
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
         
    return ans

def mergeSort(left, right,a):
    if left == right:
        return [a[left]]
    
    mid = (left + right) // 2
    lefty = mergeSort(left, mid, a)
    righty = mergeSort(mid + 1, right,a)
    
    return merge(lefty, righty)



def merge2(left, right):
    lenLeft = len(left)
    lenRight = len(right)
    i = 0
    j = 0
    ans = []
    
    while i < lenLeft or j < lenRight:
        if i == lenLeft:
            ans.append(right[j])
            j += 1
            continue
        if j == lenRight:
            ans.append(left[i])
            i += 1
            continue

        if left[i] > right[j]:
            greater_before[right[j]] += lenLeft - i
            ans.append(right[j])
            j += 1
        else:
            ans.append(left[i])
            i += 1
    
    return ans

def merge2Sort(left, right, a):
    if left == right:
        return [a[left]]
    
    mid = (left + right) // 2
    lefty = merge2Sort(left, mid, a)
    righty = merge2Sort(mid + 1, right, a)
    
    return merge2(lefty, righty)

def solve():
    n = I()
    a = IL()
    mergeSort(0, n - 1, a)
    merge2Sort(0, n - 1, a)

    
  

    
    
    ans = 0
    for i in a:
        ans += greater_before[i] * lesser_after[i]
    
    print(ans)


    
 
 
 
 
T = 1
for _ in range(T):
    solve()