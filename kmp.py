
def KMP_part_one(p : str) -> list:
    length = len(p)
    ans = [0] * length

    i = 0
    j = 1

    while j < length:
        if p[i] == p[j]:
            i += 1
            ans[j] = i 
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = ans[i - 1]

            


    return ans

print(*KMP_part_one(input()))
assert KMP_part_one('aaacaaaa') == [0, 1, 2, 0, 1, 2, 3, 3]
assert KMP_part_one('dsgwadsgz') == [0, 0, 0, 0, 0, 1, 2, 3, 0]
