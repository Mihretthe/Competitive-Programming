for _ in range(int(input())):
    digits = input()
    parity = []
    length = len(digits)

    for i in digits:
        parity.append(int(i) % 2)
    
    # print(*parity)
    backward = []
    forward = []

    for i in range(length):
        j = i - 1
        while j >= 0 and parity[j] != parity[i] :
            j -= 1
        forward.append(j)
        j = i + 1
        while j < length and parity[j] != parity[i]:
            j += 1
        backward.append(j)
    
    print(*forward)
    print(*backward)
    print()



