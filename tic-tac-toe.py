def winner(character, lists):
    for i in lists:
        if all(val == character for val in i):
            return True
    for i in range(3):
        if all(lists[r][i]== character for r in range(3)):
            return True
    if all(lists[i][i] == character for i in range(3)) or all(lists[i][2-i] == character for i in range(3)):
        return True
    return False
for j in range(int(input())):
    a = [input() for _ in range(3)]
    for k in ["X","O","+"]:
        if winner(k, a):
            print(k)
            break
    else:
        print("DRAW")
            
