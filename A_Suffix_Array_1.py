s = input()
enumerated_s = list(enumerate(s))

enumerated_s.sort(key = lambda x : x[1])

print(enumerated_s)