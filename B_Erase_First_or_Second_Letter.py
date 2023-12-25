for _ in range(int(input())):
    n = int(input())
    s = input()

    collect = set()
    collect.add(s)

    

    collect.discard('')

    print(len(collect))
        