for _ in range(int(input())):
    n, m = map(int, input().split())
    infected = set(map(int, input().split()))
    bigger = set()
    protected = set()

    while infected:
        stack = set()
        for i in infected:
            if i in bigger and i in protected:
                continue
            if i == 1:
                if n not in bigger and n not in protected:
                    stack.add(n)
                if 2 not in bigger and 2 not in protected:
                    stack.add(2)
                
            elif i == n:
                if n - 1 not in bigger and n - 1 not in protected:
                    stack.add(n - 1)
                if 1 not in bigger and 1 not in protected:
                    stack.add(1)
            else:
                if i - 1 not in bigger and i - 1 not in protected:
                    stack.add(i - 1)
                if i + 1 not in bigger and not i + 1 in protected:
                    stack.add(i + 1)
        if stack:
            protected.add(min(stack))
            stack.remove(min(stack))            
        bigger.update(infected)
        infected = stack
        
    



    print(len(bigger))
