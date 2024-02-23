from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    frequency = defaultdict(set)
    hashmap = defaultdict(int)
    letters = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    ans = []

    for i in range(n):
        if a[i] == 0:
            hashmap[letters[index]] = 1
            frequency[1].add(letters[index])
            ans.append(letters[index])
            index += 1            
        else:
            letter = frequency[a[i]].pop()
            ans.append(letter)
            hashmap[letter] += 1
            frequency[hashmap[letter]].add(letter)

    print("".join(ans))