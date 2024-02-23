for _ in range(int(input())):
    ab = input()

    

    for right in range(1,len(ab)):
        if ab[right] != "0" and int(ab[:right]) < int(ab[right:]):
            print(ab[:right], ab[right:])
            break
    else:
        print(-1)