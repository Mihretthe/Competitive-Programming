board = ["qwertyuiop","asdfghjkl;","zxcvbnm,./"]

def left(s):
    ans = ""
    where = ""
    for i in s:
        idx = 0
        for j in board:
            if i in j:
                where = j
                idx = j.index(i)
                break
        ans += j[idx + 1]
    return ans
def right(s):
    ans = ""
    where = ""
    for i in s:
        idx = 0
        for j in board:
            if i in j:
                where = j
                idx = j.index(i)
                break
        ans += j[idx - 1]
    return ans

c = input()
s = input()
if c == 'R':
    print(right(s))
else:
    print(left(s))



