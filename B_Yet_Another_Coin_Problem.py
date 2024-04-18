def get_ans(n):
    ans = 0
    ans += n // 15
    n %= 15
    ans += n // 6
    n %= 6
    ans += n // 3
    n %= 3
    ans += n
    return ans

testcases = int(input())
for i in range(1, testcases + 1):
    n = int(input())
    if n < 10:
        print(get_ans(n))
    elif n < 20:
        print(min(get_ans(n), get_ans(n - 10) + 1))
    else:
        print(min(get_ans(n), get_ans(n - 10) + 1, get_ans(n - 20) + 2))