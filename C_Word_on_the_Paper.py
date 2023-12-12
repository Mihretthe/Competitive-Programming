from collections import Counter

for _ in range(int(input())):
    idx = 0
    word = ""

    for i in range(8):
        s = input()
        counter = Counter(s)
        if len(counter) == 1:
            continue
        else:
            for key in counter:
                if key != '.':
                    word += key
    print(word)
