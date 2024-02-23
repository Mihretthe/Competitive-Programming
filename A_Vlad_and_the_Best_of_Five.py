for _ in range(int(input())):
    s = input()
    counter = {"A" : 0, "B" : 0}

    for i in s:
        counter[i] += 1
    if counter["A"] > counter["B"]:
        print("A")
    else:
        print("B")