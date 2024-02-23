s = input()
k = int(input())
w = list(map(int, input().split()))
letters = "abcdefghijklmnopqrstuvwxyz"

m = max(w)

my_list = list(range(len(s) + 1, len(s) + k + 1))

answer = 0

for i in range(len(s)):
    answer += (w[letters.index(s[i])] * (i + 1))


for i in my_list:
    answer += (i * m)

print(answer)