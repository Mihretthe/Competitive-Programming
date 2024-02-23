length, k = map(int, input().split())
s = input()

left = 0
right = 0
count_a = 0
count_b = 0
max_beauty = 0

for right in range(length):
    if s[right] == "a":
        count_a += 1
    else:
        count_b += 1
    
    while left < length and min(count_a, count_b) > k:
        if s[left] == 'a':
            count_a -= 1
        else:
            count_b -= 1
        left += 1
    max_beauty = max(max_beauty, right - left + 1)

print(max_beauty)
    