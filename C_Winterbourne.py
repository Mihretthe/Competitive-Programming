for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    mini = min(a)
    maxi = max(a)
    s = sum(a) + n
    if maxi <= (m - s + mini):
        print("YES")
    else:
        print("NO")




 
   








































# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     if n > m:
#         print("NO")
#     else:
#         a.sort()
#         flag = True
#         at = 0
#         put = ["-"] * m
#         for i in range(n):            
#             at = ((at + a[i]) % m)
#             if put[at] != "-":
#                 print("NO")
#                 break
#             for k in range(1,a[i] % m + 1):
#                 if put[(at - k)] != "-" or put[(at + k)%m] != '-':
#                     print("NO")
#                     flag = False
#                     break
#             if flag == False:
#                 break
#             put[at] = i      
#             at += a[i] % m  
            
            
#         else:
#             print("YES")
        
 

    

        




