for _ in range(int(input())):
	n, k = map(int, input().split())
	for x in range(2):
		if n - x * k >= 0 and (n - x * k) % 2 == 0:
			print("YES")
			break
	else:
		print("NO")