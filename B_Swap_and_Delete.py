for _ in range(int(input())):
    s = input()
    count_one = s.count("1")
    count_zero = s.count("0")

    print(abs(count_one - count_zero))