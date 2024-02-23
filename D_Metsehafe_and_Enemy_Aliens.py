for _ in range(int(input())):
    n = int(input())
    aliens = list(map(int, input().split()))
    aliens.sort()

    ans = 0
    combo = 0

    left, right = 0, n - 1

    while left < right:
        combo += aliens[left]
        if combo >= aliens[right]:
            ans += aliens[right] + 1
            combo -= aliens[right]
            right -= 1
        left += 1
    
    if left == right:
        combo += aliens[right]

    ans += ((combo + 1) // 2) + 1 if combo > 1 else combo

    print(ans)