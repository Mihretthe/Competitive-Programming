for _ in range(int(input())):
    n = int(input())
    strings = []
    max_elements = 0

    for __ in range(n):
        strings.append(input())

    characters = ["a", "b", "c", "d", "e"]

    for char in characters:
        s = 0
        count = 0
        a = [2 * x.count(char) - len(x) for x in strings]
        a.sort(reverse = True)

        for i in range(n):
            if a[i] + s <= 0:
                break
            s += a[i]
            count += 1
        max_elements = max(max_elements, count)

    print(max_elements)































    # n = int(input())
    # string = []
    # max_elements = 0
    # for i in range(n):
    #     string.append(input())
    # # the_string = "".join(string)
    # # counter = Counter(the_string)

    # # the_string = [x for x in counter if counter[x] == max(counter.values())]
    # the_string = ["a","b","c","d","e"]
    # # print(the_string)

    # for i in the_string:
    #     # string.sort(key = lambda x : x.count(i) if i in x else -len(x), reverse = True)
    #     a = [2 * x.count(i) - len(x) for x in string]
    #     a.sort(reverse = True)
    #     count = 0
    #     s = 0
    #     for j in range(n):
    #         if s + a[j] <= 0:
    #             break
    #         count += 1
    #         s += a[j]
    #         # a[j] += a[j - 1]
    #     # print(a)


    #     max_elements = max(max_elements, count)

    # print(max_elements)
    # print()

    